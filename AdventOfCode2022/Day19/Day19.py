from collections import deque


def solve(blueprint, minutes):
    SEEN_STATES = set()
    best_geod = 0
    queue = deque([(0, 0, 0, 0, 1, 0, 0, 0, minutes)])
    while queue:
        state = queue.popleft()
        total_ore, total_clay, total_obs, total_geod, total_ore_robots, total_clay_robots, total_obs_robots, total_geod_robots, t = state

        if total_geod > best_geod:
            best_geod = total_geod
        if t == 0:
            continue

        max_needed_ore = max(blueprint[0][0], blueprint[1][0], blueprint[2][0], blueprint[3][0])
        max_needed_clay = max(blueprint[0][1], blueprint[1][1], blueprint[2][1], blueprint[3][1])
        max_needed_obs = max(blueprint[0][2], blueprint[1][2], blueprint[2][2], blueprint[3][2])
        if total_ore > max_needed_ore * t - total_ore_robots * (t - 1):
            storage_0 = max_needed_ore * t - total_ore_robots * (t - 1)
        else:
            storage_0 = total_ore
        if total_clay > max_needed_clay * t - total_clay_robots * (t - 1):
            storage_1 = max_needed_clay * t - total_clay_robots * (t - 1)
        else:
            storage_1 = total_clay
        if total_obs > max_needed_obs * t - total_obs_robots * (t - 1):
            storage_2 = max_needed_obs * t - total_obs_robots * (t - 1)
        else:
            storage_2 = total_obs
        if total_ore_robots >= max_needed_ore:
            robot_0 = max_needed_ore
        else:
            robot_0 = total_ore_robots
        if total_clay_robots >= max_needed_clay:
            robot_1 = max_needed_clay
        else:
            robot_1 = total_clay_robots
        if total_obs_robots >= max_needed_obs:
            robot_2 = max_needed_obs
        else:
            robot_2 = total_obs_robots

        state = (storage_0, storage_1, storage_2, total_geod, robot_0, robot_1, robot_2, total_geod_robots, t)
        if state in SEEN_STATES:
            continue
        SEEN_STATES.add(state)

        storage = (storage_0, storage_1, storage_2, total_geod)
        # Geod robot
        if blueprint[3][0] <= state[0] and blueprint[3][1] <= state[1] and blueprint[3][2] <= state[2]:
            queue.append((storage_0 + robot_0 - blueprint[3][0], storage_1 + robot_1 - blueprint[3][1],
                          storage_2 + robot_2 - blueprint[3][2], total_geod + total_geod_robots, robot_0, robot_1,
                          robot_2,
                          total_geod_robots + 1, t - 1))
        # Obs robot
        if blueprint[2][0] <= storage[0] and blueprint[2][1] <= storage[1] and blueprint[2][2] <= storage[2]:
            queue.append((storage_0 + robot_0 - blueprint[2][0], storage_1 + robot_1 - blueprint[2][1],
                          storage_2 + robot_2 - blueprint[2][2], total_geod + total_geod_robots, robot_0, robot_1,
                          robot_2 + 1,
                          total_geod_robots, t - 1))
        # Clay robot
        if blueprint[1][0] <= storage[0] and blueprint[1][1] <= storage[1] and blueprint[1][2] <= storage[2]:
            queue.append((storage_0 + robot_0 - blueprint[1][0], storage_1 + robot_1 - blueprint[1][1],
                          storage_2 + robot_2 - blueprint[1][2], total_geod + total_geod_robots, robot_0,
                          robot_1 + 1, robot_2,
                          total_geod_robots, t - 1))
        # Ore robot
        if blueprint[0][0] <= storage[0] and blueprint[0][1] <= storage[1] and blueprint[0][2] <= storage[2]:
            queue.append((storage_0 + robot_0 - blueprint[0][0], storage_1 + robot_1 - blueprint[0][1],
                          storage_2 + robot_2 - blueprint[0][2], total_geod + total_geod_robots, robot_0 + 1,
                          robot_1, robot_2,
                          total_geod_robots, t - 1))
        queue.append((storage_0 + robot_0, storage_1 + robot_1,
                      storage_2 + robot_2, total_geod + total_geod_robots, robot_0, robot_1, robot_2,
                      total_geod_robots, t - 1))
    return best_geod


def func1and2(blueprints):
    ans1 = 0
    ans2 = 1
    for idx, blueprint in enumerate(blueprints):
        best_geod = solve(blueprint, 24)
        ans1 += (idx + 1) * best_geod
        if idx < 3:
            best_geod = solve(blueprint, 32)
            ans2 *= best_geod

    return ans1, ans2


def parse_data(data):
    blueprints = []
    for row in data:
        ore_robot = (int(row.split(".")[0].split()[-2]), 0, 0)
        clay_robot = (int(row.split(".")[1].split()[-2]), 0, 0)
        obs_robot = (int(row.split(".")[2].split()[-5]), int(row.split(".")[2].split()[-2]), 0)
        geod_robot = (int(row.split(".")[3].split()[-5]), 0, int(row.split(".")[3].split()[-2]))
        blueprints.append((ore_robot, clay_robot, obs_robot, geod_robot))
    return blueprints


def main():
    data = open("input.txt").read().split("\n")
    blueprints = parse_data(data)

    sol1, sol2 = func1and2(blueprints)
    print(f"Solution 1: {sol1}")
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
