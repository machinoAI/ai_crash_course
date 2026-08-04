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


6.



"""