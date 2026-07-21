"""
1. Why was LoRA introduced ?
    - LoRA introduced because full fine-tuning became prohibitively expensive as models grows to billions of params.

    Existing problems in full fine-tune:
    - GPU Memory explosion
    - Storage explosion
    - Training cost

    Idea, here is to instead of training full 7 B weights LoRA train only few million.
    Hence:
        - Lower GPU Memory
        - Faster training
        - Smaller Checkpoints
        - Ability to maintain multiple task-specific versions

2. How LoRA decides which weights needs to modify/update ?
    - LoRA doesn't  decide which individual weights to update.  It learns a small set of new parameters that
     indirectly modify all the weights in the matrix.

     Example:
            During the full fine-tuning, every entry gets updated.

                W ∈ R^(4096×4096) = 16.7 million parameters ( it is counting of parameters)

            But LoRA freezes W and introduce two trainable matrices.
                A ∈ R^(r×4096)
                B ∈ R^(4096xr)

                BA = (4096xr + r×4096 ) where r =8,16,32,61,...

                and learns:
                    ΔW=BA = R^(4096xr)R^(r×4096)

                    r = 16
                    To count the parameters we add the power = (4096x 16) + (4096 x 16)
                        = 131,072  parameters

                So instead of updating the 16.7 Million of weights we are just updating 131K.

                But when we do actual matrix multiplication to compute BA we would have same dimension as actual model.

        While computing the inference model uses:
            W′=W+BA


    Intuition: LoRA behaves like light-weight correction layer that nudges the frozen model towards the new task
        without re-writing its original knowledge.

3. What is r (rank) in LoRA ?
    r is the rank of low rank decomposition.
        r = 4,8,16,32,64,...

    ΔW=BA
        where A = A^(dxr)
            B = A^(rxk)

        where r is the rank
            and r << d, k

            k = Input dimension
            d = output dimension

    - Rank r in LoRA controls the dimensionality of the low-rank update matrix ΔW=BA.
    - It determines the adaptation capacity of LoRA  and trades off model quality against memory and compute.
    - Rank r is the number of directions LoRA is allowed to move in to adapt the pretrained model.

Typical Values of r: Trades off:
    4 ->> Very small tasks -->> Less Memory
    8 ->> Classifications -->> Faster training
    16 ->> Default LoRA  -->> mediocre reasoning
    32 ->> Instruction Tuning -->> More memory
    64 ->> Complex Task  ->>>> Slower training
    128+ ->> Near Full Fine-Tuning  -->>>>  Larger adapters


4. What is LoRA ?
    - Low Rank Adaptations or LoRA is a parameter efficient fine-tuning technique in which :
        - The original weights are frozen
        - Only a very small sets of additional trainable matrices are learned.

        instead of learning W new

        LoRA learns:
            ΔW
        and computes
            W′=W+ΔW

    Where W is pretrained weight matrix.
        ΔW is Small task specific updates.


5. Why do we freeze the base model ?
    - Because the pretrained model already contains enormous amount of useful knowledge:
        - Grammar
        - Reasoning
        - World Knowledge
        - Code
        - Language structure

    - For most of the downstream task we don't want to destroy this knowledge.
    - Instead we only learn,
        ΔW
    Which gently steers the model
    There is also a systems reason, If the base model is frozen:
        - No gradients for base weights
        - No optimizer states for base weights
        - No update for base weights
    This dramatically reduces the memory cost.

6. Why does larger batch size needs more memory ?

    Q = XWq

    where x ∈ R^(B x S x H)
    B = batch size
    S = Sequence Length
    H = Hidden size

    Let's Say

    B = 2
    S = 2048
    H = 4096

    (B x S x H) = 2 x 2048 x 4096 = 16.7 Million

    Now increase your batch size B = 64

     (B x S x H) = 64 x 2048 x 4096 = 536.9 million values

    Weights has been increase by 32 times bigger, Now you need more memory to process and  more storage.

7. What are the hidden assumptions behind LoRA ?
    Researcher Observes that:
        " The difference between 'general English' and 'medical QA' often lies in low dimensional space."
8. Why should the update matrix be low-rank at all?

    - There is no theorem that guarantees that the update matrix must be low-rank. LoRA is based on an empirical observation from large models.
    Intuition-1:
        The base model already knows:
            - English
            - Grammar
            - Reasoning
            - Mathematics
            - Coding
        Now when we fine-tune it for
            - Medical QA
            - chat support
            - Legal documents

        Are we really changing 7B parameters, The answer is No;
        Existing knowledge is useful, we only need to steer the model in few directions.

    Intuition 2: High-dimensional data often lives in a low-dimensional space
        Example: Even though the parameter space is huge, useful task-specific changes may occupy only a small region of it.

    Intuition 3: Evidence from linear algebra
        - LoRA assumes that most of the energy of the update matrix is concentrated in a few singular directions.


9. How do we choose r?



10. Notes:
    - Hidden size (H): The dimensionality of the token representation inside the transformer.
    - Embedding dimension: Another name for hidden size in most transformer architectures.
    - Head dimension: Hidden size divided by the number of attention heads.
    - Batch size trade-off: Larger batches improve GPU utilization and training speed but require more memory and may reduce generalization.
    - Sequence length trade-off: Longer sequences capture more context but increase attention and activation memory.


"""