array = []
while True:
    entrada = int(input())
    if entrada < 0:
        break
    else:
        array.append(entrada)
print("%.2f" % (sum(array) / float(len(array))))
