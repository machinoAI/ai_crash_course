"""
17. What is semaphore?
    - A Semaphore is a synchronization primitive that allows a fixed number of threads or processes to access a shared resource simultaneously.


18. Why do we need Semaphore?
    - Suppose you have 100 worker processes but Only 3 database connections
    - Can all 100 use the database simultaneously?
        - NO
        - Instead Semaphore ensures only 3 process access the database remaining wait.

- A Semaphore controls concurrency by limiting the number of threads or processes that can access a shared resource simultaneously.
- Semaphore = Concurrency Controller
- Rate Limiter = Time-based Controller
"""
from multiprocessing import Process, Semaphore
import time


def worker(sem, worker_id):
    print(f"Worker {worker_id} is waiting...")

    with sem:
        print(f"Worker {worker_id} entered")
        time.sleep(3)
        print(f"Worker {worker_id} leaving")


if __name__ == "__main__":

    sem = Semaphore(2)   # Allow only 2 processes simultaneously

    processes = []

    for i in range(5):
        p = Process(target=worker, args=(sem, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()