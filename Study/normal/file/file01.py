try:
    #file = open('file01.txt', mode='rt')
    #print("文件打开了：只读")
    #file.close()
    file = open('./Study/normal/file/file01.txt',mode='wt')
    print("文件打开了：只写")
    while True:
        s = input("请输入内容，输入exit退出输入：")
        if s == 'exit':
            break
        file.write(s + '\n')
    file.close()
    #file = open('file02.txt',mode='at')
    #print("文件打开了：追加")
    #file.close()
except:
    print("文件打开失败：文件不存在")
