# 这是一个开数字平方根的python程序
import math

s = input("输入一个数：")
s = float(s)
if s >= 0:
    s = math.sqrt(s)
    print("平方根是：", s)
else:
    print("负数不能开平方根")
print("结束了，没有什么返回值")
