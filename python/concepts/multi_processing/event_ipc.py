"""
19. What is an Event?
    - An Event is a synchronization primitive used to notify one or more threads/processes
        that a particular event has occurred.

    - Event → Controls coordination/signaling

20. Why do we need an Event?
    - Imagine 'Process A' downloads a model 'Process B' , Should start inference only after the model is downloaded.

    How does B know ?
    - Use an Event


"""
from multiprocessing import Process, Event
import time


def downloader(event):
    print("Downloading model...")
    time.sleep(5)
    print("Download Complete")
    event.set()


def inference(event):
    print("Waiting for model...")
    event.wait()

    print("Model available")
    print("Starting inference...")


if __name__ == "__main__":

    event = Event()

    p1 = Process(target=downloader, args=(event,))
    p2 = Process(target=inference, args=(event,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()