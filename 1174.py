array = []
for i in range(100):
    array.append(float(input()))
for a, b in enumerate(array):
    if b <= 10:
        print("A[%d] = %.1f" % (a, b))
