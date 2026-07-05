"""
Optimisers: Algorithms that update the weights of the neural network during training to minimize the loss function.
    - After forward pass we compute a loss (how wrong the model was):
        loss = compute_loss(prediction, target)

    - Then backpropagation compute the gradient
        gradients = backpropagation(loss)    # The direction and magnitude of the loss's sensitivity to each weight

    - The optimizer decides how to actually change the weights using that gradient.
       new_weights = optimizer.update(old_weights, gradients)

        or

        w = w - learning_rate * gradient

Examples:
    - Adam: Combines momentum + per-parameter adaptive learning rates
    - AdamW : Adam but with weight decay decoupled from the gradient update.
    - RMSProp : Adapts learning rate using a moving average of squared gradients, per parameter
    - Adagrad : Accumulates all past squared gradients to shrink the learning rate for frequently-updated params
"""