import threading
import time

def worker():
    print("Starting...")
    time.sleep(3)
    print("Done")

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

start = time.perf_counter()

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Elapsed: {time.perf_counter() - start:.2f}s")