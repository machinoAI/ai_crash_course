"""
1. How does QLoRA decide how many quantized blocks to dequantize simultaneously?
    - QLoRA itself doesn't make that decision.
    - The execution strategy is determined by the underlying CUDA kernels and GPU architecture.
    - The kernels tile the matrix into blocks and schedule them across Streaming Multiprocessors based on hardware
        resources such as shared memory, registers, Tensor Cores, and occupancy.
    - Multiple blocks are processed in parallel to maximise throughput while keeping temporary dequantized buffers small.

2. What is quantization ?
-  Quantization is the process of representing model weights into smaller bits , reducing memory usage and
    often improving inference efficiency with minimal loss in accuracy.

3. How do you convert an FP32 weight into INT4?
    - FP32 values are mapped to one of 16 discrete INT4 values using a quantization scale
    - During computation, these INT4 values are dequantized back to approximate floating-point values.

4. Why isn't normal INT4 enough?
    - Normal INT4 uses uniformly spaced values.
    - LLM weights are not uniformly distributed—they are approximately normally distributed.
    - Uniform quantization wastes precision where most weights lie.
    - NF4 allocates its 16 values according to the weight distribution, reducing quantization error.

5. What are the 16 discrete values?
- Since INT4 uses 4 bits, it can represent only 2^4 =16 distinct quantization levels.
- Every floating-point weight is mapped to the nearest one of these levels.

6. What is NF4?
- NF4 (NormalFloat4) is a 4-bit quantization scheme designed for neural network weights.
- Instead of using uniformly spaced values like standard INT4, it uses non-uniform quantization levels that
 match the approximately normal distribution of LLM weights, reducing quantization error.

 Example:
        INT4 = 2^4 = 16 discrete values = uniformly distributed
        NF4 = Normally distributed similar to actual model weights = bell shape curve.

    Quantization error:
        Original FP32 weight=  0.046
        Nearest INT4 representable value = 0.10
        Quantization Error = |0.046 - 0.10|
                   = 0.054
    - The error comes from approximating the original floating-point value with the nearest representable quantized value.

7. What is double quantization ?
- Double Quantization reduces memory further by quantizing the quantization scales themselves.
    Instead of storing scale values in full precision, QLoRA stores them in a lower precision format,
    reducing overhead while maintaining accuracy.

    let's say FP-32 has value = 0.74
    INT4 storing 7
    so scale is 0.1

    While dequantization = 7x0.1 = 0.7 and 0.04 is quantization error

    So,
        After the quantization:
            Weights      → 4 GB
            Scale Values → 400 MB

        or
            FP32 Weights
              │
                  ▼
            INT4 Weights
            +
            FP32 Scales

    After double quantization:
        FP32 Weights
              │
              ▼
        INT4 Weights
        +
        INT8 Scales  -->>> Even scale is getting quantized in lower precisions.

8. What is a Paged Optimizer?
- A Paged Optimizer stores optimizer states in CPU memory when GPU memory is under pressure and transfers
    them back only when needed. This prevents temporary GPU memory spikes from causing out-of-memory errors during QLoRA training.


9. What happens in one forward and backward pass during QLoRA training?





"""