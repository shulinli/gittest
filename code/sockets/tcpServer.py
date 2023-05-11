import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print("服务器启动...")
        while True:
            try:
                msg = self.request.recv(1024)
                print("clien[%s]>>%s"%(self.client_address,msg.decode("utf-8")))
                self.request.sendall(msg.upper())
            except Exception as e:
                if hasattr(e,"reason"):
                    print(e.reason)

