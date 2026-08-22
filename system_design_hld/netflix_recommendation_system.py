"""
# NETFLIX RECOMMENDATION SYSTEM

1. What are we recommending?

- Recommendation Target = the items the system predicts a user is most likely to engage with.

- Three options:

  1. Unified Model
     - One model handles all content types.
     - Pros → simpler, more training data, better generalization.
     - Risk → one content type can dominate the recommendations.

  2. Separate Models
     - Separate model for movies, TV shows, documentaries, etc.
     - Pros → better control over category-specific behavior.
     - Cons → higher engineering and maintenance cost.

  3. Hybrid Approach — Selected
     - Use one recommendation pipeline with content type as a feature.
     - Apply balancing/business rules so recommendations maintain appropriate category diversity.
     - Best trade-off between simplicity and category control.


2. What type of user feedback should we use?

- Explicit Feedback = direct user actions such as ratings, likes/dislikes and watch-list additions.
  - Problem → sparse and highly selection-biased.

- Implicit Feedback = behavior observed from normal usage.
  - Examples → click, play, pause, replay, early exit, watch duration.

- Selected approach → primarily use implicit feedback because it provides much denser behavioral data.


3. Why is CTR not sufficient for a recommendation system?

- CTR (Click-Through Rate) = percentage of recommendations that users click.

- Problem:
  - Click does not necessarily mean engagement.

  Example:
  - User clicks a movie → watches 10 seconds → leaves.
  - User clicks another movie → watches 3 hours.

- Both produce a click, but their actual engagement is very different.

- Therefore, optimize for a metric closer to actual consumption.


4. Why is Percentage Watched not sufficient?

- Percentage Watched = watched duration / total content duration.

- Problem → it is not directly comparable across content with different durations.

- Example:
  - 10% of a 3-hour movie = 18 minutes.
  - 10% of a 30-minute episode = 3 minutes.

- Therefore, percentage watched can misrepresent actual engagement.


5. What is the primary business metric?

- Session Watch Time = total time a user spends consuming content during a session.

- It better captures actual engagement than simple clicks.

- Primary online optimization target:
  → Session Watch Time.


6. What are the important NFRs?

- Latency → recommendations should be returned within milliseconds.
- Scalability → support hundreds of millions of active users.
- Availability → recommendation service should remain available at large scale.
- Accuracy vs Latency → complex models may improve accuracy but increase inference latency.

- Core trade-off:

  Model Complexity ↑
       ↓
  Accuracy potentially ↑
       +
  Inference Cost/Latency ↑


7. What are the evaluation metrics?

- Evaluation is divided into:

  Offline Metrics
       ↓
  Before deployment

  Online Metrics
       ↓
  Production / A/B testing


8. What are the important Offline metrics?

- Precision = among recommended items, how many were relevant?

  Precision =
  Relevant Recommended Items
  ──────────────────────────
  Total Recommended Items

- Recall = among all historically relevant items, how many were recommended?

  Recall =
  Relevant Recommended Items
  ───────────────────────────
  Total Historically Relevant Items

- F1 Score = harmonic mean of Precision and Recall.

  F1 = 2 × Precision × Recall
       ───────────────────────
        Precision + Recall

- MAP (Mean Average Precision) = mean of Average Precision across users/queries; evaluates ranking quality while rewarding relevant items appearing higher.

- MAR (Mean Average Recall) = mean of Average Recall across users/queries; measures ranking/recommendation coverage.

- Important:
  → Precision focuses on correctness.
  → Recall focuses on coverage.
  → MAP/MAR evaluate these across users while considering recommendation quality.


9. What are the important Online metrics?

- Online metrics are measured using real production users.

- A/B Testing = compare the existing model against a new model using different user cohorts.

  Group A → Current/Baseline Model
  Group B → New Model

- Primary metric:
  → Session Watch Time

- Also monitor:
  → Latency
  → Error rate
  → Other business/engagement metrics

- A new model should only be rolled out if it improves the target metric without violating important NFRs such as latency.


10. What is the high-level recommendation architecture?

  User
    ↓
  API Gateway / Load Balancer
    ↓
  Recommendation Service
    ↓
  Candidate Generation
    ↓
  ~100 Candidates
    ↓
  Ranking Model
    ↓
  Top 20 Recommendations
    ↓
  Redis Cache
    ↓
  User

- This is called a Multi-Stage Recommendation Architecture.


11. Why do we need a multi-stage recommendation architecture?

- Suppose the catalog contains 100K videos.
- Running a complex ranking model against all 100K items for every request is too expensive.

- Instead:

  100,000 items
       ↓
  Candidate Generation
       ↓
  ~100 candidates
       ↓
  Complex Ranking Model
       ↓
  Top 20

- Candidate Generation → optimize for HIGH RECALL.
- Ranking → optimize for HIGH PRECISION.

- Key principle:

  Cheap model → reduce search space
       ↓
  Expensive model → make final decision


12. What is Candidate Generation?

- Candidate Generation = first stage that retrieves a small set of potentially relevant items from the complete catalog.

- Example:

  Catalog = 100K
       ↓
  Candidate Generation
       ↓
  100 candidates

- Main objective:
  → High Recall.

- Missing a good candidate at this stage means the ranking model can never recommend it.


13. What is Ranking?

- Ranking = second stage that scores the shortlisted candidates and selects the final recommendations.

- Example:

  100 candidates
       ↓
  Ranking Model
       ↓
  Top 20

- Main objective:
  → High Precision / ranking quality.

- Since only 100 items are evaluated, a more computationally expensive model can be used.


14. What model options can be used for Candidate Generation?

- Collaborative Filtering
  - Uses user-item interaction patterns.
  - Candidate source → behavior of similar users/items.
  - Common approaches → KNN, Matrix Factorization.

- Content-Based Filtering
  - Uses item metadata/content similarity.
  - Candidate source → similarity to items the user has consumed.

- Embedding-Based Retrieval
  - Represents users/items as vectors.
  - Candidate source → nearest items in embedding space.
  - Retrieval → ANN / vector similarity search.

- Hybrid Candidate Generation — selected
  - Run multiple candidate generators in parallel.
  - Merge results.
  - Deduplicate.
  - Apply filters/business constraints.
  - Produce final high-recall candidate set.


15. What are the trade-offs between Candidate Generation approaches?

- Collaborative Filtering:
  - Strong at exploiting behavioral patterns.
  - Weak for new users with no interaction history.

- Content-Based:
  - Works for new items because metadata exists before interactions accumulate.
  - Can become overly similar to the user's existing preferences.

- Embedding-Based:
  - Efficient similarity retrieval at scale.
  - Requires substantial training data and offline computation.

- Hybrid:
  - Combines strengths of multiple approaches.
  - More engineering complexity.


16. What is Cold Start?

- Cold Start = insufficient historical interaction data for making personalized recommendations.

- User Cold Start:
  - New user has little/no watch history.
  - Collaborative filtering has insufficient behavioral information.

- Item Cold Start:
  - New movie/show has little/no interaction data.
  - Collaborative filtering cannot easily surface it.

- Content-based methods can help with item cold start because metadata is available immediately.


17. How does the Hybrid Candidate Generator work?

  User
    │
    ├──► Collaborative Filtering ──► Candidates
    │
    ├──► Content-Based ────────────► Candidates
    │
    └──► Embedding Retrieval ──────► Candidates
                     │
                     ▼
              Merge Candidates
                     ↓
                Deduplicate
                     ↓
                 Filter
                     ↓
             ~100 Candidates
                     ↓
              Ranking Model


18. What data/storage architecture is used?

- PostgreSQL / MySQL
  - User metadata.
  - Video metadata.
  - Structured, relatively slow-changing data.

- Kafka
  - Real-time interaction/event stream.
  - Clicks, plays, pauses, replays.
  - High-throughput ingestion and decoupling.

- Cassandra
  - Aggregated/high-volume interaction data.
  - Horizontally scalable.
  - High write throughput.

- S3
  - Raw videos.
  - Training logs.
  - Historical/back-up data.

- Vector DB (Pinecone / Milvus)
  - User/video embeddings.
  - Fast similarity retrieval.


19. Why use Kafka before Cassandra?

- Kafka = distributed event streaming/message system used to ingest and decouple high-volume events.

  User Events
       ↓
     Kafka
       ↓
  Aggregator
       ↓
  Cassandra

- Benefits:
  - Absorbs high-throughput event traffic.
  - Decouples producers from storage.
  - Allows consumers to process events asynchronously.


20. Why use Cassandra for interaction data?

- Cassandra = distributed wide-column NoSQL database optimized for high write throughput and horizontal scalability.

- Suitable because recommendation systems generate huge volumes of behavioral events.

- Important distinction:

  PostgreSQL/MySQL → structured metadata
  Cassandra       → high-volume interaction data


21. Why use a Vector DB?

- Vector DB = database/index optimized for storing and searching high-dimensional embeddings.

- It stores:
  - User embeddings.
  - Video embeddings.

- Candidate Generation can perform similarity search:

  User Embedding
       ↓
  Vector DB
       ↓
  Similar Video Embeddings
       ↓
  Candidate IDs


22. What is the role of Redis?

- Redis = in-memory key-value store used for very fast reads.

- Store:
  → Precomputed final recommendations.

- Example:

  user_123 → [video_17, video_42, video_91, ...]

- Benefit:
  → Avoid recomputing recommendations for every page load.


23. What is the Real-Time vs Batch strategy?

- Real-Time:
  - Generate recommendations on demand.
  - Useful when recent user behavior needs to influence recommendations immediately.

- Batch:
  - Precompute recommendations offline.
  - Useful for popular, trending or relatively static recommendation sets.

  Batch
    ↓
  Precompute
    ↓
  Redis

  Real-Time Request
    ↓
  Recommendation Service
    ↓
  Compute dynamically

- Hybrid approach:
  → Use batch where possible + real-time computation where personalization/freshness requires it.


24. What is the end-to-end request flow?

  User Device
       ↓
  API Gateway / Load Balancer
       ↓
  User Service
       ↓
  Recommendation Service
       ↓
  Candidate Generation
       │
       ├── Cassandra → recent interactions
       ├── Vector DB → embedding retrieval
       ├── Collaborative Filtering
       └── Content-Based Filtering
       ↓
  Merge + Deduplicate + Filter
       ↓
  ~100 Candidates
       ↓
  Ranking Service
       ↓
  Top 20
       ↓
  Redis
       ↓
  User


25. What does the Ranking Model predict?

- Ranking Model = model that assigns a score to each candidate so candidates can be ordered.

- In this design, the ranking objective is to predict the candidate's expected contribution to user engagement, particularly session watch time.

- Model options mentioned:
  - Deep Neural Network
  - XGBoost

- Important design point:
  → The ranking model can be much more complex than the candidate generator because it only evaluates ~100 candidates instead of the entire catalog.


26. What is Negative Downsampling?

- Negative Sample = an item shown/recommended to a user but not consumed.

- Recommendation datasets are highly imbalanced:

  Not watched  ████████████████████████
  Watched      ██

- If we train directly on raw data, the model can become biased toward predicting "not watched."

- Negative Downsampling = intentionally keep all/most positive examples while sampling only a subset of negative examples.

  Positive examples → retain
  Negative examples → downsample

- Goal:
  → Reduce class imbalance and make training more informative.


27. What are the important capacity numbers?

- Users = 500M
- Interactions/user/day = 100
- Recommendations/user/day = 20
- Interaction event size = 1 KB
- Catalog = 100K videos
- Embedding size = 512 bytes
- Assumed peak/average request rate = 100K RPS

- Interaction storage:

  500M × 100 × 1 KB
  ≈ 50 TB/day

  30 days
  ≈ 1.5 PB

- Recommendation cache:

  500M × 20 × 1 KB
  ≈ 10 TB/day

  7 days
  ≈ 70 TB

- Embeddings:

  User:
  500M × 512 bytes
  ≈ 256 GB

  Videos:
  100K × 512 bytes
  ≈ 50 MB


28. What is the main scalability bottleneck in this design?

- Do NOT run the expensive ranking model over the complete catalog.

- Instead:

  Huge Catalog
       ↓
  Cheap Retrieval
       ↓
  Small Candidate Set
       ↓
  Expensive Ranking

- This is the key scalability principle of the architecture.


29. What are the major trade-offs?

- Unified vs Separate Models
  → simplicity/data sharing vs category control.

- Candidate Recall vs Ranking Precision
  → retrieve broadly first, rank accurately later.

- Model Accuracy vs Latency
  → more complex models can improve quality but increase inference cost.

- Real-Time vs Batch
  → freshness/personalization vs lower compute and latency.

- Collaborative vs Content-Based vs Embedding
  → behavioral signal vs metadata vs learned semantic similarity.

- More Candidate Generators
  → better coverage/diversity but higher system complexity.


30. What should I say in an interview if asked to design Netflix Recommendation System?

- I would use a multi-stage recommendation architecture.
- First, collect implicit user interactions through Kafka and store aggregated behavioral data in a scalable store such as Cassandra.
- For each request, candidate generation combines collaborative filtering, content-based retrieval and embedding-based ANN retrieval to maximize recall.
- The candidates are merged, deduplicated and filtered down to roughly 100 items.
- A more expensive ranking model then scores those candidates based on expected engagement, with session watch time as the primary business metric.
- The top 20 recommendations are returned and cached in Redis.
- For scale and latency, I would combine real-time recommendations for fresh user behavior with batch precomputation for stable/trending content.
- I would validate models offline using Precision, Recall, MAP, MAR and F1, and finally use A/B testing with Session Watch Time and latency as key online metrics.


31. What are the 10 things to remember?

- 1. Primary objective → Session Watch Time.
- 2. Use implicit feedback because explicit feedback is sparse/biased.
- 3. Multi-stage architecture → Candidate Generation + Ranking.
- 4. Candidate Generation → high recall.
- 5. Ranking → high precision.
- 6. Use multiple candidate generators → collaborative + content + embeddings.
- 7. Handle user/item cold start explicitly.
- 8. Kafka → event ingestion; Cassandra → high-volume interaction storage.
- 9. Vector DB → embedding retrieval; Redis → recommendation caching.
- 10. Offline metrics + online A/B testing are both required.
"""