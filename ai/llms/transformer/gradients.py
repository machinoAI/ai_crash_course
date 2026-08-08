"""
1. What exactly is a Gradient?
    - A gradient is the derivative of the loss with respect to a parameter. It measures how much the loss changes if that parameter changes slightly.
    - Gradient = Direction to increase the loss.


        Gradient=   ∂Loss / ∂Weight

    - Every trainable parameter has a gradient.
        - Embedding.weight.grad
        - WQ.grad
        - WK.grad
        - WV.grad
        - MLP.grad
        - LMHead.grad

2. What is Scalar vs Vector Gradient ?

    - The gradient tensor always has the same shape as the parameter tensor.
    - Gradient shape = Weight shape
    - A 7B model has ->> 7 billion parameters. ->> Backprop computes ->> 7 billion gradients.


3. Why are Gradients Accumulated?
    - PyTorch adds gradients by default. It doesn't overwrite them.
    - Gradients accumulate until you clear them.

4. How does loss.backward() compute gradients?
    - Autograd stores the computation graph during the forward pass and traverses it in reverse,
        applying the chain rule to compute gradients for every trainable parameter.

    - Autograd walks the computation graph backward.


5. What is vanishing gradients ?
    - Gradients becomes extremely small , Learning almost stops.
    Causes:
        - Sigmoid
        -   Deep networks
        - Poor initialization

    Solutions:
        - Residual Connections
        - LayerNorm
        - ReLU / GeLU
        - Better initialization

    Tiny gradients → Tiny updates → No learning.


6. What is Gradient Clipping ?

    - Gradient Clipping limits the maximum gradient magnitude before the optimizer updates the weights,
        preventing unstable parameter updates.

    - Clip gradients, not weights.

7. What is Gradient Accumulation ?
    - Gradient Accumulation computes gradients over multiple mini-batches and delays the
        optimizer update until all accumulated gradients have been collected,
         allowing a larger effective batch size without increasing GPU memory.


8. What is Effective Batch Size?

    - Effective Batch Size is the total number of training samples that contribute to one weight update.

    - Effective Batch Size = Micro Batch Size × Accumulation Steps
                            = 16 x 4 = 64


9. What is micro batches ?
    - A Micro-Batch is the portion of data processed in one forward and backward pass due to GPU memory limitations.

    - Micro-Batch = Actual batch that fits into GPU memory.

10. How Gradient Accumulation Works ?

    - Without accumulation:
        Batch 16 -> Forward Pass -> Backward Pass -> AdamW update

        - Every batch updates the weights.

    - With Accumulation:
        Micro Batch 1
              ↓
        Forward
              ↓
        Backward
              ↓
        Store Gradient

        Micro Batch 2
              ↓
        Forward
              ↓
        Backward
              ↓
        Add Gradient

        Micro Batch 3
              ↓
        Forward
              ↓
        Backward
              ↓
        Add Gradient

        Micro Batch 4
              ↓
        Forward
              ↓
        Backward
              ↓
        Add Gradient

        ↓
----------------------------------Weights update after last accumulation.
        AdamW Update (Once)


    - Weights remain unchanged until the last accumulation step.
    - Only the gradients accumulate.

11. When to use gradients accumulation ?

    - GPU memory is insufficient for the desired batch size.
    - You want the optimization behavior of a larger batch.
    - Training large models (LLMs, diffusion models, ViTs).

12.



"""