list = range(1, 101)
total_of_range = sum(list)
ans = pow(total_of_range, 2)

for i in list:
    ans -= pow(i, 2)

print(ans)
