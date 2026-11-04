import numbers
from random import randint

def primary(mult):
    def secundary(number):
        return mult * number
    return secundary

numbers = [randint(1, 10) for _ in range(10)]

duplicate = primary(2)
triplicate = primary(3)
quadruplicate = primary(4)

for number in numbers:
    print(f"Number: {number}, Duplicate: {duplicate(number)}, Triplicate: {triplicate(number)}, Quadruplicate: {quadruplicate(number)}")