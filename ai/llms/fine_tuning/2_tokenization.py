"""
1. Why do we tokenize ?
- Because LLMs can not understand the raw text , so tokenization converts into numerical token Ids that the model
    can process. The tokenizer also ensures a consistent libraries.

2. What is BPE (Byte Pair Encoding)?
    - BPE builds a vocabulary by repeatedly merging the most frequent pairs of characters or subwords.
    - It reduces vocabulary size by repeatedly handling unknown words efficiently.
3. What is wordPiece ?
    - WordPiece is similar to BPE but selects merges based on likelihood rather than frequency. It is used in models like BERT.

4. What is SentencePiece?
    - SentencePiece treats text as a sequence of Unicode characters and tokenizes without requiring whitespace.
    - It is widely used in LLaMA, T5, and many multilingual models.
    - Example:
        I love machine learning.
        Tokenization:
            ▁I
            ▁love
            ▁machine
            ▁learn
            ing
            .
    - Notice the symbol "▁" , it means not a token but a white space.
    - hyperparameterization:
        ▁hyper
        parameter
        ization

    - There is only one word hence only first token has "_" not the intermediate one.

5. What are BOS, EOS, and PAD tokens?
    - BOS: Beginning of Sequence
    - EOS: End of Sequence
    - PAD: Fills shorter sequences so all inputs in a batch have the same length.
    - UNK = Unknown Token: It represents tokens which doesn't present in the vocabulary.

6. What are Special Tokens?
    - Special tokens have predefined meanings, such as BOS, EOS, PAD, UNK, or chat role tokens, and
        help the model understand the structure of the input.

7. What is Context Length?
    - Context length is the maximum number of tokens a model can process in a single input.
    - Inputs longer than this must be truncated or split.

8. What is padding ?
    - Padding adds PAD tokens to shorter sequences so that all sequences in a batch have equal length, enabling efficient parallel computation.

9. What is Dynamic Padding?
    - Dynamic padding pads sequences only to the longest example in the current batch rather than a fixed maximum length, reducing wasted computation and memory.

10. What is Sequence Packing?
    - Sequence packing combines multiple short training examples into one long sequence, maximizing context utilization and improving GPU efficiency during training.

11. What are Chat Role Tokens?
    - LLMs need to know who is speaking.
    - Instead of just feeding plain text:
        Hello

        Hi, how can I help?

    - we insert role tokens.
        <system>
            You are a helpful assistant.

            <user>
            Explain LoRA.

            <assistant>
            LoRA is...

12. What is Dynamic Padding?
    - Let's say your batch size is 4.
    - Suppose the token lengths are:
        | Sentence | Tokens |
        | -------- | -----: |
        | S1       |     15 |
        | S2       |     10 |
        | S3       |      7 |
        | S4       |     12 |

    Static Padding: Assume the maximum sequence length is 512.
        - Every sentence becomes 512 after padding.
        - Processing = 4x 512 2048
        - Even though only: 15 + 10 + 7 + 12 = 44 tokens contain useful information.
        - This wastes memory and compute.

    But in Dynamic padding:
        - The longest sequence of token is 15
        so we pad only 15. So after padding:
            | Sentence | Original | After Padding |
            | -------- | -------: | ------------: |
            | S1       |       15 |            15 |
            | S2       |       10 |            15 |
            | S3       |        7 |            15 |
            | S4       |       12 |            15 |

    So now we process only: 15 × 4 = 60 tokens

13. What is Truncation?
    - Truncation removes tokens that exceed the model's maximum context length. It ensures the input fits within the model's limits.

"""