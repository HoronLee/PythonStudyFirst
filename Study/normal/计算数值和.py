a = 0
while a <= 0 or a >= 10:
    a = int(input("输入a[1,9]"))
n = 0
while n <= 0:
    n = int(input("输入n"))
m = 0
s = 0
for i in range(n):
    m = 10 * m + a
    s = s + m
    if i < n - 1:
        print(m, end="+")
    else:
        print(m, end="=")
print(s)
