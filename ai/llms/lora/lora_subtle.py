"""
1. How does the forward pass work in LoRA ?
    - During the forwards pass, LoRA keeps the pretrained weights frozen and computes the output as y = xW + α/r(xA)B.
    The first path uses the original model,  while the second path computes the low rank correction through the adapter matrices.
    Their outputs are added together, allowing task specific adaptation without modifying the pretrained weights.

2. How does backpropagation work when the base model is frozen?
    During backpropagation, gradients flow through the entire computation graph, including the frozen base model.
    However, the base weights have requires_grad=False, so gradients are not stored for them and the optimizer does not update
    them. Only the LoRA matrices A and B receive parameter updates,
    which greatly reduces memory usage while preserving the pretrained model's knowledge.

3. What is autograd ?
    Autograd is the automatic differentiation engine that computes the gradients required for backpropagation.

4. How are LoRA adapters merged into the base model after training?
    After LoRA training, the adapter matrices A and B can either remain separate or be merged into the base weights.
    Merging computes

    W =W+ α/r(BA)

    producing a standard weight matrix for inference.
    Keeping adapters separate allows multiple task-specific adapters to share the same base model,
    while merging simplifies deployment and slightly reduces inference overhead.

5. Can multiple LoRA adapters be attached to the same base model?
    Yes;

    Base Model (16GB) + 100 MB (coding) + 100 MB (Medical) + 100 MB (finance)

6. Can multiple adapters be loaded at the same time?
    Yes; LoRA separates general knowledge (base model) from task-specific knowledge (adapter),
    allowing one model to support many domains efficiently.

    There are three common approaches.
        - Switch between adapters (most common)
        - Stack adapters: Sometimes multiple adapters are applied sequentially.
        - Combine adapters (70% Medical + 30 % Legal)

7. If I have 100 LoRA adapters, do I need 100 copies of the base model?
    - No. All adapters share the same frozen base model. Only the lightweight adapter weights differ.

8. What is Adapter Fusion / Multi-LoRA?
- Suppose you have three LoRA adapters:
    - Medical LoRA
    - Legal LoRA
    - Coding LoRA
User asks - :
    "Write Python code to analyse medical records."

    Which adapter should you load?

option1: Multi-LoRA ->> Serve multiple adapters together
        Instead of loading just one adapter we load two adapters:

            base Model + Medical LoRA + Coding LoRA

        Both adapters contribute to the output.

option 2: Weighted Adapter Fusion: Sometimes one domain should have more influence.
    Instead of simply adding them:
        W′= W + 0.7ΔW1 + 0.3ΔW2

    Example:
        70% Medical
        30% Finance

9. Do adapters always work well together?
    No:

    Medical adapters Learns: Apple → health benefits
    Finance adapters learns: Apple → company

    How do frameworks handle this?

    Modern systems may use:
        - Weighted combinations.
        - Dynamic routing (choose adapters based on the prompt).
        - Mixture-of-Experts style routing.
        - Selective activation of adapters.

    The goal is to reduce interference while still benefiting from multiple specialised adapters.

10. What are the limitations of LoRA?
    - Limited adaptation capacity
    - Choosing the right rank is difficult
    - Performance may still lag behind full fine-tuning
    - Multiple adapters can interfere
    - More adapters = more management
    - LoRA does not reduce activation memory: If your GPU bottleneck is activation memory (for example, long context windows), LoRA alone will not solve it.
    - LoRA is not ideal when the entire model must change


"""