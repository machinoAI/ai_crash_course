"""
1. What is model's memory ?
    - Suppose you build the world's simplest neural network:
        - Input (3 features) → Hidden layer (2 neurons) → Output (1 neuron)
        - x = [age, salary, experience]
        - It starts with random numbers:
            Input → Hidden
            W1 =
                [ 0.2   -0.5 ]
                [ 1.1    0.3 ]
                [-0.7    0.9 ]
            Hidden → Output
            W2 =
                [0.4]
                [-0.8]
        - These random numbers are called weights (parameters).
        - The weights of the model is the model's memory.

        y = w1x1 + w2x2 + w3x3 + b

        The weights determine:
            - How important age is
            - How important salary is
            - How important experience is
        Example:
                Risk = 0.1xage + 5x Salary

        - Salary matters more.

        The model learns those important scores from the data.


2. What creates billions of weights in transformer ?
    In transformers, weights appear inside many matrix multiplications:
        Self Attention:
            Q = XWq
            K = XWk
            V = XWv

        Feed-Forward:
            H = ReLU(XW1)
            Y = HW2
    Each matrix contains millions of numbers.
    Example: hidden_size = 4096
        Wq ∈ R^(4096×4096)
        Number of weights: = 4096×4096 ≈ 16.7 million

    And this is just one matrix in one layer.
    Forty layers later:
        7 billion weights

3. Why do weights remains constant during inference ?
- Training Steps:
    Forward Pass ->> Loss ->> Backward Pass ->> Gradients ->> Update weights
- Inference Steps: We don't update weights hence weights are frozen here.
    Forward Pass only .

4. Where do gradients come from ?
    - Forward Pass:
        y^=f(x,W)

    - Loss:
        L(y^,y)

    - Backward: This derivative is the gradient.
        ∂L/∂W

    It answers: If I change this weight slightly, how much will the loss change?

    GPU memory must store:  One gradient per weight
    Thus,
    7B weights → 7B gradients

5. What are optimizer moments? Why not 3rd moment ?

    1. First moment(mt): First moment is the exponentially weighted moving average of past gradients.
     It captures the direction and momentum of parameter updates, making optimization smoother and less noisy.

    2. Second moment (vt): Second moment is the exponentially weighted moving average of squared gradients.
     It captures the magnitude/variance of updates and helps adapt the learning rate for each parameter.

    3. Why not third moment?:
    The third moment measures skewness (asymmetry) of the gradient distribution, which usually provides
     little benefit for optimization while increasing memory and computation overhead.

6. Why does Adam require 3× or 4× memory?
    For every parameter adam stores the following: For FP16
        - Weights ->> 2 Bytes
        - Gradients ->> 2 Bytes
        - Momentum first ->> 4 Bytes
        - Momentum 2nd ->> 4 Bytes
    - Total 12 Bytes =  7B x 12 = 84B
7. What is CUDA overhead?
    CUDA overhead is the extra GPU memory consumed by internal buffers, temporary tensors, kernel workspaces,
     memory caching, and communication primitives used by libraries like CUDA, cuBLAS, and cuDNN.




"""