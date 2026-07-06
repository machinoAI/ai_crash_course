"""
    - Given the query and this document together, how relevant is this document?
    - Re-ranker does not search, it re-orders

    type of re-rankers:
    1. Cross-Encoder:
        - Instead of embedding the query and document separately, it feeds them together into a transformer.
    - Popular cross encoders:
        - cohere re-ranker
        - BGE re-ranker
        - Jina re-ranker

    2. LLM Re-ranking: Use an LLM instead of a dedicated re-ranker
    3. Rule Based Re-ranking
    4. Hybrid ranking


"""
import chromadb


client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="employees")

results = collection.query(
    query_texts=["Who works in AI?"],
    n_results=20
)

from sentence_transformers import CrossEncoder

documents = results["documents"][0]
scores = CrossEncoder.rank(
    query="Who works in AI?",
    documents=documents
)

"""
output:
[
  ("John works in AI", 0.98),
  ("Alice ML Engineer", 0.91),
  ("Insurance policy", 0.15)
]
"""

