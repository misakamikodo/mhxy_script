from mhxy_fuben import *
from mhxy_ghost import *
from mhxy_shopping2 import *

_520Thread = None


def httpServer():
    global _520Thread
    listen_sock = socket.socket()
    listen_sock.bind(('0.0.0.0', 7368))
    listen_sock.listen(10)
    body = 'Hi你好'

    while True:
        conn, addr = listen_sock.accept()
        req = conn.recv(1024).decode('utf-8')
        log('received ', str(req), 'from', conn.getpeername())
        if req == '':
            request = None
        else:
            request = parse_request(req)
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain;charset=utf-8\r\nContent-Length: ' \
                   '{length}\r\n\r\n{body}'.format(length=len(body.encode("utf-8")), body=body)
        conn.sendall(response.encode('utf-8'))
        conn.close()
        if request is not None and request["url"].startswith('/do520') and _520Thread is None:
            _520Thread = threading.Thread(target=do520, daemon=True)
            _520Thread.start()


def tcpServer():
    global _520Thread
    with socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM) as s:  # AF_INET表示socket网络层使用IP协议，SOCK_STREAM表示socket传输层使用tcp协议
        # 绑定服务器地址和端口
        s.bind(("0.0.0.0", 7368))
        # 启动服务监听
        s.listen(10)
        log('等待用户接入……')
        while True:
            # 等待客户端连接请求,获取connSock
            conn, addr = s.accept()
            log('远端客户:{} 接入系统！！！'.format(addr))
            # with conn:
            log('接收请求信息……')
            # 接收请求信息
            data = conn.recv(1024)
            try:
                if not data:
                    log('frp 服务 ping')
                    continue
                info = data.decode()
                action = json.loads(info)["action"]
                if action.startswith('do520') and _520Thread is None:
                    _520Thread = threading.Thread(target=do520, daemon=True)
                    _520Thread.start()
                if action.startswith('relogin'):
                    Shopping2().relogin()
                # 发送请求数据
                conn.send(f'{info}'.encode())
                log('发送返回完毕！！！')
            except UnicodeEncodeError:
                pass
            finally:
                conn.close()
        s.close()

def do520():
    global _520Thread
    log("start 520....")
    fuben = Fuben(idx=0)
    fuben.fubenPos = [
        # ("xiashi", 13, 15),
        ("xiashi", 7, 15),

        ("norm", 19, 15),
        ("norm", 13, 15),
        ("norm", 7, 15)
    ]

    fuben.loginIn()

    fuben.do()

    ghost = Ghost(idx=0)
    ghost.maxRound = 5
    ghost.chasepos = 1
    ghost.go()
    ghost.do()
    _520Thread = None


# 远程520
if __name__ == '__main__':
    tcpServer()
