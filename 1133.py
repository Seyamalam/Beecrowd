a = int(input())
b = int(input())
x, y = sorted([a, b])
for i in [k for k in range(x + 1, y) if k % 5 == 2 or k % 5 == 3]:
    print(i)
