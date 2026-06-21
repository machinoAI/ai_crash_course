# A Decorator is a function which takes another function as input, adds some extra behaviour and returns a new function
# without modifying the original function's code.

import time

def measure_latency(func):

    def wrapper(**args):
        start_time = int(time.time()* 1000)

        result = func(**args)

        end_time = int(time.time() * 1000)

        latency = (end_time-start_time)

        print("Latency:", latency)

        return result

    return wrapper


@measure_latency
def fetch_data():
    time.sleep(0.2)
    print("Fetching Data...")


fetch_data()