"""
10. What is a Queue?
    - A Queue is an IPC mechanism that allows multiple processes to safely exchange data using FIFO (First In, First Out).
    - Many-to-many communication
    - Bidirectional needs to design not in-built like pipe.


"""
from multiprocessing import Process, Queue

def producer(q):
    q.put("Hello Ravi")

def consumer(q):
    print(q.get())


if __name__ == "__main__":

    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()