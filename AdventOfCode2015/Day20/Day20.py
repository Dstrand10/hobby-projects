def prime_factors(n):
    factors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors


with open("input.txt") as f:
    data = int(f.read())
    # data = [line.strip() for line in f.readlines()]

    house = 500000 #Comes after 600'000 so start from there to take a shortcut
    presentHouse = -1
    while presentHouse < data:
        house += 1
        factors = prime_factors(house)
        presentHouse = sum(factors) * 10
        if house % 100000 == 0:
            print("House: " + str(house) + ", Presents: " + str(presentHouse) + ".")
    print("Answer 1: " + str(house))

    house = 0 #Comes after 700'000 so start from there to take a shortcut
    presentHouse = -1
    factors_visits = dict()
    while presentHouse < data:
        house += 1
        factors = prime_factors(house)
        for factor in factors:
            factors_visits[factor] = factors_visits.get(factor, 0) + 1
        presentHouse = sum([factor for factor in factors if factors_visits[factor] <= 50]) * 11
        if house % 100000 == 0:
            print("House: " + str(house) + ", Presents: " + str(presentHouse) + ".")
    print("Answer 2: " + str(house))
