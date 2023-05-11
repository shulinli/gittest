import os,sys
import numpy as np
import socketserver
import threading
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ec import variable
from ec import fileBlock
from ec import fileMerge
from ec import fileTransfer
from ec import fileErasure
# from sockets import tcpClient
from sockets import tcpServer

"文件分块"
def splite():
    print("\033[31;1m文件开始分块...\033[0m")
    return fileBlock.splitFile()

"文件合并"
def merge(blockFilePath):
    print("\033[32;1m文件开始合并...\033[0m")
    fileMerge.mergeFile(blockFilePath)

"启动服务器"
def startServer():
    tcp_server = socketserver.ThreadingTCPServer(variable.ip_port, tcpServer.Myserver)
    tcp_server.serve_forever()

"文件传输"
def transfer():
    print("\033[33;1m文件开始传输...\033[0m")
    pass

"块丢失与恢复操作"
def erasure(blockNumbers,checkBlockNums,blockFilePath):
    print("\033[34;1m文件开始恢复...\033[0m")
    fileErasure.erasureCode(blockNumbers,checkBlockNums,blockFilePath)

if __name__ == '__main__':
    start_time = time.time()
    np.set_printoptions(suppress=True)
    # serverThread = threading.Thread(target=startServer)
    # serverThread.start()
    # print("hello")
    blockNumbers,blockFilePath = splite()
    checkBlockNums = int(blockNumbers / 3)
    erasure(blockNumbers,checkBlockNums,blockFilePath)
    merge(blockFilePath)
    #print("spend time",time.time()-start_time)