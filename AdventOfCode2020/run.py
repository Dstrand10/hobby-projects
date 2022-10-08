#!/usr/bin/env python3
import time
import subprocess
import os

def run_day(d):
    my_env = os.environ.copy()
    my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
    print(my_env)
    starttime = time.time()
    p = subprocess.Popen(
        ['python', f'day{d}.py'], cwd=f'./2020_12_{d}', stdout=subprocess.PIPE, env=my_env)
    result = p.stdout.read().decode('utf-8')
    endtime = time.time()
    t = endtime - starttime
    return result, t


def print_result(d, result, t):
    print(f'Day {int(d)}')
    print(result)
    print(f'Time: {round(t, 5)}s')
    print('---------------------------')


def main():
    start_t = time.time()
    for i in [13]: # range(1, 26):
        d = ('0' * int(i < 10)) + str(i)
        result, t = run_day(d)
        print_result(d, result, t)
    end_t = time.time()
    tot = end_t - start_t
    print(f'Total execution time: {round(tot, 5)}s')


if __name__ == '__main__':
    main()