"""
1. Epoch: One complete pass of the entire dataset through the model

 2. Batch: A subset of training data processed together
    The training data split into smaller groups called batches.
    The model processed one batch a time

3. Batch size: Number of training data into one batch.

Example: Lets training sample is 10. batchsize = 2
 So # of batches = 10/2 = 5 batch will get created , with 2 samples each.

 4. Iteration: Processing one batch of data through the model...to process 5 batches it will take 5 iteration.

 5. Activation functions: Activation functions are mathematical functions applied to the output of neurons.
    They introduce non-linearity, allowing neural networks to learn complex patterns.
    They can be used in hidden layers as well as the output layer.
    Only certain activation functions, such as Softmax and Sigmoid, produce probability-like outputs.

Examples:
• ReLU (Rectified Linear Unit): f(x) = max(0, x)
    - Outputs 0 for negative values and x for positive values.
    - Introduces non-linearity and helps mitigate the vanishing gradient problem.
    - Most commonly used activation function in hidden layers.

• Leaky ReLU: f(x) = max(αx, x), where α ≈ 0.01
    - Instead of outputting 0 for negative inputs, it outputs a small negative value (e.g., 0.01x).
    - Helps solve the dying ReLU (dying neuron) problem.

• Softmax:
    - Converts the output logits into a probability distribution.
    - Output values lie between 0 and 1, and all probabilities sum to 1.
    - Used for multi-class classification.

• Sigmoid: f(x) = 1 / (1 + e^(-x))
    - Converts the output to a value between 0 and 1.
    - Interpreted as the probability of the positive class.
    - Used for binary classification.

• Tanh (Hyperbolic Tangent): tanh(x)
    - Outputs values between -1 and 1.
    - Zero-centered, making optimization easier than Sigmoid in some cases.
    - Used in hidden layers, especially in older neural networks and RNNs.

"""