"""
1. Why wasn't LoRA enough?
- LoRA significantly reduces the memory required for gradients and optimizer states, but it still requires loading the
    full-precision pretrained model into GPU memory. For very large models like 65B parameters, the frozen base model
    itself becomes the dominant memory cost, making fine-tuning infeasible on a single GPU.

2. What problem was QLoRA trying to solve?
- Quantize the frozen pretrained weights to 4-bit while still fine-tuning effectively using LoRA.

3. Why can't LoRA fine-tune a 65B model on one GPU?
- The real bottleneck is:
    Frozen Base Weights
    +
    Activation Memory
    +
    KV Cache (sometimes)
    +
    Small LoRA parameters

4. Which memory components still dominate after LoRA?
- Base model weights
- Activation memory

5. What is the key insight behind QLoRA?
-The key insight is that the frozen base model does not need full-precision storage during fine-tuning.
By storing it in an efficient 4-bit representation while keeping computation in higher precision and training only
LoRA adapters, QLoRA drastically reduces memory without significantly sacrificing performance.

6. If the base model is stored in 4-bit integers, how can we still perform matrix multiplication accurately during the forward pass?

- QLoRA stores weights in 4-bit to save memory but computes with higher precision to preserve accuracy.

7. How QLoRA stores weights in 4-bit but computes in higher precision like FP-16/ FP-32 ?

- QLoRA stores the weights in blocks like
    - Block-1, Block-2, Block-3, Block-4 etc...
    - Before computing the inferences it dequantize these blocks and performs the computations in FP-16 not in 4-INT

8. A 7B model after quantization becomes just 3.5 GB but when you dequantize it again becomes 7GB only,
    so where QLoRA helps ?

    - Actually dequantization doesn't happen to all the block at once. Only the necessary blocks get dequantize
    and inferences gets calculated.

    Flow:
        Load Block 1 (INT4)

        ↓

        Dequantize Block 1 → BF16

        ↓

        Multiply

        ↓

        Discard temporary BF16 copy

        ↓

        Load Block 2

        ↓

        Repeat...

9. When does de-quantization happen?

- Dequantization happen during the inferences
- Dequantization happen during the training.
- So dequantization happens every forward pass, not just once.

10. How QLoRA actually works ?
- For every inference, it dequantize all the block one by one and accumulate the matrix multiplication and at
the end returns the final output.

- Think of QLoRA as streaming the model through the GPU a few blocks at a time, rather than
    inflating the entire model into memory before computation.
11.

"""
