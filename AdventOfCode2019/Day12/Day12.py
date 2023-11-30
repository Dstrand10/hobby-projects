import math


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def updatePos(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def calculateEnergy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z))


file = open("inputDay12.txt", "r")
content = file.read()
moons = []
starting_x = []
starting_y = []
starting_z = []
for row in content.split("\n"):
    row = row.strip("<").strip(">")
    x = int(row.split(",")[0].split("=")[-1])
    y = int(row.split(",")[1].split("=")[-1])
    z = int(row.split(",")[2].split("=")[-1])
    starting_x.append(x)
    starting_y.append(y)
    starting_z.append(z)
    moons.append(Moon(x, y, z))

step = 1
iter_to_x_repeating = None
iter_to_y_repeating = None
iter_to_z_repeating = None

while not iter_to_x_repeating or not iter_to_y_repeating or not iter_to_z_repeating:
    moon_copy = moons.copy()
    while moon_copy:
        chosen_moon = moon_copy.pop(0)
        for moon in moon_copy:
            if chosen_moon.x < moon.x:
                chosen_moon.vel_x += 1
                moon.vel_x -= 1
            elif chosen_moon.x > moon.x:
                chosen_moon.vel_x -= 1
                moon.vel_x += 1

            if chosen_moon.y < moon.y:
                chosen_moon.vel_y += 1
                moon.vel_y -= 1
            elif chosen_moon.y > moon.y:
                chosen_moon.vel_y -= 1
                moon.vel_y += 1

            if chosen_moon.z < moon.z:
                chosen_moon.vel_z += 1
                moon.vel_z -= 1
            elif chosen_moon.z > moon.z:
                chosen_moon.vel_z -= 1
                moon.vel_z += 1
    for moon in moons:
        moon.updatePos()
    if step == 1000:
        tot_energy = 0
        for moon in moons:
            tot_energy += moon.calculateEnergy()
        print(tot_energy)
    step += 1

    if not iter_to_x_repeating and starting_x == list(map(lambda moon: moon.x, moons)):
        iter_to_x_repeating = step
    if not iter_to_y_repeating and starting_y == list(map(lambda moon: moon.y, moons)):
        iter_to_y_repeating = step
    if not iter_to_z_repeating and starting_z == list(map(lambda moon: moon.z, moons)):
        iter_to_z_repeating = step

print(math.lcm(iter_to_x_repeating, iter_to_y_repeating, iter_to_z_repeating))
