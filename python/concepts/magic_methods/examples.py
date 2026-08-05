class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee(Name={self.name}, Age={self.age}, Salary={self.salary})"



    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, {self.salary})"


    def __len__(self):
        return len(self.name)


    def __getitem__(self, key):
        return getattr(self, key)


    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __iter__(self):
        return iter([self.name, self.age, self.salary])


    def __contains__(self, item):
        return item in [self.name, self.age, self.salary]


    def __add__(self, other):
        return self.salary + other.salary

    # emp1 - emp2
    def __sub__(self, other):
        return self.salary - other.salary

    # emp * 2
    def __mul__(self, multiplier):
        return self.salary * multiplier

    # emp1 == emp2
    def __eq__(self, other):
        return self.salary == other.salary

    # emp1 < emp2
    def __lt__(self, other):
        return self.salary < other.salary


emp1 = Employee("Ravi", 30, 100000)
emp2 = Employee("Amit", 28, 80000)

# __str__
print(emp1)

# __repr__
print(repr(emp1))

# __len__
print(len(emp1))

# __getitem__
print(emp1["name"])

# __setitem__
emp1["salary"] = 120000
print(emp1.salary)

print("=================================")
# __iter__
for value in emp1:
    print(value)

# __contains__
print("Ravi" in emp1)

# __add__
print(emp1 + emp2)

# __sub__
print(emp1 - emp2)

# __mul__
print(emp1 * 2)

# __eq__
print(emp1 == emp2)

# __lt__
print(emp1 < emp2)