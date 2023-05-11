import os
import time
import numpy as np

"编码块" #其实就是编码矩阵 不能称之为编码快 编码块就是校验块
def codeBlock(blockNumbers,checkBlockNums):
    # 单位矩阵
    identity = np.identity(blockNumbers,dtype=int)
    # 范德蒙矩阵
    vandermonde = np.ones((checkBlockNums, blockNumbers),dtype=int)
    for i in range(1,checkBlockNums):
        for j in range(blockNumbers):
            vandermonde[i][j] = (i+1)**j
    B = np.vstack((identity, vandermonde))

    return B


"数据块"
def dataBlock(orignFilePath,listdir):
    asi = []
    # 将文字转成ascii
    for item in listdir:
        temp = []
        # 读取每个分块的数据
        fo = open(os.path.join(orignFilePath, item), "rb")
        while True:
            data = fo.read(1024)
            if not data:
                break
            for num in data:
                temp.append(num)
            ''' data = fo.read(1024)
            text = data.decode("utf-8", errors="ignore")
            for item in text:
                # ord将数据转成与之对应的ascii码
                temp.append(ord(item))
            # 文件读取完毕，结束
            if not data:
                break'''
        asi.append(temp)
    # 寻找最长的文件块，以保证每个数据块相同
    maxLength = max([len(l)] for l in asi)
    # 填充数据块用~
    for item in asi:
        if len(item) < maxLength[0]:
            for i in range(maxLength[0] - len(item)):
                item.append(ord("~"))
    # 转成numpy形式
    B = np.array(asi)

    return B

"校验块"
def checkBlock(B,D):
    C = np.dot(B,D)
    
    return C

"文件丢失"
def fileMissing(checkBlockNums,listdir,orignFilePath,B,D,C):
    loseBlock ,loseindex= [],[]
    for i in range(5, -1, -1):
        print("\r数据块即将丢失...%ss" % (i), end=" ")
        time.sleep(0.5)

    # 丢失的数据块(丢失数据块个数在1-checkBlockNumbers之间)
    # for i in range(np.random.randint(1,checkBlockNums)):
    for i in range(2):
        # 保存丢失的数据块
        while True:
            index = np.random.randint(0,len(listdir))#随机丢失
            if index not in loseindex:
                loseindex.append(index)
                loseBlock.append(listdir[index])
                print("\n数据块 %s 已丢失" % loseBlock[i])
                # 删除数据块
                os.remove(os.path.join(orignFilePath, loseBlock[i]))
                break
    print(loseBlock)
        # loseBlock = np.random.randint(0,len(listdir))
    #
    # print("\n删除文件大小..%s"%os.path.getsize(os.path.join(orignFilePath, loseBlock[0])))
    # print(u"\n丢失数据块 \033[31;1m%s \033[0m" % loseBlock[0])
    # 目录删除数据块
    # os.remove(os.path.join(orignFilePath, loseBlock[0]))
    # # 保存丢失的数据块
    # loseIndex.append(loseBlock)

    # 更改B、D、C
    for item in loseBlock:
        index = os.path.splitext(item)[0]
        index = int(index) - 1
        np.delete(B,index,axis=0)
        D[index,:] = 0
        np.delete(C,index,axis=0)

    return loseBlock,B,D,C

"文件恢复"
def fileRecovery(loseBlock,blockNumbers,orignFilePath,B,D,C):
    start_time = time.time()
    restoreData ,i,text= [],0,b""
    # 取编码块以及校验块数据
    B = B[0:blockNumbers,:]
    C = C[0:blockNumbers,:]
    # 对编码块求逆
    invB = np.linalg.inv(B)
    # 恢复数据
    for item in loseBlock:
        start_time2 = time.time()
        index = os.path.splitext(item)[0]
        index = int(index) - 1
        data = np.dot(invB[index],C)
        restoreData.append(data)
        print("spend time1", time.time() - start_time2)
    # 存入文件
    for item in restoreData:
        fi = open(os.path.join(orignFilePath, loseBlock[i]), "wb")
        for data in item:
            # 把int转成bytes
            text +=chr(int(data)).encode("latin1")
            if len(text) == 1024:
                fi.write(text)
                text = b""
        fi.write(text)
        print("\n数据块 %s 已恢复" % loseBlock[i])
        print("spend time", time.time() - start_time)
        i += 1
        fi.close()

"纠删码"
def erasureCode(blockNumbers,checkBlockNums,orignFilePath):
    #start_time = time.time()
    listdir = os.listdir(orignFilePath)
    B = codeBlock(blockNumbers,checkBlockNums)
    D = dataBlock(orignFilePath,listdir)
    C = checkBlock(B, D)
    loseBlock,B,D,C = fileMissing(checkBlockNums,listdir,orignFilePath,B,D,C)
    fileRecovery(loseBlock,blockNumbers,orignFilePath,B,D,C)#根据丢失的块恢复
    #print("spend time",time.time()-start_time)
    print("\033[34;1m文件完成恢复...\033[0m")
    print("*"*30)
