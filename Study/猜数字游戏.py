import random

num = random.randint(1,10)
guss = int(input("已经随机生成一个数字，请输入你猜的数字（一共有三次机会）："))
if num == guss:
    print("恭喜你一次就猜对了")
else:
    if num < guss:
        guss = int(input("你猜大了，还有两次机会："))
        if num < guss:
            guss = int(input("你猜大了，还有一次机会："))
            if guss != num:
                print("太逊了，一次都没有答对")
            elif guss == num:
                print("你丫的终于猜对了")
        else:
            guss = int(input("你猜小了，还有一次次机会："))
            if guss != num:
                print("太逊了，一次都没有答对")
            elif guss == num:
                print("你丫的终于猜对了")
    else:
        guss = int(input("你猜小了，还有两次机会："))
        if num < guss:
            guss = int(input("你猜大了，还有一次机会："))
            if guss != num:
                print("太逊了，一次都没有答对")
            elif guss == num:
                print("你丫的终于猜对了")
        else:
            guss = int(input("你猜小了，还有一次次机会："))
            if num < guss:
                guss = int(input("你猜大了，还有一次机会："))
                if guss != num:
                    print("太逊了，一次都没有答对")
                elif guss == num:
                    print("你丫的终于猜对了")