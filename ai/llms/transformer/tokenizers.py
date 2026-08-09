"""
1. What is tokenizers ?

    - A tokenizer converts raw text into a sequence of discrete tokens that the model can map to integer IDs
        and then embeddings. This process is called tokenization.

    Example: "Curiosity killed the cat" -->> [12543, 8271, 279, 841]


2. How do you design/train a tokenizer?

    Large text corpus
      ↓
    Normalize text
          ↓
    Choose tokenization algorithm
          ↓
    Learn vocabulary
          ↓
    Tokenizer
          ↓
    Text → tokens → IDs


3. What are the main approaches of tokenization?

    1. Word Level
    2. Character Level
    3. BPE- Byte pair encoding
    4. WordPiece
    5. Unigram

    Details about above are there in fine_tuning section

4. What happens with Out-of-Vocabulary ?
    - Word tokenizer , it may produce

        "Forgagilationer" -> [UNK]

    - Modern sub-word tokenizers
        - Usually don't need [UNK] for ordinary unseen words.
            Example:
                    "unhappiness"  ->> "un" + "happiness"


    - Modern LLM tokenizers solve OOV primarily by decomposing unseen words into
        smaller subword/byte units rather than requiring an [UNK] token.







"""