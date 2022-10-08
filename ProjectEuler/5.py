# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import collections
import math
import numpy as np


def primeFactors(n):
    primes = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        primes.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            primes.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        primes.append(int(n))

    return primes


primeDict = {}

for i in range(2, 21):
    primes = primeFactors(i)
    for nbr, count in collections.Counter(primes).items():
        if primeDict.get(nbr, 0) >= count:
            continue
        else:
            primeDict[nbr] = count

print(primeDict)
ans = 1
for nbr, count in primeDict.items():
    ans *= pow(nbr, count)

print(ans)
