"""
1. What is an Event Loop ?

    - The event loop is the engine that manages and schedules asynchronous tasks.
    -Imagine you have tasks:

        Task A → waiting for LLM
        Task B → waiting for DB
        Task C → ready to run
        Task D → waiting for HTTP API

    The event loop keeps track of these.
                        Event Loop
                             │
               ┌─────────────┼─────────────┐
               ↓             ↓             ↓
            Task A         Task B        Task C
           waiting         waiting        ready
               │             │             │
           LLM response    DB response    RUN


    When something becomes ready, the event loop can resume that task.


2. Why do we need an event loop?
    async def task_a():
        response = await call_llm()
        return response

    When Python reaches: await call_llm()
        - the LLM might take 2 seconds to respond.

    We don't want the program to simply sit there doing nothing.
    Instead:
            Task A
              │
             │ call LLM
             ↓
            WAIT ─────────────────────┐
                                      │
                                 Event Loop
                                      │
                                      ↓
                                 Run Task B
                                      │
                                      ↓
                                 Run Task C
                                      │
                                      ↓
                             LLM response ready
                                      │
                                      ↓
                                Resume Task A

        That's the fundamental purpose of the event loop.


3. The event loop is usually associated with one thread:
    - A useful simplified model is:

        One thread
            │
            ▼
        ┌─────────────────┐
        │   Event Loop    │
        ├─────────────────┤
        │ Task A          │
        │ Task B          │
        │ Task C          │
        │ Task D          │
        └─────────────────┘

    - The event loop doesn't execute all four simultaneously.
    - Instead, it switches between tasks when they reach points where they can yield, such as await.
    - This is why we call it cooperative concurrency.


"""

import asyncio


async def task_a():
    print("A: Start")
    await asyncio.sleep(3)
    print("A: Finished")


async def task_b():
    print("B: Start")
    await asyncio.sleep(1)
    print("B: Finished")


async def main():
    await asyncio.gather(
        task_a(),
        task_b()
    )


asyncio.run(main())


"""
Output: 
    A: Start
    B: Start
    B: Finished
    A: Finished
    
    - The event loop knows both are waiting.
        After 1 second: B → resumes → Finished
        After 3 seconds: A → resumes → Finished

"""