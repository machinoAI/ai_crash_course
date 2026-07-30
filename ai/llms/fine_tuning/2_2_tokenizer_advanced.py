"""
1. How do we choose tokenizer ?
    - You almost always use the tokenizer that was trained with the model.

2.  What does BPE do internally?
        Dataset
        ↓
        Split every word into characters
            ↓
        Count character pair frequencies
            ↓
        Merge most frequent pair
            ↓
        Repeat
            ↓
        Build vocabulary


"""