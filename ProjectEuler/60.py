def findAllPrimesUpTo(nbr):
    import math
    primes = []
    for num in range(2, nbr):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes

primes = findAllPrimesUpTo(1000)

