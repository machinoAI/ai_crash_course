"""
1. What are different types of chunking ?

- | Chunking strategy     | How it works                                               | When to use                                     |
| --------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| Fixed-size        | Split every N tokens/characters                            | Simple baseline                                 |
| Recursive         | Split using hierarchy: paragraph → sentence → word         | General-purpose RAG; very common                |
| Sentence-based    | Split on sentence boundaries                               | Q&A where preserving complete sentences matters |
| Semantic chunking | Group sentences with similar meaning                       | Documents with variable topic boundaries        |
| Structure-based   | Split using headings, sections, HTML/Markdown, code blocks | Documentation, PDFs, code, manuals              |


"""