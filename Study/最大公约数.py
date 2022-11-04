num_one = int(input("输入第一个整数："))
num_two = int(input("输入第二个整数："))
flag = 0
min_num = min(num_one, num_two)
for convention in range(min_num, 0, -1):
    if (num_one % convention == 0) and (num_two % convention == 0):
        print(f"最大公约数：{convention}")
        flag = 1
        break
if flag == 0:
    print("某种错误？")
