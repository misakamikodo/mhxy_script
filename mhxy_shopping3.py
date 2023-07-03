from mhxy import *

class Shopping3:
    _approached = False
    _startTime = datetime.datetime.now()
    _time = datetime.datetime(_startTime.year, _startTime.month, _startTime.day, 3, 38)

    def __init__(self) -> None:
        init()
        super().__init__()

    def _refresh(self):
        cooldown(0.2)
        Util.leftClick(5, 7)
        cooldown(0.2)
        Util.leftClick(23, 18.5)

    def _buy(self):
        print("购买商品")
        cooldown(0.1)
        buyTab = (frame.right - relativeX2Act(5), frame.bottom - relativeY2Act(3))
        pyautogui.leftClick(buyTab[0], buyTab[1])
        cooldown(0.1)
        # confirmTab = (frame.left + relativeX2Act(13.5), frame.top + relativeY2Act(8.5))
        confirmTab = (frame.left + relativeX2Act(8), frame.top + relativeY2Act(14))
        pyautogui.leftClick(confirmTab[0], confirmTab[1])

    def _timeApproach(self):
        now = datetime.datetime.now()
        # 三分钟开始刷新页面
        sj1 = now - datetime.timedelta(minutes=2)
        sj2 = now + datetime.timedelta(minutes=1)
        # 三分钟内
        if sj1 < self._time and sj2 > self._time:
            self._approached=True
            return True
        return False

    def close(self):
        cooldown(2)
        Util.leftClick(-2.5, 3.5)
        cooldown(2)

    class _End(Exception):
        pass

    def shopping3(self):
        while True:
            while self._timeApproach():
                # 找三次是否有商品
                itemPic = r'resources/shop/item_2.png'
                point = Util.locateCenterOnScreen(itemPic)
                # 两次都没有刷新列表
                if point is None:
                    self._refresh()
                else:
                    # 如果有则购买
                    pyautogui.leftClick(point.x, point.y)
                    self._buy()
                    break
                cooldown(1.5)
            if self._approached:
                break
            cooldown(60)

# 不关注、靠搜索抢
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    # pyautogui.PAUSE = 2
    print("start task....")
    Shopping3().shopping3()
