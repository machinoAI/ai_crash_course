"""
1. What is stochastic gradient descent (SGD) ?

    - Stochastic Gradient Descent (SGD) is an optimization algorithm used to update model weights by moving them in the direction that minimizes the loss.
    - The word "stochastic" means the training data is randomly shuffled,
        and updates are computed using one sample or, more commonly today, a small mini-batch.


    - Types of Gradient Descent:
        1. Batch Gradient Descent : Uses the entire dataset to compute one gradient update.

            Uses the entire dataset
                W_t+1 = W_t - (1/N) x η x ∑ ∇L_i

        where i varies from 1 to N and N is entire datasets.


        2. Stochastic Gradient Descent: Uses one training example to compute one gradient update.

            Uses one sample:
                Uses the entire dataset
                    W_t+1 = W_t - η x ∇L_i

        Where i = one randomly selected training example

        3. Mini-batch Gradient descent: Uses a small batch (e.g., 32, 64, 128 samples) to compute one gradient update.

            Uses B samples:

                W_t+1 = W_t - (1/B) x η x ∑ ∇L_i

        where i varies from 1 to B and B is mini batch 32,64,128,...

        - This is what GPT, Llama, BERT, etc., actually use.



    Notes: There are decent difference in SGD and SGB.

2. Why SGD is not enough?

    - SGD updates weights using only the current mini-batch gradient.
    - It has no memory of previous updates and uses the same learning rate for every parameter.

    Bottlenecks:
        1. No  memory ( Solution: Momentum)
        2. Same Learning Rate for Every Weight
            Example:
                    W1 needs tiny updates
                    w2 needs large updates

                    But learning rate is same = 0.001  Treat everything equally.

            Solution:
                AdaGrad / RMSProp / Adam.

        3. Sensitive to Learning Rate
            - If the learning rate is too large: It overshoots and may never converge.
            - If it's too small:Training becomes painfully slow.


3. What is Momentum ?
    - Momentum is an optimizer that uses both the current gradient and the accumulated history of previous
     gradients to update the weights, resulting in faster and smoother convergence.

    Intuition:
        - Think of rolling a heavy ball downhill.
        - A heavy ball doesn't instantly change direction when it hits a small bump.
            It keeps moving because of its momentum.

        - Similarly, Momentum remembers the previous update direction and doesn't overreact to noisy gradients.

    -Momentum = SGD + Memory of previous gradients.

4. What is AdaGrad  ?

    - AdaGrad (Adaptive Gradient) is an optimizer that assigns a separate learning rate to each parameter based on its historical gradients.

    - AdaGrad = Adaptive learning rate for every parameter, but the learning rate keeps shrinking over time.

    - Formula:  G_t = G_t−1 + g_t^2

5. What is RMSProp ?

    - RMSProp is an optimizer that uses an exponentially weighted moving average of squared gradients
        to assign an adaptive learning rate to each parameter.

    - Instead of remembering all gradients forever, RMSProp remembers only recent gradients.
    - Old gradients gradually fade away.


    Moving average of squared gradients:
        v_t = βv_t-1 + (1−β) g_t^2

    Weight update:
        W_t+1 = W_t - η/ sqrt(v_t + ϵ) g_t

    Where:
        g_t = current gradient
        v_t = moving average of squared gradients
        β ≈ 0.9
        ϵ = small constant

    Advantages:
        - Different learning rate for every parameter.
        - Learning rate doesn't shrink to zero.
        - Faster and more stable than AdaGrad.

    Limitation
    - RMSProp still has no momentum.


    - RMSProp = AdaGrad + Forget old gradients.

6. What is Adam (Adaptive Moment Estimation) ?

    - Adam is an optimizer that combines Momentum (first moment) and
        RMSProp (second moment) to provide fast, stable, and adaptive weight updates.


    - First Moment (m) → Moving average of gradients → Momentum
    - Second Moment (v) → Moving average of squared gradients → Adaptive learning rate

    Adam = Momentum + RMSProp

7. What is AdamW ?

    - AdamW is Adam with decoupled weight decay. It separates optimization from regularization, leading to better generalization and more stable training.

"""