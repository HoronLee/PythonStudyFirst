print("开始")
try:
    print("除法")
    n = 1 / 0
except Exception as err:
    print("进入异常处理")
    print("error")
print("结束")