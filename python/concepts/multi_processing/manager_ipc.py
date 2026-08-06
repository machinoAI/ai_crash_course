"""
15. What is a Manager?
    - A Manager is an IPC mechanism that allows multiple processes to safely share and modify Python objects
        such as lists, dictionaries, sets, and namespaces.

    - Worker processes run in parallel, but updates to a Manager object are serialized because
        they are handled by a single Manager process.

"""



from multiprocessing import Process, Manager

def worker(shared_list):
    shared_list.append("Ravi")

if __name__ == "__main__":

    manager = Manager()

    shared_list = manager.list()

    p1 = Process(target=worker, args=(shared_list,))
    p2 = Process(target=worker, args=(shared_list,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(shared_list)