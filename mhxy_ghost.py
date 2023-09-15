import datetime as dt
import os
import sys
from configparser import ConfigParser

from pyautogui import FailSafeException

from mhxy import *


class Ghost(MhxyScript):
    maxRound = 99
    _count = 0
    _startTimestamp = None
    _chaseWin = None
    # 任务位置
    chasepos = 1
    # 自动领双数
    _doublePointNumPer100 = -1
    warnMinute = 25
    _battleTimeTick = datetime.datetime.now()

    def __init__(self, idx=0, changWinPos=True) -> None:
        conn = ConfigParser()
        file_path = os.path.join(os.path.abspath('.'), 'resources/ghost/ghost.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")
        conn.read(file_path)
        chasepos = float(conn.get('main', 'chasepos'))
        maxRound = int(conn.get('main', 'maxRound'))
        doublePointNumPer100 = int(conn.get('main', 'doublePointNumPer100'))
        resize = bool(int(conn.get('main', 'resize')))
        warnMinute = int(conn.get('main', 'warnMinute'))
        if chasepos is not None:
            print("读取配置：任务位置为：" + str(chasepos))
            self.chasepos = chasepos
        if maxRound is not None:
            print("读取配置：捉鬼轮数为：" + str(maxRound))
            self.maxRound = maxRound
        if warnMinute is not None:
            print("读取配置：报警时间为：" + str(warnMinute))
            self.warnMinute = warnMinute
        if doublePointNumPer100 is not None:
            print("读取配置：领双数为：" + str(doublePointNumPer100))
            self._doublePointNumPer100 = doublePointNumPer100
        print("读取配置：调整窗口大小：" + str(resize))

        self._chaseWin = (-1, 3.5)
        super().__init__(idx=int(idx), resizeToSmall=resize, changWinPos=changWinPos)

    def _chaseWinFix(self):
        fix = 2 * self.chasepos
        return fix

    def getDialog(self):
        cooldown(1)
        Util.leftClick(7.5, 1.5)
        cooldown(1)
        Util.leftClick(3, 4.5)
        cooldown(2)
        mission = Util.locateCenterOnScreen(r'resources/ghost/mission.png')
        i = 0
        while mission is None and i in range(0, 2):
            pyautogui.moveTo(winRelativeX(10), winRelativeY(12.5))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)
            cooldown(1)
            mission = Util.locateCenterOnScreen(r'resources/ghost/mission.png')
            i += 1
        if mission is not None:
            cooldown(1)
            pyautogui.leftClick(mission.x + relativeX2Act(3.5), mission.y + relativeY2Act(0.2))

    def getPoint(self):
        cooldown(2)
        Util.leftClick(11, 1.5)
        cooldown(2)
        for each in range(0, self._doublePointNumPer100):
            Util.leftClick(20, 16)
            cooldown(0.2)
        cooldown(2)
        Util.leftClick(23, 3.5)
        cooldown(2)
        pass

    def _startMission(self, location):
        # 领任务
        pyautogui.leftClick(location.x, location.y)
        # +3 整点第二个任务
        print("关闭对话框 ", self._chaseWin)
        cooldown(1)
        five = Util.locateOnScreen(r'resources/ghost/team_not_full.png')
        if five is not None:
            # 按取消
            pyautogui.leftClick(five.left + five.width - 120, five.top + five.height - 20)
        # 校验双倍 self.__count % 25 == 0
        if self._count % 25 == 0 and self._doublePointNumPer100 != -1:
            Util.leftClick(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix())
            cooldown(0.2)
            self.getPoint()
            Util.leftClick(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix())
        else:
            # 关对话 + 追踪
            Util.click(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix(), clicks=2, buttons=pyautogui.LEFT)

    def _newDayCloseDiagDo(self, newDay):
        if newDay is None:
            return
        pyautogui.leftClick(newDay.x, newDay.y)
        cooldown(1)
        Util.leftClick(-1, -3)

    def go(self):
        cooldown(1)
        Util.leftClick(6.8, 1.5)
        cooldown(0.5)
        Util.leftClick(3, 4.7)
        cooldown(1)
        tag = Util.locateCenterOnScreen('resources/ghost/activity_tag.png')
        i = 0
        while tag is None and i in range(0, 2):
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)
            cooldown(1.5)
            tag = Util.locateCenterOnScreen('resources/ghost/activity_tag.png')
            i += 1
        if tag is not None:
            cooldown(1)
            pyautogui.leftClick(tag.x + relativeX2Act(3.5), tag.y + relativeY2Act(0.2))

    def _startGhostDo(self):
        cooldown(5 * 60)

    def do(self):
        # _thread.start_new_thread(resumeIfDisconnect, ("Thread-1", 2,))
        def initStartLocation():
            return Util.locateCenterOnScreen('resources/ghost/start_ghost0.png')

        while self._flag:
            # 战斗标识
            battleLoc = Util.locateOnScreen('resources/small/enter_battle_flag.png')
            if battleLoc is not None:
                self._battleTimeTick = datetime.datetime.now()

            # 上次战斗结束时间相差2分钟
            if (datetime.datetime.now() - self._battleTimeTick).seconds > 60 * 2:
                Util.leftClick(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix())
                cooldown(10)

            # 是否继续捉鬼弹窗 虽然使用确定即可，但是截图截得长了，所以locateOnScreen获取相对截图右下点的位置
            completeLocation = Util.locateOnScreen('resources/ghost/complete_ghost0.png')
            startLocation = None

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
                self._count += 1
                print("已完成抓鬼" + str(self._count) + "轮数")
                if self._count > self.maxRound:
                    self._flag = False
                    # pl.playsound('resources/common/music.mp3')
                else:
                    self._startMission(startLocation)
                    self._startTimestamp = dt.datetime.now()
                    print("开始抓鬼 ", startLocation)
                    self._startGhostDo()
                if self._count % 25 == 0:
                    print("完成一千双")
                    pl.playsound('resources/common/music.mp3')
            # 二十分钟没有下一轮 怀疑掉线
            if self._startTimestamp is not None and (dt.datetime.now() - self._startTimestamp).seconds > self.warnMinute * 60:
                Util.leftClick(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix())
                naozhong = threading.Thread(target=pl.playsound('resources/common/music.mp3'))
                # 闹钟提醒
                naozhong.start()
            cooldown(2)


# 小窗口 pyinstaller -F mhxy_ghost.py
if __name__ == '__main__':
    idx = 0 if len(sys.argv) <= 1 else sys.argv[1]
    pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
    pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
    try:
        Ghost(idx=idx).do()
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
