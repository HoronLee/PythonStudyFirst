import random

num = 5

if int(input("请输入一个数字:")) == num:
        print("恭喜你第一次就猜对了")
elif int(input("猜错了，还有两次机会，再试一次：")) == num:
    print("猜对了")
elif int(input("猜错了，还有最后一次机会，再试一次")) == num:
    print("恭喜，最后一次猜对了")
else:
    print("太逊了，一次都没猜对")
    print("答案是：",num)