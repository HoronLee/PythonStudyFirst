while True:
    n = int(input("请输入一个大于6的偶数"))
    try:
        n = int(n)
    except Exception as err:
        print(err)
        continue
    if n > 5 or n % 2 == 0:
        break
maxp = n // 2 + 1
for p in range(2,maxp):
    flag = True
    for i in range(2, p,):
        if p % i == 0:
            flag = False
            break
    if flag:
        q = n - p
        for i in range(2, q):
            if q % i == 0:
                flag = False
    if flag:
        print(n, "=", p, "+", q)