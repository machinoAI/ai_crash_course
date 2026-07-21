"""
1. Why do different datatypes exist?
    - There are two fundamental issues:
        - Storing the numbers/weights precisely to get high precision.
        - Storing the weights for bigger model requires high memory and compute.

    - To solve these two problem, there are different datatypes exist:
    1. Floating point Representation:
        Computers store numbers as:

            (−1)^sign × mantissa × 2^exponent

        Three components:
            Sign bit → positive or negative.
            Exponent → scale/range.
            Mantissa → precision.

        Number = precision x scale
            Example: 12345 = 1.2345x10^4

            mantissa stores = 1.2345
            and exponent stores = 10^4


    1.1 FP32 ( 32 bit floating point)
        sign: 1 bit
        mantissa: 23 bit
        exponent : 8 bit   ->> total 32 bit


    - FP32 gives:
        - High precision
        - Large numerical range
        - Stable training

    Drawback: it requires
        7 B x 4 =  28 GB

    Training a larger model becomes expensive/impossible.

    1.2 FP16 ( 16 bit floating point)

        sign: 1 bit
        mantissa: 10 bit
        exponent : 5 bit   ->> total 16 bit

    Problem solved by FP16: It reduces
        - GPU memory by 50%
        - training time
        - communication cost

    Drawback: The exponent shrinks from 8 bits to 5 bits means:
        - Smaller numeric range
        - Tiny gradients may become zero ->> 0.0000001 ->> 0
        - Large value may overflow
        - that leads into unstable training

    1.3 BF16 (Brain Float 16)

        sign: 1 bit
        mantissa: 7 bit
        exponent : 8 bit   ->> Keeping exponent range same as FP32.
            ->> total 16 bit -

    BF16 gives:
        - Half memory of FP32
        - Nearly the same numerical ranges of FP32
        - Better stability than FP16
    Trade-off:
        Less precision but better stability

    This is why modern LLMs are usually trained in BF16.

    1.4 INT8: - It stores integer : -128 -> 127

        8 bits
        mantissa: No
        exponent : No

    We quantize and store the weights:
        original = 2.73
        stored = 27

    Quantized = weight/scale
    Recover = 27 x 0.1 = 2.7

    Why INT8:
         Because:
            - Memory usage drops by 75%
            - Inference becomes faster
            - Small GPUs can run bigger model
    Drawbacks:
        - Some precision is lost
        - Training directly in INT8 is difficult

    1.5 INT4/ NF4:
        - INT4 uses 4 bits
        - 7B model needs just = 7B x 0.5 = 3.5GB memory to load
    - Memory saved but there are several issues like
        - Accuracy loss
        - Harder optimization

    NF4 (Normal Float 4)
        - Weights in neural network is uniformaly distributed
        - Weights follow roughly a bell curve
        - INT4 wastes representation capacity.
        - NF4 (Normal Float 4) was designed specifically for this distribution.
        - It allocates more precision where most weights lie.

2. How do we decide which one to use?
    FP32 ->> 4 Bytes ->> High Precision ->> Huge Memory
    FP16 ->> 2 Bytes ->> Fast & Compact ->> Numerical Instability
    BF16 ->> 2 Bytes ->> Stable training ->> Lower precision
    INT8 ->> 1 Bytes ->> Cheap inference ->> Quantization Loss
    INT4 ->> 0.5 Bytes ->> Very Low memory ->> More accuracy loss


3. What is mixed precision training ?
    - Instead of using single datatype everywhere , we use different datatypes for different jobs
    - Example:
        Forward pass ->> BF16/FP16
        Backward pass ->> BF16/FP16
        Optimizer states ->> FP32
        Master weights ->> FP32

    - Typical setup to train the llm today:
        Model weights ->> BF16
        Activations ->>> BF16
        Gradients ->>> BF16
        Optimizers(adam) ->>> FP32
        Accumulations --->>> FP32

4. What is loss scaling ?
    - Multiplying large value with gradients to prevent becoming it zero , called loss scaling.
    Example:
            Gradient = 0.0000001
            Multiplying = 0.0000001* 10^6

Trade-offs: Use low precision where memory matters, and high precision where numerical stability matters.

"""