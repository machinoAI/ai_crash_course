"""
1. Why is multiprocessing slower than threading to start?

    - Multiprocessing is slower because creating a new process requires a new interpreter,
        memory space, and OS resources, whereas a thread shares the existing process resources.

    - Analogy: Building a new house vs adding a new room.

2. What is Pickling?

    - Pickling is the process of converting a Python object into a byte stream so
        it can be stored or transferred between processes.

    - Example:
        import pickle
        data = {"name": "Ravi"}
        bytes_data = pickle.dumps(data)

    Analogy: Packing a parcel before shipping.

3. Why do multiprocessing arguments get pickled?

    - Because processes have separate memory spaces, Python serializes (pickles) arguments before sending them to another process.
    - Analogy: You can't hand over RAM; you send a copy.

4. Serialization vs Pickling

    - Serialization: Converting an object into a transferable format.

    - Pickling: Python's serialization mechanism.


5. Why is sending a large NumPy array expensive?
    - Because the array must be serialized and copied into the destination process,
        consuming CPU, memory, and bandwidth.


    - Solution: Shared Memory.
    - Analogy: Photocopying a 500-page book.


6. What is Copy-on-Write (CoW) ?

    - Copy-on-Write allows parent and child processes to initially share memory after fork;
        a copy is created only when one process modifies the data.

    - Analogy: Two people share a document until one edits it.


7. What is Process Creation Overhead ?

    - Process creation involves allocating memory, creating an interpreter, setting up resources,
        and registering with the OS scheduler.

    - Much heavier than thread creation.


8. What is Context Switching ?

    - Context switching is the OS saving one process/thread's state and loading another's so execution can continue.
    - Excessive context switching hurts performance.

    - Analogy: One driver getting out, another getting into the same car.

9. ProcessPoolExecutor vs multiprocessing.Pool

    | ProcessPoolExecutor           | Pool                      |
    | ----------------------------- | ------------------------- |
    | Modern (`concurrent.futures`) | Older API                 |
    | Cleaner interface             | Lower-level               |
    | Returns `Future` objects      | Uses `map`, `apply`, etc. |



10. Threading vs Multiprocessing ?

    | Threading     | Multiprocessing     |
    | ------------- | ------------------- |
    | I/O-bound     | CPU-bound           |
    | Shared memory | Separate memory     |
    | One GIL       | One GIL per process |



11. Queue vs Pipe?

    | Queue           | Pipe            |
    | --------------- | --------------- |
    | Many-to-many    | One-to-one      |
    | FIFO mailbox    | Direct channel  |
    | Higher overhead | Slightly faster |


12. Manager vs Shared Memory:

    | Manager               | Shared Memory     |
    | --------------------- | ----------------- |
    | Shares Python objects | Shares raw memory |
    | Easy                  | Fast              |
    | Serialization         | Zero-copy         |
    | Safer                 | Needs Lock        |

13. Multiprocessing vs NumPy/OpenBLAS:

    - Multiprocessing: Parallelism by creating multiple Python processes.

    - NumPy/OpenBLAS : Parallelism inside optimized native C/C++ libraries.

14. Multiprocessing vs AsyncIO:

    | Multiprocessing    | AsyncIO                    |
    | ------------------ | -------------------------- |
    | CPU-bound          | I/O-bound                  |
    | Multiple processes | Single-threaded event loop |
    | True parallelism   | Cooperative concurrency    |

15. CPU-bound vs I/O-bound Decision Tree:

    | Scenario                      | Best Choice         |
    | ----------------------------- | ------------------- |
    | Pure Python computation       | Multiprocessing     |
    | Network/API calls             | Threading / AsyncIO |
    | Matrix multiplication         | NumPy/OpenBLAS      |
    | FastAPI thousands of requests | AsyncIO             |
    | Large data sharing            | Shared Memory       |
    | Python list/dict sharing      | Manager             |

"""