"""
1. Why is data more important than the model?
- A high-quality dataset has a bigger impact on model performance than changing the model architecture. Poor-quality or noisy data leads to poor fine-tuning regardless of the model.

2. What types of datasets exist for LLM fine-tuning?
- Common datasets include:
    - Pre-training data,
    - Supervised Fine-Tuning (SFT) data,
    - Preference data (DPO/RLHF), and
    - Evaluation datasets

    Each serves a different stage of the LLM lifecycle.

3. What is Instruction Tuning?
    - Instruction tuning trains the model to follow natural language instructions using instruction-response pairs.
    - It improves the model's ability to follow user requests.
    Example:
            Instruction:
                Summarize this article.

            Response:
            ...
4.  What is Completion Tuning?
    - Completion tuning trains the model to predict the continuation of a given prompt. It is commonly used for language modeling or domain adaptation.
    - Prompt:
        The capital of France is

        Completion:
        Paris.

5. What is the Prompt–Response format?
    - Each training example consists of a user prompt (input) and the expected assistant response (output). This is the most common format for instruction tuning.

6. What is a Chat Template?
    - A chat template converts structured conversations (system, user, assistant) into the token sequence expected
        by a specific model. Different models (Llama, Mistral, Qwen, etc.) use different templates.

7. What is JSONL format?
    - JSONL (JSON Lines) stores one JSON object per line, making it efficient for large-scale streaming and processing.
    - It is the standard format for many LLM datasets.
    - Examples:
        {"instruction":"Explain LoRA","output":"LoRA is..."}
        {"instruction":"What is QLoRA?","output":"QLoRA is..."}

8. What is the Alpaca dataset format?
    - Alpaca uses three fields: instruction, input, and output. It is one of the most widely used formats for supervised instruction tuning.
    - Example:
            {
              "instruction": "Translate to French",
              "input": "Hello",
              "output": "Bonjour"
            }

9. What is the ShareGPT format?
    - ShareGPT stores complete multi-turn conversations with alternating user and assistant messages.
    - It is commonly used for training conversational chatbots.
    - Example:
            [
              {"role":"user","content":"Hi"},
              {"role":"assistant","content":"Hello!"}
            ]


10. What is the OpenAI Messages format?
    - The OpenAI format represents conversations as ordered messages with roles such as system, user, and assistant.
    - It is widely used for chat-based fine-tuning and API interactions.
    - Example:
            [
              {"role":"system","content":"You are a helpful assistant."},
              {"role":"user","content":"Explain LoRA."},
              {"role":"assistant","content":"LoRA is..."}
            ]

11. How much data is enough for fine-tuning?
    - The required data depends on the task complexity and quality.
    - High-quality, diverse examples are generally more valuable than simply having a larger dataset.

    Typical guidance:
        - Small task: 1k–10k examples
        - Domain adaptation: 10k–100k examples
        - Large instruction tuning: 100k+ examples

12. How do you prepare a dataset before fine-tuning?
    - Clean the data, remove duplicates, normalize formatting, validate labels, apply the correct chat template,
     tokenize, split into train/validation sets, and perform quality checks before training.


"""