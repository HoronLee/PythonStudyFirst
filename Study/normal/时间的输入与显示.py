def my_Time():
    h = int(input("时："))
    if h < 0 or h > 23:
        raise Exception("无效的时间！")
    m = int(input("分："))
    if m < 0 or m > 59:
        raise Exception("无效的分")
    s = int(input("秒："))
    if s < 0 or s > 59:
        raise Exception("无效的秒")
    print("%02d:%02d:%02d" % (h, m, s))


try:
    my_Time()
except Exception as e:
    print(e)
