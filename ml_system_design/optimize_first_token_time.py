"""
1. Your LLM takes 1.5 seconds to generate the first token, but subsequent tokens arrive in just 30 ms each.
    What causes this latency gap, and how would you optimize time-to-first-token (TTFT)?



    - Here's what is actually happening:
     - Generating text happens in two very different phases.

        - Prefill: the model reads your entire prompt at once and builds an internal cache (the KV cache).
        - This is one big, compute-heavy pass over every token you sent. Long prompt → long prefill.

        - Decode: the model then produces one token at a time, reusing that cache.
            Each step is tiny and memory-bound, so tokens stream out fast.

    So TTFT ≈ queue wait + prefill. The 30 ms is decode. A long prompt punishes the first token, not the rest.

    How you'd actually reduce TTFT:

    1. Send fewer tokens
    - Prefill cost scales with prompt length, so trim the prompt first
    - In RAG, retrieve top-5 well-ranked chunks instead of top-20 mediocre ones
    - Compress or summarise long chat history instead of resending it every turn
    - Move static rules into a system prompt you can cache, not into every user message

    2. Cache the prefix
    - Most prompts share a big, unchanging prefix (system prompt, tools, few-shot examples)
    - Prompt caching / KV-cache reuse lets the server skip re-reading that prefix
    - Put stable content first and variable content last, or the cache won't hit
    - This is usually the single biggest TTFT win and it also cuts cost

    3. Fix the queue, not just the model
    - Under load, most of TTFT is waiting, not computing
    - Continuous batching (vLLM, TGI) admits new requests instead of making them wait for a batch to finish
    - Separate fast interactive traffic from bulk/batch jobs so a 50-page summarisation doesn't block a chat reply
    - Add capacity based on p99 TTFT, not average GPU utilisation

    4. Shorten the physical path
    - Serve from a region close to your users; cross-continent round trips add real milliseconds
    - Reuse HTTP connections, keep TLS sessions warm, avoid a cold proxy hop
    - Cold starts on serverless GPUs can dominate everything else — keep a warm pool

    5. Overlap work instead of serialising it
    - Run retrieval, safety pre-checks, and auth in parallel, not one after another
    - Start streaming as soon as the first token exists; don't buffer the full answer
    - Do slower checks on the streamed output while it renders

    6. Make the wait feel shorter
    - Stream, always — perceived latency is what users judge
    - Show retrieval status ("searching your documents…") so the pause has meaning
    - Render a skeleton immediately instead of a blank screen
"""