num_one = int(input("输入第一个整数："))
num_two = int(input("输入第二个整数："))
flag = 0
for min_multiple in range(1, num_one * num_two + 1, 1):
    if (min_multiple % num_one == 0) and (min_multiple % num_two == 0):
        print(f"最小公倍数：{min_multiple}")
        flag = 1
        break
if flag == 0:
    print("无最小公倍数或是某种错误？")
