"""
1. What is wrong in the following code ?

    async def get_recommendations(user_id):
        response = await client.get(...)
        return response.json()

Issues:
    ❌ No timeout
    ❌ No status-code handling
    ❌ No retry policy
    ❌ No circuit breaker
    ❌ No validation
    ❌ No fallback
    ❌ What if response is malformed?
    ❌ What if service is unavailable?
    ❌ What if user_id is invalid?
    ❌ What if 10,000 requests arrive?


2. Code Review format:
             CODE REVIEW
                 │
      ┌──────────┼───────────┐
      ▼          ▼           ▼
 Correctness  Reliability  Performance
      │          │           │
      ▼          ▼           ▼
   bugs       failures     latency
   types      timeout      concurrency
   logic      retry        caching
   edge       fallback     DB calls
   cases      recovery     resource use
      │          │           │
      └──────────┼───────────┘
                 ▼
              SECURITY
                 │
                 ▼
            OBSERVABILITY
                 │
                 ▼
              SCALING




"""