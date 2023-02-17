from mhxy import *


class Shopping2:
    # 购买总商品数
    _startTime = datetime.datetime.now()
    #  购买时间点 没差3分钟需要至少设置一个
    _timeList = [
        datetime.datetime(_startTime.year, _startTime.month, _startTime.day, 2, 19),
    ]
    # _total = len(_timeList)
    _total = 1
    #  购买成功数量
    _count = 0
    _flag = True

    def __init__(self) -> None:
        init()
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
        confirmTab = (frame.left + relativeX2Act(8), frame.top + relativeY2Act(14))
        # pyautogui.leftClick(confirmTab[0], confirmTab[1])

    def _timeApproach(self):
        now = datetime.datetime.now()
        oldCount = 0
        for time in self._timeList:
            # 三分钟开始刷新页面
            sj = now + datetime.timedelta(minutes=3)
            # 三分钟内
            if now < time and sj > time:
                return True
            elif now > time:
                oldCount += 1
        if oldCount == len(self._timeList):
            # 全部过期
            self._flag = False
        return False

    class _End(Exception):
        pass

    def shopping2(self):
        while self._flag:
            if self._count >= self._total:
                self._flag = False
                break
            while self._timeApproach():
                # 找三次是否有商品
                itemPic = [r'resources/shop/item_2.png']
                point = None
                for each in itemPic:
                    point = pyautogui.locateCenterOnScreen(each, region=(frame.left, frame.top, frame.right, frame.bottom),
                                                           confidence=0.99)
                    if point is not None:
                        break
                # 两次都没有刷新列表
                if point is None:
                    self._refresh()
                else:
                    print("购买商品")
                    # 如果有则购买
                    pyautogui.leftClick(point.x, point.y)
                    self._buy()
                    noMoney = pyautogui.locateOnScreen(r'resources/shop/no_money.png',
                                                       region=(frame.left, frame.top, frame.right, frame.bottom))
                    if noMoney is not None:
                        self._flag = False
                        raise self._End()
                    self._count += 1
                cooldown(2)
            cooldown(30)


if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    init()
    Shopping2().shopping2()
    print("end")
