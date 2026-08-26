documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals"
]

import numpy as np
import re


def tokenize(text):
    """Convert text into lowercase words."""
    return re.findall(r"\b\w+\b", text.lower())


def tfidf_vectorizer(documents):
    # -----------------------------------------
    # 1. Tokenize documents
    # -----------------------------------------

    tokenized_docs = [
        tokenize(doc)
        for doc in documents
    ]

    # -----------------------------------------
    # 2. Build vocabulary
    # -----------------------------------------

    vocabulary = []

    for doc in tokenized_docs:
        for word in doc:
            if word not in vocabulary:
                vocabulary.append(word)

    word_to_index = {
        word: i
        for i, word in enumerate(vocabulary)
    }

    # -----------------------------------------
    # 3. Calculate TF
    # -----------------------------------------

    n_docs = len(documents)
    n_words = len(vocabulary)

    tf = np.zeros(
        (n_docs, n_words)
    )

    for doc_idx, doc in enumerate(tokenized_docs):

        word_count = len(doc)

        for word in doc:
            word_idx = word_to_index[word]

            tf[doc_idx, word_idx] += 1 / word_count

    # -----------------------------------------
    # 4. Calculate Document Frequency
    # -----------------------------------------

    df = np.zeros(n_words)

    for word_idx, word in enumerate(vocabulary):

        for doc in tokenized_docs:

            if word in doc:
                df[word_idx] += 1

    # -----------------------------------------
    # 5. Calculate IDF
    # -----------------------------------------

    idf = np.log(
        n_docs / df
    )

    # -----------------------------------------
    # 6. TF × IDF
    # -----------------------------------------

    tfidf = tf * idf

    return vocabulary, tf, idf, tfidf


# =================================================
# Example
# =================================================

documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals"
]

vocabulary, tf, idf, tfidf = tfidf_vectorizer(
    documents
)

print("Vocabulary:")
print(vocabulary)

print("\nTF:")
print(tf)

print("\nIDF:")
print(idf)

print("\nTF-IDF:")
print(tfidf)


