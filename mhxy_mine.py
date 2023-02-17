from mhxy import *


class _MinePoint:
    wait = 10
    pic = 10
    offsetY = 0

    def __init__(self, wait, pic, offsetY=20):
        self.wait = wait
        self.pic = pic
        self.offsetY = offsetY
        pass


# 矿图列表
_normMineList = [
    # 矿
    _MinePoint(3, r'resources/mine/norm_purple_shade_mine.png'),
    _MinePoint(3, r'resources/mine/norm_purple_mine.png'),
    _MinePoint(5, r'resources/mine/norm_blue_mine.png'),
    _MinePoint(5, r'resources/mine/norm_blue_shade_mine.png'),

    # _MinePoint(7, r'resources/mine/norm_green_mine.png'),
    # MinePoint(7, r'resources/mine/norm_green_shade_mine.png'),

    # MinePoint(10, r'resources/mine/norm_grey_mine.png'),
    # MinePoint(10, r'resources/mine/norm_grey_shade_mine.png')
    # 采集
    # _MinePoint(8, r'resources/mine/norm_cao.png', 20),
]


# 关闭花果小地图
def _closeSmallMap(type):
    if type == "daxue":
        pos = (frame.right - relativeX2Act(7),
               frame.top + relativeY2Act(6))
    else:
        pos = (frame.right - relativeX2Act(7.8),
               frame.top + relativeY2Act(3.8))
    pyautogui.leftClick(pos[0],
                        pos[1])


class _StandPoint:
    mineList = _normMineList

    def move2Point(self):
        pass


class _FstStandPoint(_StandPoint):
    relativeX = 0
    relativeY = 0
    mineList = []

    def __init__(self, x, y, map="huaguo", cooldown=4, mineList=None):
        self.map = map
        self.relativeX = x
        self.relativeY = y
        self.cooldown = cooldown
        if mineList is None:
            self.mineList = _normMineList
        else:
            self.mineList = mineList

    def move2Point(self):
        self.newDayCloseDiag()
        # 打开大地图
        posBigMap = (frame.left + relativeX2Act(1),
                     frame.top + relativeY2Act(2))
        print("click bigMap", posBigMap)
        pyautogui.leftClick(posBigMap[0],
                            posBigMap[1])
        # 选择花果山
        posMap = None
        if self.map == "huaguo":
            posMap = (bigMap.right - relativeX2Act(1.5),
                      bigMap.top + relativeY2Act(5))
            print("click 花果山", posMap)
        elif self.map == "daxue":
            posMap = (bigMap.left + relativeX2Act(11.5),
                      bigMap.top + relativeY2Act(2.5))
        pyautogui.leftClick(posMap[0],
                            posMap[1])
        # self.newDayCloseDiag()
        # 打开小地图
        posSmallMap = (frame.left + relativeX2Act(3.5),
                       frame.top + relativeY2Act(2))
        pyautogui.leftClick(posSmallMap[0],
                            posSmallMap[1])
        # 选择右上部分的点
        posMove = winRelativeXY(self.relativeX, self.relativeY)
        pyautogui.leftClick(posMove[0],
                            posMove[1])
        _closeSmallMap(self.map)
        closeMission()
        cooldown(self.cooldown)

    def newDayCloseDiag(self):
        def do(newDay):
            if newDay is None:
                return
            pyautogui.leftClick(newDay.x, newDay.y)
            cooldown(1)
            Util.leftClick(-1, -3)

            def scroll2Lingshifu(locate, idx):
                pyautogui.moveTo(winRelativeX(-9), winRelativeY(-4.9))
                pyautogui.dragTo(winRelativeX(-9), winRelativeY(6.7), duration=1)
                cooldown(0.2)

            locate, idx = doUtilFindPic(r'resources/mine/lingshifu.png', scroll2Lingshifu)
            if locate is not None:
                pyautogui.leftClick(locate.x, locate.y)
                cooldown(0.2)
                Util.leftClick(11, 13)
                cooldown(0.7)
                # pyautogui.leftClick(newDay.x, newDay.y)
                Util.leftClick(-1.5, 4)
                cooldown(0.2)
                Util.leftClick(-2.5, 3.7)
                cooldown(0.7)
        newDayCloseCheck(do)


class _NormStandPoint(_StandPoint):
    # 相对小地图的位置
    relativeX = 0
    relativeY = 0
    map = "huaguo"

    def __init__(self, x, y, cooldown=6, map="huaguo", mineList=None):
        self.relativeX = x
        self.relativeY = y
        self.map = map
        self.cooldown = cooldown
        if mineList is None:
            self.mineList = _normMineList
        else:
            self.mineList = mineList

    def move2Point(self):
        # 打开小地图
        posSmallMap = (frame.left + relativeX2Act(3.5),
                       frame.top + relativeY2Act(2))
        pyautogui.leftClick(posSmallMap[0],
                            posSmallMap[1])
        # 选择右上部分随意点
        posMove = winRelativeXY(self.relativeX, self.relativeY)
        pyautogui.leftClick(posMove[0],
                            posMove[1])
        _closeSmallMap(self.map)
        cooldown(self.cooldown)


# 所有定义站立点
_standPoints = (
    _FstStandPoint(
        -9, 10.5, map="huaguo", cooldown=4
    ),
    _NormStandPoint(
        12.5, 9, cooldown=5
    ),
    _NormStandPoint(
        18.5, -5.5, cooldown=9
    ),
    _NormStandPoint(
        10, -5, cooldown=7
    ),
    _NormStandPoint(
        10, 14, cooldown=3
    ),
    # 采集
    # _FstStandPoint(
    #     11, 8.5, map="daxue", cooldown=8
    # ),
    # _NormStandPoint(
    #     14, 10.5, map="daxue", cooldown=8
    # ),
    # _NormStandPoint(
    #     -9.5, 8.5, map="daxue", cooldown=8
    # ),
    # _NormStandPoint(
    #     16.5, 12, map="daxue", cooldown=8
    # ),
    # _NormStandPoint(
    #     9.5, 13.5, map="daxue", cooldown=8
    # ),
    # _NormStandPoint(
    #     17.5, 15, map="daxue", cooldown=8
    # )
)

# 小地图
_smallMap = Frame(0, 0)


def _initForMine():
    pyautogui.PAUSE = 0.3
    _smallMap.left = frame.left + relativeX2Act(7.5)
    _smallMap.top = frame.top + relativeY2Act(3.7)
    _smallMap.right = frame.right - relativeX2Act(7.5)
    _smallMap.bottom = frame.bottom - relativeY2Act(2.8)
    print("init smallMap:", _smallMap)


def _changeMapPos(mapPos):
    _standPoints[mapPos % len(_standPoints)].move2Point()
    return _standPoints[mapPos % len(_standPoints)]


class Mine:
    __lastMineTime = datetime.datetime.now().timestamp()
    mark = True

    def __init__(self) -> None:
        super().__init__()
        init(resizeToNice=False)
        _initForMine()
        self.__lastMineTime = datetime.datetime.now().timestamp()

    def _mining(self, mineList=None):
        def waitMoveOk():
            mineSelect = pyautogui.locateCenterOnScreen(r'resources/mine/mine_select.png',
                                                        region=(frame.left, frame.top, frame.right, frame.bottom),
                                                        confidence=0.96)
            if mineSelect is not None:
                pyautogui.leftClick(mineSelect.x, mineSelect.y)
            collect = None
            count = 0
            while collect is None:
                if count > 10:
                    return False
                cooldown(1)
                collect = pyautogui.locateCenterOnScreen(r'resources/mine/collect.png',  # collect_caiji
                                                         region=(frame.left, frame.top, frame.right, frame.bottom),
                                                         confidence=0.8)
                count += 1
            return True

        if mineList is None:
            mineList = _normMineList
        # 等待时间 点位信息
        count = 0
        while count < len(mineList):
            for mine in mineList:
                point = pyautogui.locateCenterOnScreen(mine.pic,
                                                       region=(frame.left, frame.top, frame.right, frame.bottom),
                                                       confidence=0.96)
                if point is not None:
                    print("发现矿：", mine.pic)
                    p = (mine.wait, point.x, point.y)
                    # 点击矿
                    pyautogui.leftClick(point.x, point.y - mine.offsetY)  # -20 采集
                    res = waitMoveOk()
                    if res and point.y > frame.top + relativeY2Act(3):
                        # 点击挖
                        self.__lastMineTime = datetime.datetime.now().timestamp()
                        posMove = (frame.right - relativeX2Act(5),
                                   frame.bottom - relativeY2Act(3.5))
                        pyautogui.leftClick(posMove[0],
                                            posMove[1])
                        count += 1
                        # 根据颜色等待 3-5-7-10 秒
                        if p[0] == -1:
                            pyautogui.click(frameSize[0] / 2, frameSize[1] / 2, clicks=10, duration=0.08,
                                            button=pyautogui.LEFT)
                        else:
                            cooldown(p[0] + 1)
                else:
                    count += 1

    def mineMain(self):
        mapPos = 0
        standPoint = _changeMapPos(mapPos)
        # 没有改变过位置
        notChange = True
        while self.mark:
            self._mining(standPoint.mineList)
            # mine = mining()
            now = datetime.datetime.now()
            minute = now.minute
            second = now.second
            # 修改位置
            if minute % 5 == 0 and second > 10 and notChange:
                mapPos = 0
                standPoint = _changeMapPos(mapPos)
                notChange = False
            elif mapPos < 2 * len(_standPoints) - 1:
                mapPos += 1
                standPoint = _changeMapPos(mapPos)
            else:
                notChange = True
            cooldown(2)
            # 30 分钟没挖到矿 跳出循环
            if datetime.datetime.now().timestamp() - self.__lastMineTime > 60 * 16:
                self.mark = False


# 大窗口
if __name__ == '__main__':
    time.sleep(2)
    print("start task....")
    Mine().mineMain()
    # 挖完矿关机

    print("结束挖矿")
