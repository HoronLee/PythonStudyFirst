# 这是一个开数字平方根的python程序
import math

s = input("输入一个数：")     # 输入待开方的数
s = float(s)                # 将字符串类型转化为浮点类型
if s >= 0:                  # 开放数必须是非负数
    s = math.sqrt(s)        # 引用math的类库方法，赋值回s
    print("平方根是：", s)    # 打印开放后的数值
else:                       # 不满足非负数就不执行开方
    print("负数不能开平方根")
print("结束了")
