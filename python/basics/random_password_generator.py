import random
import string
from operator import length_hint

#Methods:

# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)

print("Welcome to password generator!")

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

all = lower+digits+upper+symbols

length=int(input("Enter the length of the password:"))
password=random.sample(all, length)
password="".join(password)
print(password)