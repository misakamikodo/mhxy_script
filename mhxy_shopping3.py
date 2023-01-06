import datetime

from mhxy import *

now = datetime.datetime.now()


class Shopping2:
    _time = datetime.datetime(now.year, now.month, now.day, 2, 25)

    def _refresh(self):
        # TODO
        leftTab = (frame.left + relativeX2Act(5), frame.top + relativeY2Act(8.5))
        pyautogui.leftClick(leftTab[0], leftTab[1])
        leftTab = (frame.left + relativeX2Act(5), frame.top + relativeY2Act(8.5))
        pyautogui.leftClick(leftTab[0], leftTab[1])

    def _buy(self):
        buyTab = (frame.right - relativeX2Act(5), frame.bottom - relativeY2Act(3))
        pyautogui.leftClick(buyTab[0], buyTab[1])
        confirmTab = (frame.left + relativeX2Act(8), frame.top + relativeY2Act(14))
        pyautogui.leftClick(confirmTab[0], confirmTab[1])

    def _timeApproach(self):
        # 三分钟开始刷新页面
        sj = now + datetime.timedelta(minutes=3)
        if now < self._time and sj > self._time:
            return True
        return False

    class _End(Exception):
        pass

    def shopping2(self):
        while True:
            while self._timeApproach():
                # 找三次是否有商品
                itemPic = r'resources/shop/item_2.png'
                point = pyautogui.locateCenterOnScreen(itemPic,
                                                       region=(frame.left, frame.top, frame.right, frame.bottom),
                                                       confidence=0.95)
                # 两次都没有刷新列表
                if point is None:
                    self._refresh()
                else:
                    print("购买商品")
                    # 如果有则购买
                    pyautogui.leftClick(point.x, point.y)
                    self._buy()
                    raise self._End()
                cooldown(2)
            cooldown(60)

# 不关注、靠搜索抢
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    init()
    Shopping2().shopping2()
