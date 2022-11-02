n = int(input("输入一个数字"))
m = 2
while m < n:
    if n % m == 0:
        break
    m = m + 1
if m == n:
    print(n, "是素数")
else:
    print(n, "不是素数")
