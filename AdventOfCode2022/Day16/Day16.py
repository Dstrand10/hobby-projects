def parse_data(data):
    valves = dict()
    for row in data:
        valve = row.split()[1]
        flow_rate = int(row.split("=")[1].split(";")[0])
        childValves = [valve.replace(",", "") for valve in row.split("valve")[1].split() if valve != "s"]
        valves[valve] = (valve, flow_rate, childValves)
    return valves


def floyd_warshall(valves):
    dist = {v: {u: int(1e9) for u in valves} for v in valves}

    for v in valves:
        dist[v][v] = 0
        for childValve in valves[v][2]:
            dist[v][childValve] = 1

    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    with open("input.txt") as f:
        valves = parse_data(f.readlines())
        dist = floyd_warshall(valves)
        non_zero_valves = [valve for valve in valves if valves[valve][1] > 0]

        def generated_open_options(pos, open_valves, time_left):
            for next in non_zero_valves:
                if next not in open_valves and dist[pos][next] <= time_left:
                    open_valves.append(next)
                    yield from generated_open_options(next, open_valves, time_left - dist[pos][next] - 1)
                    open_valves.pop()
            yield open_valves

        def get_score_open_valves_combination(opened_valves, time_left):
            curr_valve, ans = 'AA', 0
            for v in opened_valves:
                time_left -= dist[curr_valve][v] + 1
                ans += valves[v][1] * time_left
                curr_valve = v
            return ans

        print("Solution 1: ", max([get_score_open_valves_combination(opened_valves, 30) for opened_valves in
                                   generated_open_options('AA', [], 30)]))

        human_max_pressure = 0
        best_human_opened_valves = None
        for human_opened_valves in generated_open_options('AA', [], 26):
            curr_pressure = get_score_open_valves_combination(human_opened_valves, 26)
            if curr_pressure > human_max_pressure:
                human_max_pressure = curr_pressure
                best_human_opened_valves = human_opened_valves.copy()
        non_zero_valves = [valve for valve in non_zero_valves if valve not in best_human_opened_valves]
        print("Solution 2: ",
              human_max_pressure + max([get_score_open_valves_combination(opened_valves, 26) for opened_valves in
                                        generated_open_options('AA', [], 26)]))


if __name__ == "__main__":
    main()
