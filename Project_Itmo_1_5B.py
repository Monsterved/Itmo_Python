# part1
from unittest import result
import numpy

def function(*data):
    function2 = list(filter(None, data))
    function = numpy.average(function2)
    return round(function, 2)

finish = function(1, 8, -17, None, -2, 5, 8, -7.5, None, 3, 1.3)
print(finish)

# part2
def function2(*digits):
    plus = []
    minus = []
    for i in digits:
        if i > 0:
            plus.append(i)
        else:
            minus.append(i)
    return sorted(plus), sorted(minus, reverse=True)

finish2 = function2(8, 1, -12, -9, 9, 3, -2.5, 6, 3.4)
print(finish2)

# part3
def function3(a, b):
    result = 1
    for i in range (abs(b)):
        result *= a
    if n < 0:
        result = 1 / result
    elif n == 0:
        result = 1
    return result

finish3 = function3(7, -2)
print(finish3)

def function4(a, b):
    if b > 0:
        return (a * function4(a, b - 1))
    else:
        return 1
a = int(input("enter ther number: "))
b = int(input("enter degree: "))
print("The result of exponentiation:", function4(a, b))
