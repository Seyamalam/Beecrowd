array = []
while True:
    entrada = float(input())
    if entrada >= 0 and entrada <= 10:
        array.append(entrada)
    else:
        print("nota invalida")
    if len(array) == 2:
        print("media = %.2f" % (sum(array) / 2.0))
        break
