import math
import os
from ec import variable

"文件开始切块"
def processSplite(orignFilePath,chunkSize,goalFilePath):
    blockSize,i= 0,0
    fo = open(orignFilePath, "rb")
    fi = open(os.path.join(goalFilePath,"%s.txt"%(i+1)),"wb")
    while True:
        data = fo.read(1024)
        if not data:
            break
        blockSize += len(data)
        fi.write(data)
        # 数据块大小
        if blockSize == chunkSize:
            fi.close()
            i += 1
            fi = open(os.path.join(goalFilePath,"%s.txt"%(i+1)),"wb")
            blockSize = 0

"文件分块"
def splitFile():
    # 1024*1024
    chunkSize = variable.chunkSize
    orignFilePath =  os.path.join(variable.filePath, "测试.docx")
    # 获取文件大小、文件名
    fileSize = os.path.getsize(orignFilePath)
    fileName = os.path.basename(orignFilePath)
    blockNumbers = math.ceil(fileSize / chunkSize)

    print("[文件大小为: %s ,可以分成 %s ]" %(fileSize,blockNumbers))
    # 文件分块后存放的位置
    if not os.path.exists(os.path.join(variable.directory,fileName[0:2])):
       os.mkdir(os.path.join(variable.directory,fileName[0:2]))
    processSplite(orignFilePath,chunkSize,os.path.join(variable.directory,fileName[0:2]))

    print("\033[31;1m文件完成分块...\033[0m")
    print("*"*30)

    return blockNumbers,os.path.join(variable.directory,fileName[0:2])

