import threading
import time

def io_bound_task(seconds):
    time.sleep(seconds)

def measure_execution(seconds, num_threads):
    start = time.perf_counter()

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=io_bound_task, args=(seconds,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return time.perf_counter() - start

print(measure_execution(5, 1))
print(measure_execution(5, 2))