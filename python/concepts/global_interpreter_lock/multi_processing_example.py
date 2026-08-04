from multiprocessing import Process

x = 10

def worker():
    global x
    x = 20
    print(x)

p1 = Process(target=worker)
p2 = Process(target=worker)

p1.start()
p2.start()