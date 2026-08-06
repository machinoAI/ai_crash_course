"""
16. What is Lock ?
    - A Lock is a synchronization primitive that allows only one thread or process to access a shared resource at a time,
        preventing race conditions.

"""



from multiprocessing import Process, Value, Lock

def worker(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value += 1


if __name__ == "__main__":

    counter = Value('i', 0)
    lock = Lock()

    p1 = Process(target=worker, args=(counter, lock))
    p2 = Process(target=worker, args=(counter, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(counter.value)