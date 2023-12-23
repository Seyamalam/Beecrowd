while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        print(" ".join([str(i) for i in range(1, entrada + 1)]))
