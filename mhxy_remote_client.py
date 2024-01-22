import json
import socket
from datetime import *

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)

BUFFSIZE = 1024

def tcpClient(inData):
    # 创建客户套接字
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        # 尝试连接服务器
        s.connect(("127.0.0.1", 7367))
        # s.connect(("192.168.222.132", 7368))
        # s.connect(("rdp.bonelf.com", 35671))
        log('连接服务成功！！')
        # 通信循环
        # 发送数据到服务器
        s.send(inData.encode())
        log('发送成功！')

        # 接收返回数据
        outData = s.recv(1024)
        log(f'返回数据信息：{outData}')
        s.close()

# 向虚拟机追加商品购买
if __name__ == '__main__':
    now = datetime.now()
    _startTime = datetime(now.year, now.month, now.day, 3, 9)
    _timeList = [
        (2, 29),
        (0, 57),
        (3, 38),
        (2, 26),
        (2, 48),
        (0, 59),
        (3, 54),
        (1, 14),
        (2, 39),
    ]
    datetimeList=[]
    for each in _timeList:
        datetimeList.append(_startTime + timedelta(hours=each[0], minutes=each[1]))
    data = json.dumps({"datetimeList": datetimeList}, cls=DateEncoder)
    for each in json.loads(data)["datetimeList"]:
        log(datetime.strptime(each, "%Y-%m-%d %H:%M:%S"))
    tcpClient(data)

    # tcpClient(json.dumps({"action": "relogin"}))

    # tcpClient(json.dumps({"action": "do520"}))
