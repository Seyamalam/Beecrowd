entrada = int(input())
array = [entrada * (2**i) for i in range(10)]
for a, b in enumerate(array):
    print("N[%d] = %d" % (a, b))
