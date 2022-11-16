from random import randint, random

game = input('是否开始游戏：')
while game == '是':
    mode = input('请输入游戏难度（简单/中等/炼狱）：')
    flag = False
    if mode == '简单':
        num = randint(0, 10)
        guss = int(input('请猜一个0~10的整数(3/3)：'))
        i = 2
        n = 3
        while i <= 3:
            i += 1
            n -= 1
            if guss < num:
                a = '你猜小了，请再试一次(' + str(n) + '/3):'
                guss = int(input(a))
            elif guss > num:
                a = '你猜大了，请再试一次(' + str(n) + '/3):'
                guss = int(input(a))
            else:
                flag = True
                print("6666666666666666666666666666猜对了")
                break
        if not flag:
            print("your are loser")
        game = input('是否继续游戏：')
    elif mode == '中等':
        num = random.randint(0, 100)
        guss = int(input('请猜一个0~100的整数：'))
        i = 2
        n = 3
        while i <= 3:
            i += 1
            n -= 1
            if guss < num:
                a = '你猜小了，请再试一次(' + str(n) + '/3):'
                guss = int(input(a))
            elif guss > num:
                a = '你猜大了，请再试一次(' + str(n) + '/3):'
                guss = int(input(a))
            else:
                print("6666666666666666666666666666猜对了")
                break
        if not flag:
            print("your are loser")
        game = input('是否继续游戏：')
    elif mode == '炼狱':
        num = randint(0, 100000)
        guss = int(input('请猜一个0~100000的整数：'))
        i = 2
        n = 3
        while i <= 3:
            i += 1
            n -= 1
            if guss < num:
                a = '你猜小了，请再试一次(' + str(n) + '/3):'
                guss = int(input(a))
            elif guss > num:
                a = '你猜大了，请再试一次(' + str(n) + '/3):'
                guss = int(input(a))
            else:
                print("6666666666666666666666666666猜对了")
                break
        if flag == False:
            print("your are loser")
        game = input('是否继续游戏：')
print('欢迎下次继续来找虐！bye~~')
