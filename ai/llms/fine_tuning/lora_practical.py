"""
1. LoRA Hyperparameters:
    - Rank (r) : controls the Capacity of the adapter.
    - Alpha (α): Controls How much the LoRA update influences the frozen model.
    - LoRA Dropout: Not normal neural network dropout.It is applied only to the LoRA path.
        - Reduce overfitting.
    - Target Modules:
        - Instead of every linear layer Choose only:
            - q_proj
            - v_proj
        or
            - q_proj
            - k_proj
            - v_proj
            - o_proj
    - Learning Rate

2. Debugging LoRA:
    - Problem 1: Loss not decreasing
        - Learning rate is too low
        - Rank too small
        - Wrong target modules
        - Dataset poor

    - Problem 2: Validation worse than training
        - Overfitting
        Solutions:
            - Increase dropout
            - Early stopping
            - More data
            - Reduce rank

    Problem 3: Model almost identical to base model.
        Reasons:
            - Alpha too low
            - Rank too low
            - Not enough epochs

    Problem 4: Training unstable
        - Solutions:
            - Lower Learning Rate
            - Lower alpha
            - Gradient clipping

3. LoRA variants:
    - AdaLora:
        problem : Fixed Rank
        Idea: Automatically allocate rank where needed.

    - DoRA:
        problem:
        LoRA only updates direction.
        Idea:
            - Also update weight magnitude.
            - Often improves accuracy.

    - IA^3: Instead of learning matrices,
        - Learns scaling vectors.
        - Even fewer parameters.

    - LoHa
        - Uses Hadamard products.
        - Higher expressive power.

    - LoKr
        - Uses Kronecker decomposition.
        - Compresses updates differently.


"""