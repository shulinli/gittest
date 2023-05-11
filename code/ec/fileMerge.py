import os
from ec import variable

"数据块合并"
def mergeFile(blockFilePath):
    listdir = os.listdir(blockFilePath)
    f = open(os.path.join(blockFilePath, "测试.docx"), "wb")
    for i in range(len(listdir)):
        fo = open(os.path.join(blockFilePath,"%s.txt"%(i+1)), "rb")
        while True:
            data = fo.read(1024)
            if not data:
                break
            f.write(data)

    print("\033[33;1m文件完成合并...\033[0m")
    print("*"*30)