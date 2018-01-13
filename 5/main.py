# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def isDivisibleEvenly(x, y, n):
    for d in range(x, y):
        z = n % d
        if(z > 0):
            return 0
    return 1

for a in range(11, 999999999):
    if(isDivisibleEvenly(1, 20, a)):
        print(a)