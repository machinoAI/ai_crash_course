"""
1. Where exactly do we apply LoRA in transformers?
    - LoRA can be applied to any layer
    - But in practice , it usually injected into the attention projections
    Inside self-attention:
        Q = XWq
        K = XWk
        V = XWv

    O = Attention(Q,K,V)Wo

    The corresponding weights matrices are:
        Wq, Wk, Wv, Wo

    LoRA modifies them as:

         WQ' = WQ' + BQAQ
          Wv' = Wv' + BvAv
    - Most commonly
        - Query projections:  WQ'
        - Value Projections :  Wv'

    Sometimes:
        Key projection (Wk)
        Output projection( Wo)
        Feed-forward layers (W1, W2)

2. Why mostly Q and V?
    - Query matrix controls: What information should this token pay attention to?
        - Changing Q changes the attention pattern.

            QK^T

        which changes:
        - which tokens attend to each other,
        - how much attention they pay,
        - the reasoning path.

    - Value matrix controls: What information gets passed forward?
        - Changing V changes the content being propagated.

    - Researchers found that modifying Q and V gives most of the performance improvement while keeping parameter
        count low.

3. Can LoRA be applied to FFN layers?
    - Yes; This increases the capacity but also increases the memory and cost.

4. How much memory does LoRA save compared to full fine-tuning?
    - Full fine-tuning needs memory for
        - Weights -->> 2 Bytes
        - Gradients ->> 2 Bytes
        - Adam first moment ->> 4 Bytes
        - Adam 2nd moment ->> 4 Bytes

        Total : 12 Bytes

        Now let's say
        Batch size = 2
        Sequence Length =  2048
        and Hidden size = 4096

        then Q = XWq
        where X = R^(2x 2048 x 4096) = 16.7 M

        Total memory = 12 x 16.7 = 200 MB

    Now in LoRA:
        Let's say r =16

            Q = XWq + BA

            where B = R^(k x r)
             A = R^(d x r)

            BA = R^(d x r)+(r x k) = 4096 x 16 + 16 x 4096 = 131,072


        Total memory = 131,072 x 12  = 1.57 MB

    so total memory saved = 200/1.57 = 125X

    Note: Above calculation is just for first layer.


5. Does LoRA reduce all GPU memory?

    - NO; It only reduces weights for
        - gradients
        - Optimizers
        - Checkpoints

    - It does not reduce memory for
        - Base Model weights
        - Activations
        - KV cache
        - CUDA Overhead

    The frozen model still has to sit in the memory.



Notes: Memory consumptions in practical.
        - Full Fine-tuning : 60-80 GB
        - LoRA : 16-24 GB
        - QLoRA: 8-12 GB

6. What is the LoRA scaling factor α, and why do we need it?
    In practice, LoRA actually uses:
        W′=W+ α/rxBA

    where:
    r = LoRA rank.
    α = scaling factor (a hyperparameter).


7. Why do we need α?

    Suppose you increase the rank:
        r=8→64.

    Now, A and B contain many more parameters. Without any scaling, the update
        ΔW=BA

    could become too large and destabilize training.
    The factor = α/r

    controls the strength of the LoRA update.


    Think of LoRA as adding a "correction" to the pretrained model:

        Output = Pretrained knowledge + LoRA correction.

        The scaling factor decides:
         - How loudly the correction speaks.
        - How much the adapter can influence the base model.
        - Whether the adapter dominates or gently nudges the model.

    Notes: often people use α=2r.

8. Why divide by r?
    - As r increases, the update matrix can represent more directions.
    - To keep the magnitude of the update roughly comparable across different ranks, LoRA normalizes by r:

9. What happens if α is too small?
    - LoRA updates become weak.
    - The model adapts slowly.
    - It may underfit.

10. What happens if α is too large?
    - The adapter dominates the pretrained model.
    - Training can become unstable.
    - Overfitting becomes more likely.

"""