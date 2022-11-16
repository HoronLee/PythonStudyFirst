n = int(input("输入一个整数"))
first = True
print(n, end="")
i = 2
while i <= n:
    while n % i == 0:
        if first:
            print("=", i, end="")
            first = False
        else:
            print("*", i, end="")
        n = n // i
    i = i + 1
