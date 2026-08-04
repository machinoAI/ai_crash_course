import threading
import numpy as np
import time

A = np.random.rand(3000, 3000)
B = np.random.rand(3000, 3000)

def worker():
    print("Start")
    C = np.dot(A, B)
    print("Done")

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

start = time.perf_counter()

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Elapsed: {time.perf_counter() - start:.2f}s")