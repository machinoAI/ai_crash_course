"""
1. Why PagedAttention if KV cache reduce KV memory significantly ?

    KV cache memory can explode when
        - many users/requests
        - long contexts
        - many concurrent sequences

        The GPU also needs to manage these KV caches efficiently.

        PagedAttention solves:
            - How do we efficiently allocate and manage KV-cache memory for
                many concurrent requests without wasting GPU memory?


2. What problem PagedAttention solves ?

    - Internal waste: Reserved memory isn't completely used
    - Fragmentation: Free GPU memory is scattered into small pieces


    - PagedAttention divides the KV cache into fixed-size blocks and
        stores those blocks in non-contiguous GPU memory, similar to virtual memory pages in an operating system.

    Example: Request A ->>  [Block 1] [Block 2] [Block 3] [Block 4]

    And those blocks don't need to be physically adjacent:

        GPU memory:

        [ A1 ][ C1 ][ B1 ][ A2 ][ B2 ][ free ][ A3 ]
                ↑             ↑             ↑
                └──── A's blocks ──────────┘

        - A mapping table tells the system:

            Request A
            Logical block 1 → Physical block 1
            Logical block 2 → Physical block 4
            Logical block 3 → Physical block 7


3. Why is PagedAttention useful for KV Cache?
    Imagine:

        - Request A → currently 1,000 tokens
        - You don't need to reserve memory for: 10,000 tokens

        - You allocate blocks as tokens actually arrive.

                1000 tokens
                 ↓
                allocate required blocks

                more tokens
                 ↓
                allocate more blocks

        - KV cache memory grows dynamically instead of requiring a large contiguous allocation upfront.

Note: GQA and PagedAttention both optimised the KV cache memory
    - GQA = reduce KV size.
    - PagedAttention = organize KV memory efficiently.


"""