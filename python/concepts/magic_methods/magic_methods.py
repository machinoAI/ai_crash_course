"""
1. What is magic methods in python ?
    - Magic methods, also known as dunder (double underscore) methods.
    - It define how your custom Python objects to interact seamlessly with Python's built-in syntax and functions.
    - Python automatically invokes them when operations such as:
        - print(), len(), +, ==, indexing, or iteration are performed.

    - For example:
        - print(obj) calls obj.__str__(),
        - len(obj) calls obj.__len__(), and
        - obj1 + obj2 calls obj1.__add__(obj2).

    - They enable user-defined classes to behave like native Python types.


Examples:
        | Magic Method     | Triggered By         | Example                      | Without Magic Method                                               |
        | ---------------- | -------------------- | ---------------------------- | ------------------------------------------------------------------ |
        | `__init__()`     | Object creation      | `emp = Employee("Ravi", 30)` | Default constructor is used; custom initialization isn't possible. |
        | `__str__()`      | `print(obj)`         | `print(emp)`                 | Prints `<Employee object at 0x...>`                                |
        | `__repr__()`     | `repr(obj)`          | `repr(emp)`                  | Falls back to default object representation.                       |
        | `__len__()`      | `len(obj)`           | `len(team)`                  | `TypeError: object has no len()`                                   |
        | `__getitem__()`  | `obj[index]`         | `arr[0]`                     | `TypeError: object is not subscriptable`                           |
        | `__setitem__()`  | `obj[index] = value` | `arr[0] = 10`                | `TypeError: object does not support item assignment`               |
        | `__iter__()`     | `for x in obj`       | `for x in team:`             | `TypeError: object is not iterable`                                |
        | `__next__()`     | `next(iterator)`     | `next(it)`                   | `TypeError: object is not an iterator`                             |
        | `__contains__()` | `x in obj`           | `'Ravi' in employees`        | `TypeError` or falls back to iteration if supported.               |
        | `__add__()`      | `obj1 + obj2`        | `a + b`                      | `TypeError: unsupported operand type(s) for +`                     |
        | `__sub__()`      | `obj1 - obj2`        | `a - b`                      | `TypeError: unsupported operand type(s) for -`                     |
        | `__mul__()`      | `obj1 * obj2`        | `a * b`                      | `TypeError: unsupported operand type(s) for *`                     |
        | `__eq__()`       | `obj1 == obj2`       | `emp1 == emp2`               | Compares object identity (memory address) by default.              |
        | `__lt__()`       | `obj1 < obj2`        | `emp1 < emp2`                | `TypeError: '<' not supported between instances`                   |
        

What is __str__()?
    - A special (magic) method that defines the human-readable string representation of an object.
    - It is automatically called by print() and str().
    - __str__() defines how an object should be displayed as a human-readable string.


"""