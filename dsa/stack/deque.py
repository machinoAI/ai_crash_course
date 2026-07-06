"""
A Deque (Double Ended Queue) is a linear data structure in which elements can be inserted and removed
from both the front and the rear (back) efficiently, typically in O(1) time.

| Method                 | Description                                       |
| ---------------------- | ------------------------------------------------- |
| `append(x)`            | Add to right                                      |
| `appendleft(x)`        | Add to left                                       |
| `pop()`                | Remove from right                                 |
| `popleft()`            | Remove from left                                  |
| `extend(iterable)`     | Add multiple items to the right                   |
| `extendleft(iterable)` | Add multiple items to the left (in reverse order) |
| `rotate(n)`            | Rotate elements right (`n > 0`) or left (`n < 0`) |
| `clear()`              | Remove all elements                               |
| `len(dq)`              | Number of elements                                |


"""
from collections import deque

dq = deque([10, 20, 30 ,40])

for item in dq:
    print("deque item:", item)