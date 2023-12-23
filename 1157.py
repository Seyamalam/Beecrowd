x = int(input())
for i in [k for k in range(1, int(x / 2) + 1) if x % k == 0] + [x]:
    print(i)
