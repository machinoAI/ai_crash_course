"""
0. GIL Diagram: The entire GIL in one diagram:

                 Python Thread

                   │
                   ▼

            Wants to execute bytecode?

                   Yes
                    │
                    ▼
              Acquire GIL
                    │
                    ▼
          Execute Python Bytecode
                    │
                    ▼
          Waiting on I/O ?

             Yes            No
              │              │
              ▼              ▼
         Release GIL    Keep GIL
              │
              ▼
       Another thread runs

   Golden Rule: The GIL protects the execution of Python bytecode, not CPU cores.

1. What is an interpreter?
    - Software that executes your Python code.

2. What is CPython?
    - he official Python interpreter written in C.
    - GIL is a CPython concept.

3. What happens when you run python main.py?

    Python Source Code
        ↓
    Compile to Bytecode
            ↓
    CPython Interpreter
            ↓
    CPU executes instructions

4. What is bytecode?
    - Intermediate instructions generated from Python code that CPython executes.
    - Example:  a = 10
                b = 20
                c = a + b

    becomes something like:

        LOAD_CONST
        STORE_NAME
        LOAD_CONST
        STORE_NAME
        LOAD_NAME
        LOAD_NAME
        BINARY_ADD
        STORE_NAME

    The interpreter executes these instructions one by one.

5. Why is the GIL called the Interpreter Lock?
    - Because it protects the interpreter while it executes Python bytecode.

6. Why is it called Global?
    - One lock for the entire interpreter process.
    - Not one lock per thread.

7. Why is it called a Lock?
    - Only one thread may execute Python bytecode at a time.

8. Why does the GIL exist?
    - To prevent multiple threads from corrupting CPython's internal memory.

9. Why does reference counting need GIL?
    - In case of race condition, The GIL ensures only one thread updates the reference count at a time.

10. How exactly does the GIL work while a program is running?
    - Think of the GIL as a key to the Python interpreter.

    Python Thread 1 ----\
                         \
    Python Thread 2 ------>  GIL (Key)  ----> CPython Interpreter
                          /
    Python Thread 3 ----/


    - Only the thread holding the key can execute Python bytecode. Others wait.
    - Key point: The GIL does not lock your program. It locks the interpreter.

11. When is the GIL acquired and released?

    - Acquired
        - Whenever a thread wants to execute Python bytecode.

    - Released
        - The GIL is released whenever the thread cannot make progress using the CPU.

    Examples:
            time.sleep()

            socket.recv()

            requests.get()

            file.read()

            database query

    Why?
        - Because the thread is waiting for something external.
        - Instead of blocking everyone else,
            Python says
               I'm waiting. Someone else can use the interpreter.

     - A thread acquires the GIL before executing Python bytecode and releases it whenever it blocks on an I/O operation or voluntarily yields execution.

12. Why does time.sleep() release the GIL?
    - time.sleep() releases the GIL because the thread isn't executing Python code.
    - It waits on the operating system, allowing another Python thread to use the interpreter.

13. Why do I/O operations release the GIL?
    - requests.get(...)
    - It takes time to fetch data , it might take 20 ms , 2s or 5 seconds
    during that time python can not compute anything so instead of
        Hold GIL ->> Wait 2 sec

        it does
            Release the GIL ->> wait ->> Reacquire GIL ->> Now another thread can run.

14. Why don't CPU-bound threads run in parallel?
    for i in range(100000000):
        total += i

    This loop executes Python bytecode continuously.
        LOAD_FAST

        BINARY_ADD

        STORE_FAST

        LOAD_FAST

        ...

    The thread always needs the interpreter.

    Therefore it always needs the GIL.

    Another thread also wants the GIL.

    Only one can have it.

    So execution looks like


    Thread A
    ██████

    Thread B
          ██████

    Thread A
                ██████

    Thread B
                      ██████

    Instead of:

    Thread A
    ████████████

    Thread B
    ████████████


    So two CPU-bound threads don't use two cores for Python bytecode in CPython.


    - CPU-bound threads continuously execute Python bytecode, so they continuously compete for the GIL.
    - Only one thread can execute at a time.


15. How do NumPy, PyTorch and TensorFlow bypass the GIL?
    - Python executes bytecode until it reaches a native library call.
    - It then transfers control to the C/C++ implementation, which releases the GIL and performs the heavy computation.

        Python Bytecode Starts
                │
                ▼
        Create A
                │
        Create B
                │
        Reach "A @ B"
                │
                ▼
        Call NumPy C Function
                │
        Release GIL
                │
                ▼
        NumPy/OpenBLAS computes matrix multiplication
        (using multiple CPU cores)
                │
                ▼
        Result returned to Python
                │
        Acquire GIL
                │
        Continue executing Python bytecode
        (print(C.shape))

16. Example: Python Loop + NumPy
    for i in range(100):
        x = np.dot(A, B)

    - Here in this case, since it's continuously running and doing dot product,
        for each iteration it will release the GIL as it hand over the dot product to numpy which is in c/c++.

"""