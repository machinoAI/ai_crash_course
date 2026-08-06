"""
1. What is a Process?
    - A process is an independent running instance of a program with its own memory, resources, and Python interpreter.

    Example:
            python app.py

            The OS creates:  Process

                ├── Memory
                ├── Python Interpreter
                ├── GIL
                ├── Threads
                └── Resources
            Think of a process as a house.

2. Difference between Process and Thread
    | Process                | Thread                          |
    | ---------------------- | ------------------------------- |
    | Independent program    | Execution unit inside a process |
    | Own memory             | Shares process memory           |
    | Own Python interpreter | Uses the process's interpreter  |
    | Own GIL                | Shares the process's GIL        |
    | Heavyweight            | Lightweight                     |

3. How does multiprocessing use multiple CPU cores?
    - This is where the OS comes in.
    - The OS schedules different processes on different cores.

    Threading: Here GIL released always depends on whether it would be released and acquired by other threads or not.
        - You can't say it performs true parallelism.

        One Process
              │
        One Interpreter
              │
        One GIL
              │
        ───────────────
        Thread A

        Thread B

        Thread C

    Multi-Processing: Each process have their own memory, interpreter and GIL; A true parallelism.

        Process A          Process B
            │                  │
        Interpreter A     Interpreter B
            │                  │
         GIL A             GIL B
            │                  │
        Core 1             Core 2


4. Does every process have its own memory
    - Yes; Every memory has its own virtual memory space.

5. Why can't processes access each other's variables?
    - Because every process has its own memory and every variable stored in the corresponding memory space.
    - Hence each process has its own variables, memory.


6. Why does threading not require this?
    - Thread(...) :
        - It does not start another Python interpreter.
        - It simply creates another thread inside the same process.
        - No file is re-executed.
        - No recursion.


7. What is spawn, fork, and forkserver?
    - A start method defines how a new child process is created from the parent process.
    - Python provides three methods:
        - Spawn (Windows & macOS Default): It starts a completely new Python interpreter and imports the main module from scratch.

            Parent Process
                  │
                  ▼
            python child.py
                  │
            New Interpreter
                  │
            Own Memory
            Own GIL


        - Fork(Linux Default) : Fork creates a child process by copying the parent process, including its memory and interpreter state.
            Parent Process
                 │
                 ▼
            Fork
                 │
            Child Process
            (Copy of Parent)

        - Forkserver: Forkserver starts a dedicated server process that forks all future child processes.

            Main Process
                  │
                  ▼
            Fork Server
                  │
             ┌────┴────┐
             ▼         ▼
            Child 1   Child 2

8. Comparison:
    | Feature                | Spawn | Fork  | Forkserver          |
    | ---------------------- | ----- | ----- | ------------------- |
    | Starts new interpreter | ✅ Yes | ❌ No  | ❌ No                |
    | Copies parent memory   | ❌ No  | ✅ Yes | ✅ Yes (from server) |
    | Fast                   | ❌     | ✅     | ✅                   |
    | Safe with threads      | ✅     | ❌     | ✅                   |
    | Default on Windows     | ✅     | ❌     | ❌                   |
    | Default on Linux       | ❌     | ✅     | ❌                   |
    | Default on macOS       | ✅     | ❌     | ❌                   |


9. What is IPC (Inter-Process Communication)?
    - IPC is the mechanism that allows separate processes to exchange data and synchronize their execution.
    - Processes communicate using IPC.

    | IPC Mechanism            | Purpose                             |
    | ------------------------ | ----------------------------------- |
    | Queue                    | Many-to-many communication          |
    | Pipe                     | One-to-one communication            |
    | Shared Memory            | Share the same data without copying |
    | Manager                  | Share Python objects                |
    | Socket                   | Communication across machines       |
    | Event / Lock / Semaphore | Synchronization                     |


10. What is a Queue?
    A Queue is an IPC mechanism that allows multiple processes to safely exchange data using FIFO (First In, First Out).

11. 
"""