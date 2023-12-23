fib = [0, 1, 1]
maximo = int(input())
for i in range(3, maximo):
    fib.append(fib[i - 1] + fib[i - 2])
print(" ".join([str(k) for k in fib]))
