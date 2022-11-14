class Reindeer:
    def __init__(self, name, speed, timeRunning, timeResting):
        self.name = name
        self.speed = speed
        self.timeRunning = timeRunning
        self.timeResting = timeResting
        self.timeLeftRunning = timeRunning
        self.timeLeftResting = 0
        self.dist = 0
        self.score = 0


def stepReindeer(reindeer):
    if reindeer.timeLeftRunning > 0:
        reindeer.dist += reindeer.speed
        reindeer.timeLeftRunning -= 1
        if reindeer.timeLeftRunning == 0:
            reindeer.timeLeftResting = reindeer.timeResting
    else:
        reindeer.timeLeftResting -= 1
        if reindeer.timeLeftResting == 0:
            reindeer.timeLeftRunning = reindeer.timeRunning


with open("input.txt") as f:
    reindeers = list()
    for data in f.readlines():
        data_split = data.split(" ")
        # Reindeer, speed, time-running, time-resting
        reindeers.append(
            Reindeer(
                data_split[0],
                int(data_split[3]),
                int(data_split[6]),
                int(data_split[-2])
            )
        )

    # Part 1 & 2
    totalTime = 2503
    maxDist = 0
    for second in range(totalTime + 1):
        for idx, reindeer in enumerate(reindeers):
            stepReindeer(reindeer)
        for leading_reindeer in filter(
                lambda rein1: rein1.dist == max(map(lambda rein2: rein2.dist, reindeers)),
                reindeers
        ):
            leading_reindeer.score += 1

    print("Answer 1: " + str(max(list(map(lambda x: x.dist, reindeers)))))
    print("Answer 2: " + str(max(list(map(lambda x: x.score, reindeers)))))
