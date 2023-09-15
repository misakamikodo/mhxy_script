import socket

from mhxy import *


# 收宝宝胚子
class Shopping2:
    # 购买总商品数
    _startTime = None
    #  购买时间点 没差3分钟需要至少设置一个
    _timeList = [
    ]
    __mostOldTime = None
    _datetimeList = [
    ]
    # 购买成功数量
    _count = 0
    # 运行标识
    _flag = True

    def __init__(self) -> None:
        init()
        now = datetime.datetime.now()
        self._startTime = datetime.datetime(now.year, now.month, now.day, 0, 25)
        # TODO
        self._timeList = [
            (3, 38),
        ]
        for each in self._timeList:
            dt = self._startTime + datetime.timedelta(hours=each[0], minutes=each[1])
            self._datetimeList.append(dt)
            print(format(dt))
        if len(self._datetimeList) > 0:
            self.__mostOldTime = max(self._datetimeList)
        super().__init__()

    def openSop(self):
        cooldown(2)
        Util.leftClick(1, 6)
        cooldown(2)

    def close(self):
        cooldown(2)
        Util.leftClick(-2.5, 3.5)
        cooldown(2)

    def _refresh(self):
        leftTab = (frame.left + relativeX2Act(5), frame.top + relativeY2Act(8.5))
        pyautogui.leftClick(leftTab[0], leftTab[1])

    def _buy(self):
        buyTab = (frame.right - relativeX2Act(5), frame.bottom - relativeY2Act(3))
        pyautogui.leftClick(buyTab[0], buyTab[1])
        # confirmTab = (frame.left + relativeX2Act(13.5), frame.top + relativeY2Act(8.5))
        confirmTab = (frame.left + relativeX2Act(8), frame.top + relativeY2Act(14))
        pyautogui.leftClick(confirmTab[0], confirmTab[1])

    def _timeApproach(self):
        now = datetime.datetime.now()
        oldArr = []
        for time in self._datetimeList:
            # 三分钟开始刷新页面
            sj1 = now - datetime.timedelta(minutes=2)
            sj2 = now + datetime.timedelta(minutes=2)
            # 三分钟内
            if sj1 < time and sj2 > time:
                return time
            elif now > sj2:
                oldArr.append(time)
        return None

    def __tcpServer(self):  # TCP服务
        with socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM) as s:  # AF_INET表示socket网络层使用IP协议，SOCK_STREAM表示socket传输层使用tcp协议
            # 绑定服务器地址和端口
            s.bind(("0.0.0.0", 7368))
            # 启动服务监听
            s.listen(10)
            print('等待用户接入……')
            while True:
                # 等待客户端连接请求,获取connSock
                conn, addr = s.accept()
                print('远端客户:{} 接入系统！！！'.format(addr))
                conn.send(json.dumps({"startTime": self._startTime}, cls=DateEncoder).encode())
                # with conn:
                print('接收请求信息……')
                # 接收请求信息
                data = conn.recv(1024)
                try:
                    if not data:
                        print('err not data (花生壳在ping)')
                        continue
                    info = data.decode()
                    jsonData = json.loads(info)
                    datetimeList = jsonData.get("datetimeList")
                    if datetimeList is not None:
                        for each in datetimeList:
                            self._datetimeList.append(datetime.datetime.strptime(each, "%Y-%m-%d %H:%M:%S"))
                        self.__mostOldTime = max(self._datetimeList)
                    elif jsonData.get("action") == "relogin":
                        self.relogin()
                    # 发送请求数据
                    conn.send(f'{info}'.encode())
                    print('发送返回完毕！！！')
                finally:
                    conn.close()
            s.close()

    def relogin(self):
        cooldown(1)
        Util.leftClick(14, 12.5)
        cooldown(5)
        Util.leftClick(14, 11.7)
        cooldown(5)
        Util.leftClick(14, 15)
        cooldown(5)
        self.openSop()
        Util.leftClick(26.5, 10)

    def shopping2(self):
        threading.Thread(target=self.__tcpServer, daemon=True).start()

        while self._flag:
            if self.__mostOldTime is not None and datetime.datetime.now() >= self.__mostOldTime:
                print("全部过期")
                print(self.__mostOldTime)
                self._flag = False
                break
                # cooldown(30)
                # continue
            # 被挤掉线
            # if Util.locateCenterOnScreen(r'resources/origin/offline.png') is not None:
            #     break
            time = self._timeApproach()
            while time is not None:
                # 找三次是否有商品
                itemPic = [r'resources/shop/item_2.png']
                point = None
                for each in itemPic:
                    point = Util.locateCenterOnScreen(each, confidence=0.99)
                    if point is not None:
                        break
                # 两次都没有刷新列表
                if point is None:
                    self._refresh()
                else:
                    print("购买商品", datetime.datetime.now())
                    # 如果有则购买
                    pyautogui.leftClick(point.x, point.y)
                    self._buy()
                    noMoney = pyautogui.locateOnScreen(r'resources/shop/no_money.png',
                                                       region=(frame.left, frame.top, frame.right, frame.bottom))
                    if noMoney is not None:
                        print("没钱了")
                        self._flag = False
                    else:
                        cooldown(5)
                        self._refresh()
                        # 会只删除第一个出现的
                        self._datetimeList.remove(time)
                    self._count += 1
                cooldown(2)
                time = self._timeApproach()
            cooldown(30)


if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    init()
    Shopping2().shopping2()
    print("end")
