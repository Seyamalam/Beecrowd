ordem = int(input())
for onomatopeia in range(ordem):
    a, b = [float(i) for i in input().split(" ")]
    try:
        print("%.1f" % (a / b))
    except ZeroDivisionError:
        print("divisao impossivel")
