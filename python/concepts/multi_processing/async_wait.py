"""
1. What is the difference between async def vs def ?

    - def → synchronous function

    - async def → asynchronous coroutine function


    Synchronous : Synchronous code executes sequentially.
    Asynchronous: Asynchronous code allows tasks to make progress concurrently, especially while one task is waiting for I/O.


    Note: But async def does NOT automatically make your code faster.

2. What is coroutine function ?

    - A coroutine is a function that can pause its execution and later resume from where it paused.

    Example:
        Normal Function: Start -> BLOCK for 5 sec ->> End
            def task():
                print("Start")
                time.sleep(5)
                print("End")

        Coroutine Function: Start ->> await ->> Pause ->> Other coroutine can run ->> 5 seconds complete ->> Resume ->> End

            async def task():
                print("Start")
                await asyncio.sleep(5)
                print("End")

            - That's what makes coroutines useful.

3. What is difference between Concurrency vs Parallelism ?
    - Concurrency:
        - Multiple tasks are in progress during the same period, but they may take turns executing.

    - Parallelism:
        - Multiple tasks are literally executing at the same time.
        - Multiple workers/CPU cores → actual simultaneous execution.


4. What is await ?

    - async def chat():
        response = await llm.generate()
        return response

    - Await means: This operation may take time. While I'm waiting for it, allow other asynchronous work to proceed.
    - await doesn't mean do things in parallel


    Request A
       │
       ├── Call LLM
       │
       ├── await ───────────────┐
       │                        │
       │                   Request B
       │                        │
       │                   Process B
       │                        │
       │                        │
       ◄────────────────────────┘
       │
    LLM response
       │
    Return A

5. Examples of classic async calls:
    - HTTP calls
    - Database calls
    - LLM calls
    - WebSockets
    - File/network I/O

6. What is asyncio ?

    - asyncio is Python's built-in library for asynchronous programming.
    - asyncio provides the machinery that lets Python run coroutines concurrently using an event loop.
    - asyncio provides the runtime machinery for scheduling and managing coroutines,
        primarily through the event loop and Tasks.

    - asyncio provides mechanisms such as:
    - Event Loop       ->>Manages and schedule asynchronous tasks.
    - Tasks           ->>>  A coroutine that has been scheduled to run on the event loop.
    - Futures          ->> Represents a result that will become available later.
    - gather()  --> run multiple async operations together and collect their results.
    - create_task() ->> Schedules a coroutine as a Task on the event loop.
    - Event         ->>> Provides a synchronization signal between async tasks
    - Semaphore     ->> Controls the concurrency
    - Queue         ->>> Provides asynchronous coordination for passing data between tasks
    - Timeout utilities ->>> Define the maximum amount of time allowed for an async operation

    - Under a process ->> single thread ->> multiple tasks running, but when task A is waiting for i/o then
        it allows to execute other tasks.
    - Every task has its own coroutines.


7. What is asyncio.gather() ?
    - Used to run multiple async operations concurrently.
    - Waits until all operations complete.
    - Returns their results.
    - Results are returned in the same order as the input coroutines.
    - Very useful when multiple I/O operations are independent.


    - gather() →

    Example:

    results = await asyncio.gather(
        call_llm(),
        search_vector_db(),
        call_external_api()
    )


8. What is asyncio.create_task() ?
    - create_task() schedule a coroutine as a task.

9. What is difference between Multiprocessing vs asyncio ?

    - Processes can provide CPU parallelism;
    - asyncio provides cooperative I/O concurrency



"""