"""
13. What is Shared Memory?
    - Shared Memory is an IPC mechanism that allows multiple processes to access the same memory region without copying data.

14. Why do we use NumPy with Shared Memory?
    - Because NumPy arrays can directly use a shared memory buffer, allowing multiple processes to access the
        same large dataset without copying it.


"""

from multiprocessing import Process, shared_memory
import numpy as np


def worker(shm_name):

    shm = shared_memory.SharedMemory(name=shm_name)
    arr = np.ndarray((5,), dtype=np.int64, buffer=shm.buf)

    print("Child Before :", arr)

    arr[0] = 100

    print("Child After  :", arr)

    shm.close()


if __name__ == "__main__":


    shm = shared_memory.SharedMemory(create=True, size=5 * 8)
    arr = np.ndarray((5,), dtype=np.int64, buffer=shm.buf)

    arr[:] = [1, 2, 3, 4, 5]

    print("Parent Before:", arr)

    p = Process(target=worker, args=(shm.name,))
    p.start()
    p.join()

    print("Parent After :", arr)

    shm.close()
    shm.unlink()