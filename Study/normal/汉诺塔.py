def f(n, A, B, X):
    if n == 1:
        print("从", A, "移动一个盘子到", B)
    else:
        f(n - 1, A, X, B)
        print("从", A, "移动一个盘子到", B)
        f(n - 1, X, B, A)


x = int(input("请输入A杆上盘子的数量！"))

f(x, "A", "B", "X")

