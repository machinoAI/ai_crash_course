"""
1. How much memory do you need to fit a llm model ?

    Memory(GB) = (Parameters * Bytes per parameter)/10^9

    Where Parameters (p) = Model weights
        1 Bytes = 8 Bits

    Memory (GB) = (Parameters * Bits per parameter) / 8*10^9

    Example: To fit a 7B Qwen model of FP16 = 2 Bytes
        Memory (GB)  = 7 * 2= 14 GB

        FP32 ---> 4 Bytes
        FP16 ---> 2 Bytes
        BF16 ---> 2 Bytes
        INT8 ----> 1 Bytes
        INT4 ---->  0.5 Bytes

2. Is this memory is sufficient for training/ fine-tuning LLM Model
    - No; It is the minimum memory required to load the model to compute the inferences.
    - In reality , it required much more to even compute the inferences.
    - The following components needs a memory to load in the system

3. What occupy GPU Memory ?
    1. Inference Memory:
        - Weights
        + Activations
        + KV Cache
        + CUDA Overhead

    2. Training Memory:
        - Weights
        + Activations
        + Overhead
        + Gradients
        + Optimizers
        + KV cache (sometimes)

4. What are assumptions while estimating the memory?
    - When someone says:
        " Llama 7B fits in 14 GB"
    - They are making several hidden assumptions.
        1. Only weights are counted : Memory = wights
            - Reality:
                - Weights
                + Activations
                + KV cache
                + Overhead

            - Actual usage is higher.
        2. The formula assumes inference . Training requires much more memory
        3. No optimizers:
            - Adam stores:
                - Parameters
                - Gradients
                - First Moment(m)
                - Seconds Moment(v)
        4. No KV cache:
            - Long conversation increase KV cache.
            - For chat applications, KV cache can consume several GB.

5. Why training needs much more memory ?
    - Suppose we train a 7B model in FP16.
        - Weights
            --> 7Bx2 = 14 GB
        - Gradients: Need one copy
            ---> 14 GB
        - Adam first moment:
            ---> 14 GB
        - Adam seconds Moment:
            ----> 14 GB

        Total : 56 GB

        And we still have not included :
            - Activations
            - Temporary tensors
            - CUDA Buffers

    - This is why training a 7B model often required 80- 100GB GPUs.

6. What is the biggest hidden cost among the components to load the model?
    - Activation Memory:
    - Activation depend on:
        - batch size (B)
        - sequence length (S)
        - hidden dimension (H)
        - number of layers (L)

    - Rough Intuition:
        Activation Memory ∝ B × S × H × L

    - Doubling sequence Length from 2048 to 4096
        - Does not just double memory also Attention complexity becomes O(S^2)
        - So memory can increase dramatically.

    Note: - wights stays fixed:

"""