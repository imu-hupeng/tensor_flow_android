import socketserver
from socketserver import StreamRequestHandler as SRH
from fft_test import fft
from tensorflow_test import *
from numpy import asarray

#socket IP 端口
host = '0.0.0.0'
port = 9999
addr = (host, port)

#socket服务类
class Servers(SRH):
    def handle(self):
        print("got connection from")
        print(self.client_address)
        # self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))
        while True:
            try:
                data = self.request.recv(1280)
                test = data.decode('utf-8')
                print(test)
                test = test.replace("\n", "")
                fft_final = fft(test)#fft函数调用
                data = tf_mul(fft_final)#tensorflow矩阵乘法调用
                # print(asarray(data))
                # print(type(asarray(data).tolist()))
                # print(len(asarray(data).tolist()))
                for element in asarray(data).tolist():
                    for element1 in element:
                        print(element1)
                self.request.send(data)
            except:
                pass
#开启socketservice
print("server is running....")
server = socketserver.ThreadingTCPServer(addr,Servers)
server.serve_forever()
