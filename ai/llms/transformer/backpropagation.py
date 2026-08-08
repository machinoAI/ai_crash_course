"""
 1. What is backpropagation ?

    - Backpropagation is the algorithm that computes the gradient of the loss with respect to
        every trainable parameter by propagating the error backward through the network using the chain rule.

    - It does not update the weights; it only computes how each parameter contributed to the loss.
    - Optimizers update the weights.

    Mathematical View:
        Forward Pass:
            Input

            ↓

            Embedding

            ↓

            Transformer

            ↓

            LM Head

            ↓

            Logits

            ↓

            Softmax

            ↓

            Loss


        Backward Pass:
            Loss

            ↑

            Softmax

            ↑

            LM Head

            ↑

            Transformer

            ↑

            Embedding


2. What is actually backward propagated?
    - Gradients
    - A gradients tell us, If this weights changes slightly,
     How much the loss will change.


3. Why go backwards ?
    Few things to clear:
        - Backpropagation computes gradients.
        - The optimizer updates weights.

    Suppose our model is:
        Input
           │
        Embedding
           │
        Attention
           │
        MLP
           │
        LM Head
           │
        Logits
           │
        Loss

    The only place where we know whether the model was right or wrong is at the loss.

    Now we ask: Which parameter caused this loss?
    To answer that, we need: ∂Loss/∂LW


    for every weight.

    - Since the loss depends on the logits, the logits depend on the LM Head,
        the LM Head depends on the Transformer blocks, and the Transformer blocks depend on the embeddings,
        we must trace this dependency backwards.


    - The optimizer updates the weight as:

            W new = W old −η ∂W/∂Loss


    where:

    W = parameter
    η = learning rate
    ∂W/∂Loss = gradient computed by backpropagation

    Notice the minus sign. We move in the direction that reduces the loss.


    - We propagate the error backward because the loss is computed only at the output of the network.
    - To reduce that loss, we must determine how much each earlier parameter contributed to it.
    - Backpropagation applies the chain rule to compute the gradient of the loss with respect to every trainable parameter.
    - These gradients are then passed to the optimizer, which updates the weights in the direction that minimizes the loss.


4. What is Loss Scaling ?
    - Loss Scaling multiplies the loss by a large constant before backpropagation
        to prevent gradients from underflowing when training with FP16.

    - Loss Scaling exists only because of FP16.

5. What is Tensor Cores ?
    - Tensor Cores are specialized hardware units on NVIDIA GPUs that accelerate matrix multiplication
        and mixed-precision operations used in deep learning.

    - Tensor Cores accelerate matrix multiplication, not model accuracy.


"""