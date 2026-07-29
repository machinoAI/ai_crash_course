"""
1. How does QLoRA decide how many quantized blocks to dequantize simultaneously?
    - QLoRA itself doesn't make that decision.
    - The execution strategy is determined by the underlying CUDA kernels and GPU architecture.
    - The kernels tile the matrix into blocks and schedule them across Streaming Multiprocessors based on hardware
        resources such as shared memory, registers, Tensor Cores, and occupancy.
    - Multiple blocks are processed in parallel to maximise throughput while keeping temporary dequantized buffers small.

2. 

"""