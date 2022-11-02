for n in range(3, 101):
    flag = 1
    for m in range(2, n):
        if n % m == 0:
            flag = 0
            break
    if flag:
        print(n,end=",")
