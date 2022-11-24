def writeFile():
    try:
        file = open('./Study/normal/file/file01.txt',mode='wt')
        file.write('abc\nxyz')
        file.close()
    except:
        print("文件写入失败")
    
def readFile():
    try:
        file = open('./Study/normal/file/file01.txt',mode='rt')
        print(file.read())
        file.close()
    except:
        print("文件读取失败")

def readFile_Line():
    try:
        file = open('./Study/normal/file/file01.txt',mode='rt')
        st = ""
        s = file.readline()
        while s != "":
            st = st + s
            s = file.readline()
        file.close()
    except:
        print("文件读取失败")
try:
    writeFile()
    readFile()
    print("文件读写完成")
except:
    print("文件读写失败")