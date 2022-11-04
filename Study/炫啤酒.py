money = 10
beers = money // 2
caps = 0
bottles = 0
count = 0
while beers > 0:
    caps = caps + beers
    bottles = bottles + beers
    count = count + beers
    beers = 0
    if caps >= 4:
        beers = beers + caps // 4
        caps = caps % 4
    elif bottles >= 2:
        beers = beers + bottles // 2
        bottles = bottles % 2
print(f"总共喝了{count}瓶啤酒！")
