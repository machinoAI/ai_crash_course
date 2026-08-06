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