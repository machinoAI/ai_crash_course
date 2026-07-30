"""
1. How do you choose the LoRA rank (r)?
    - Choose r based on the task complexity and available GPU memory.
    - Lower r (8–16) is sufficient for most tasks; higher r (32–64) improves capacity but increases memory and
        trainable parameters.

2. Which transformer layers should receive LoRA adapters (Q, K, V, O, FFN)?
    - Most implementations apply LoRA to the attention projection layers (q_proj and v_proj), while larger
        adaptations may also include k_proj, o_proj, and FFN layers.
    - More target modules improve adaptation but require more memory and training time.

3. What are common QLoRA training failures and how do you debug them?
    - Common issues include:-
        - loss not decreasing,
        - unstable training,
        - overfitting, and
        - OOM errors.

    - Debug by checking
        - data quality,
        - learning rate,
        - LoRA rank,
        - target modules,
        - batch size, and
        - GPU memory usage.

4. How is QLoRA implemented using Hugging Face PEFT and bitsandbytes?
    - bitsandbytes loads the base model in 4-bit NF4, while PEFT attaches and trains the LoRA adapters.
    - The base model remains frozen, and only the LoRA parameters are updated.

5. Production serving—adapter merging vs dynamic adapter loading.
    - Adapter merging permanently combines LoRA weights with the base model for faster inference.
    - Dynamic adapter loading keeps the base model unchanged and loads different adapters on demand for multiple tasks or customers.

6. Can you estimate the GPU memory required to fine-tune a 7B model using QLoRA?

    | Component        | Memory      |
    | ---------------- | ----------- |
    | Base Model (NF4) | **3.5 GB**  |
    | LoRA Adapters    | **~21 MB**  |
    | Gradients        | **~21 MB**  |
    | Adam Optimizer   | **~84 MB**  |
    | Activations      | **6–10 GB** |
    | CUDA Workspace   | **1–2 GB**  |

Total around 11- 16GB.

7. What is PEFT?
    - PEFT (Parameter-Efficient Fine-Tuning) is the Hugging Face library that implements methods like LoRA, QLoRA, Prefix Tuning, and Prompt Tuning while training only a small subset of parameters.
    - PEFT injects LoRA adapter layers into the specified transformer modules and freezes all original model weights.
    - When you call get_peft_model():-  It wraps the base model, inserts LoRA adapters into the target modules, freezes the base model, and marks only the LoRA parameters as trainable.
    - Only the LoRA adapter weights and configuration are saved—not the full base model.
    - The adapters are very small (often only a few MB to hundreds of MB), making them easy to store, share, and load with the original base model.


8. Hugging Face Training Stack:
    Transformers → Model, bitsandbytes → Quantization, PEFT → LoRA, TRL → Training, Accelerate → Multi-GPU, DeepSpeed → Scale.

9. End-to-End QLoRA Code Pipeline:

    Load Pretrained Model
        ↓
    Quantize using bitsandbytes (NF4)
            ↓
    Attach LoRA adapters (PEFT)
            ↓
    Load & Tokenize Dataset
            ↓
    Train (TRL/HF Trainer)
            ↓
    Save LoRA Adapter
            ↓
    Load Adapter for Inference

10. Common Production Mistakes:
    - Forgetting to freeze the base model.
    - Wrong target modules.
    - LoRA rank too high/low.
    - Learning rate too high.
    - Saving the full model instead of the adapter.
    - Loading an adapter with the wrong base model.
"""