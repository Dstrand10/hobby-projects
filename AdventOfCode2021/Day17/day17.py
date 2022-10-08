class RobotMissile:

    def __init__(self, x_vel, y_vel):
        self.x = 0
        self.y = 0
        self.init_x_vel = x_vel
        self.init_y_vel = y_vel
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.highest_y = 0

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        if self.x_vel > 0:
            self.x_vel -= 1
        elif self.x_vel < 0:
            self.x_vel += 1
        self.y_vel -= 1
        if self.highest_y < self.y:
            self.highest_y = self.y



def func1(in_data):
    x_min, x_max = list(map(int, in_data[0].split("x=")[1].split("..")))
    y_min, y_max = list(map(int, in_data[1].split("y=")[1].split("..")))
    robots = set()

    for x_init in range(x_max + 1):
        for y_init in range(-100, 100):
            rm = RobotMissile(x_init, y_init)
            while True:
                rm.move()
                if x_min <= rm.x <= x_max and y_min <= rm.y <= y_max:
                    robots.add(rm)
                if rm.x_vel == 0 and rm.x < x_min:
                    break
                elif rm.x_vel > 0 and rm.x > x_max:
                    break
                elif rm.y_vel < 0 and rm.y < y_min:
                    break
    for x in robots:
        print("xinit: " + str(x.init_x_vel) + " yinit: " + str(x.init_y_vel))

    print(len(robots))
    return max([x.highest_y for x in robots])







def func2(in_data):
    pass


def main():
    in_data = open("input.txt").read().split(",")



    sol1 = func1(in_data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(in_data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
