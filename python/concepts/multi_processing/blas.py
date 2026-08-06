"""
1. What is BLAS ?
    - Basic Linear Algebra Subprograms (BLAS)
    - Think of BLAS as library that knows how to perform mathematical operations extremely efficient.
    - For example:
        - Matrix Multiplication
        - Dot product
        - Matrix addition
        - Vector Multiplication
        - Matrix Transpose

    Instead of Python doing:
        for i:
            for j:
                ...

    BLAS performs these operations using highly optimized native code.

2. What is OpenBLAS?
    - OpenBLAS is one implementation of the BLAS standard.
    - BLAS =
        Specification
        ↓
        Different Implementations:
            • OpenBLAS
            • Intel MKL
            • Apple Accelerate
            • AMD BLIS

3. What is MKL?
    - MKL = Intel Math Kernel Library
    - Intel engineers optimized it specifically for Intel CPUs.
    - Advantages:
        - Uses SIMD instructions (AVX, AVX2, AVX512)
        - Uses cache efficiently
        - Uses multiple CPU cores
        - Highly optimized for Intel processors

    - When NumPy is installed through Anaconda, it often links against MKL.

4. Where does OpenMP come in?
    - It is a parallel programming framework for C/C++/Fortran.
    - It makes multithreading easy.
    - Without OpenMP:
        Thread t1(...);
        Thread t2(...);
        Thread t3(...);

        Lots of manual thread management.

    With OpenMP:
        #pragma omp parallel for
            for (...)

    Compiler automatically creates threads.


5. So who creates threads?
    There are actually three possibilities.
        - Python creates threads.
            threading.Thread()
        - NumPy creates native threads.
            - np.dot()
        - Multiprocessing
            - Process()

            OS creates processes. Each process has its own:
                CPython

                    ↓

                    Own GIL


    The architecture:
                Python Program
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ▼                ▼                ▼
Python Thread     Python Thread   Python Thread
      │                │                │
      └──────────────┬──────────────────┘
                     │
               Acquire GIL
                     │
             Execute Python Bytecode
                     │
             Call np.dot()
                     │
              Release GIL
                     │
             OpenBLAS Library
                     │
               OpenMP Runtime
                     │
      ┌────────┬────────┬────────┬────────┐
      ▼        ▼        ▼        ▼
    Core 1   Core 2   Core 3   Core 4


6. How does NumPy decide to use 1 thread, 4 threads, or all CPU cores?

    - How does OpenBLAS know how many threads to create?
        - It checks environment variables.
            - OPENBLAS_NUM_THREADS
            - MKL_NUM_THREADS
            - OMP_NUM_THREADS

        Example:
                export OPENBLAS_NUM_THREADS=4

    - If I don't specify anything?
        - OpenBLAS/MKL decides automatically. but that can lead into over subscriptions



"""