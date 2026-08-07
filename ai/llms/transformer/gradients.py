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
m

"""