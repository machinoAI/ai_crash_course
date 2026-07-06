"""
Chroma DB Pipeline:

                   Create Client
                        │
                        ▼
               Create/Get Collection
                        │
                        ▼
                 Prepare Documents
                        │
                        ▼
                  Generate IDs
                        │
                        ▼
                 Add Metadata
                        │
                        ▼
              Generate Embeddings
                        │
                        ▼
                  Add to Chroma
                        │
                        ▼
         Persist Automatically (PersistentClient)
                        │
                        ▼
         ┌──────────────┴──────────────┐
         ▼                             ▼
      Query by Text               Query by Vector
         ▼                             ▼
     Retrieve Docs               Retrieve Docs
         │
         ▼
   Update / Delete / Count / Peek


"""

# step 1: Create client:
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")


# step 2: create collection:
collection = client.get_or_create_collection(name="employees")

# step 3: prepare data:

documents = [
    "kunal is a Data Scientist.",
    "Rohan works as an ML Engineer.",
    "Manorma develops backend APIs."
]


# Step 4: Generate ids
ids = [
    "emp1",
    "emp2",
    "emp3"
]

# Step 5: Metadata:
metadatas = [
    {"department":"AI"},
    {"department":"ML"},
    {"department":"Backend"}
]

# Step 6:Embeddings
# option 1: Chroma creates its own embeddings

collection.add(
    ids = ids,
    documents=documents,
    metadatas=metadatas
)

# custom embeddings:
embedding_model="voyag3"

embeddings = embedding_model.embed_documents(documents)

collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

collection.count()    # count documents
collection.peek()     # inspection/debugging
collection.get(       # get by id
    ids=["emp1"]
)

# Step 7:Query by text

collection.query(
    query_texts=[
        "who works in AI"
    ],
    n_results=2
)

# Step 8:Query by text
query = "who works in AI"
query_embeddings = embedding_model.embed_query(query)

collection.query(
    query_embeddings=[query_embeddings],
    n_results=2

)

# Step 9: Filter by data
collection.query(
    query_texts=["engineer"],
    where = {
        "deparment":"ML"
    }
)

# Step 10: Get with Filter Only
collection.get(
    where={
        "department":"ML"
    }
)

# Step 11: collection update
collection.update(
    ids=["emp1"],
    documents=["Kunal is now senior Data Scientist"]
)

# Step 12: collection delete

collection.delete(
    ids=["emp3"]
)

# Step 13: Delete by filter
collection.delete(
    where={"department":"ML"}
)

# Step 14: List collections
client.list_collections()

# Step 15:
client.delete_collection("employees")

# Step 16: Reset database
client.reset()

"""
# RAG Evaluation Metrics:

- Precision@k
- Recall@k
- Hit Rate    -> Was at least one correct document retrieved? hit Rate =1

-MRR (Mean Reciprocal Rank) 
    1 D4
    2 D5
    3 D1 rank =3

    score= 1 / 3 = 0.33
 
 - nDCG:
    query = Who works in AI?
    
    D1 = Highly Relevant

    D2 = Somewhat Relevant
    
    D3 = Not Relevant
        
    Retriever returns:
    D2
    D3
    D1
    
    D1 should have been first.

    nDCG rewards:
        - Correct ranking
        - Highly relevant docs appearing early
    
    

"""