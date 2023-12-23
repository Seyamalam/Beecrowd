while True:
    a, b = sorted([int(i) for i in input().split(" ")])
    if a <= 0 or b <= 0:
        break
    else:
        print(
            "%s Sum=%d"
            % (str(list(range(a, b + 1)))[1:-1].replace(",", ""), sum(range(a, b + 1)))
        )
