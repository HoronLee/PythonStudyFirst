import math

while True:
    try:
        n = float(input("请输入一非负数"))
        if n < 0:
            raise Exception("输入的数值小于0")
        break
    except:
        print("请输入一个非负数！")
