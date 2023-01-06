import sys
import datetime as dt
from configparser import ConfigParser
import os
import playsound as pl
import threading

from pyautogui import FailSafeException

from mhxy import *


class Ghost:
    maxRound = 99
    _flag = True
    __count = 0
    _startTimestamp = None
    __chaseWin = None
    __chasepos = 1
    __doublePointNumPer200 = 1

    def __init__(self, picNo=0) -> None:
        conn = ConfigParser()
        file_path = os.path.join(os.path.abspath('.'), 'resources/ghost/ghost.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")
        conn.read(file_path)
        chasepos = int(conn.get('main', 'chasepos'))
        maxRound = int(conn.get('main', 'maxRound'))
        doublePointNumPer200 = int(conn.get('main', 'doublePointNumPer200'))
        resize = bool(int(conn.get('main', 'resize')))
        if chasepos is not None:
            print("读取配置：任务位置为：" + str(chasepos))
            self.__chasepos = chasepos - 1
        if maxRound is not None:
            print("读取配置：捉鬼轮数为：" + str(maxRound))
            self.maxRound = maxRound
        if doublePointNumPer200 is not None:
            print("读取配置：领双数为：" + str(doublePointNumPer200))
            self.__doublePointNumPer200 = doublePointNumPer200
        print("读取配置：调整窗口大小：" + str(resize))

        init(int(picNo), resizeToNice=resize)  # True

        self.__chaseWin = (winRelativeX(-1), winRelativeY(6 + 2 * self.__chasepos))
        super().__init__()

    def getDialog(self):
        cooldown(1)
        Util.leftClick(7.5, 1.5)
        cooldown(1)
        Util.leftClick(3, 5)
        cooldown(2)
        mission = Util.locateCenterOnScreen(r'resources/ghost/mission.png')
        if mission is not None:
            cooldown(3)
            pyautogui.leftClick(mission.x + relativeX2Act(3.5), mission.y + relativeY2Act(0.2))

    def getPoint(self):
        cooldown(2)
        Util.doubleClick(11, 1.5)
        cooldown(2)
        for each in range(0, self.__doublePointNumPer200):
            Util.leftClick(20, 16)
        cooldown(2)
        Util.doubleClick(23, 3.5)
        cooldown(2)
        pass

    def _startMission(self, location):
        # 领任务
        pyautogui.leftClick(location.x, location.y)
        # 校验双倍 self.__count % 25 == 0
        if self.__count % 25 == 0 and self.__doublePointNumPer200 != -1:
            self.getPoint()
        # +3 整点第二个任务
        print("关闭对话框 ", self.__chaseWin)
        cooldown(1)
        five = Util.locateOnScreen(r'resources/ghost/team_not_full.png')
        if five is not None:
            # 按取消
            pyautogui.leftClick(five.left + five.width - 120, five.top + five.height - 20)
        # 关对话 + 追踪
        pyautogui.click(self.__chaseWin[0], self.__chaseWin[1], clicks=2, button=pyautogui.LEFT)

    def __newDayCloseDiagDo(self, newDay):
        pyautogui.leftClick(newDay.x, newDay.y)
        cooldown(1)
        Util.leftClick(-1, -3)
        # self.__chasepos += 1

    def ghost(self):
        # _thread.start_new_thread(resumeIfDisconnect, ("Thread-1", 2,))
        def initStartLocation():
            return Util.locateCenterOnScreen('resources/ghost/start_ghost0.png')

        while self._flag:
            # 是否继续捉鬼弹窗 虽然使用确定即可，但是截图截得长了，所以locateOnScreen获取相对截图右下点的位置
            completeLocation = Util.locateOnScreen('resources/ghost/complete_ghost0.png')
            startLocation = None
            newDayCloseCheck(self.__newDayCloseDiagDo)

            if completeLocation is None:
                # 对话框：捉鬼任务选项。
                startLocation = initStartLocation()

            if completeLocation is not None:
                # 选择继续捉鬼
                pyautogui.leftClick(completeLocation.left + completeLocation.width - 50,
                                    completeLocation.top + completeLocation.height - 20)
                startLocation = initStartLocation()
                print("结束抓鬼 ", completeLocation)
            if startLocation is not None:
                self.__count += 1
                print("已完成抓鬼" + str(self.__count) + "轮数")
                if self.__count > self.maxRound:
                    self._flag = False
                else:
                    self._startMission(startLocation)
                    self._startTimestamp = dt.datetime.now()
                    print("开始抓鬼 ", startLocation)
                    cooldown(5 * 60)
                if self.__count % 25 == 0:
                    print("完成一千双")
                    # pl.playsound('resources/common/music.mp3')
            # 二十分钟没有下一轮 怀疑掉线
            if self._startTimestamp is not None and (dt.datetime.now() - self._startTimestamp).seconds > 20 * 60:
                Util.leftClick(self.__chaseWin[0], self.__chaseWin[1])
                naozhong = threading.Thread(target=pl.playsound('resources/common/music.mp3'))
                # 闹钟提醒
                naozhong.start()
            cooldown(2)


# 小窗口 pyinstaller -F mhxy_ghost.py
if __name__ == '__main__':
    picNo = 0 if len(sys.argv) <= 1 else sys.argv[1]
    pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
    pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
    try:
        Ghost(picNo=picNo).ghost()
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
