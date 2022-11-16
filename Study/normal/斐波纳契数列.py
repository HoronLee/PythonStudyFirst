# Fibonacci series: 斐波纳契数列
# 使用无中间变量语句
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
    # 等价于
    # n=b
    # m=a+b
    # a=n
    # b=m
