from mhxy import *


class Shopping:
    mark = True
    hour = 99
    _lastBuyTime = None
    _cooldown = 2
    # meigui suipian
    __mode = 'suipian'

    def __init__(self) -> None:
        init()
        self._lastBuyTime = datetime.datetime.now().timestamp()
        super().__init__()

    def _refresh(self):
        leftTab = winRelativeXY(5, 8.5)
        pyautogui.leftClick(leftTab[0], leftTab[1])
        itemTab = ()
        if self.__mode == "suipian":
            itemTab = winRelativeXY(11, 9)
        elif self.__mode == "meigui":
            itemTab = winRelativeXY(11, 9 + 2.4)
        pyautogui.leftClick(itemTab[0], itemTab[1])

    def _multiSelect(self):
        inputTab = winRelativeXY(15, 13.5)
        pyautogui.leftClick(inputTab[0], inputTab[1])
        numberTab = winRelativeXY(16, 11)
        pyautogui.doubleClick(numberTab[0], numberTab[1])

    def _buy(self):
        buyTab = winRelativeXY(24, 18.5)
        pyautogui.leftClick(buyTab[0], buyTab[1])
        # 如果是多数量的尝试选择最大数量,否则注释
        if self.__mode == "suipian":
            self._multiSelect()

        buy2Tab = winRelativeXY(16, 17)
        pyautogui.leftClick(buy2Tab[0], buy2Tab[1])

    def do(self):
        init()
        while self.mark:
            # 找三次是否有有廉价商品 r'resources/shop/item600.png',r'resources/shop/suipian.png',r'resources/shop/meigui.png',
            itemPic = [r'resources/shop/' + self.__mode + '.png']
            point = None
            for each in itemPic:
                point = pyautogui.locateCenterOnScreen(each, region=(frame.left, frame.top, frame.right, frame.bottom),
                                                       confidence=0.99)
                if point is not None:
                    break
            # if point is None:
            #     point = pyautogui.locateCenterOnScreen(itemPic, region=(frame.left, frame.top, frame.right, frame.bottom),
            #                                            confidence=0.8)
            # 两次都没有刷新列表
            if point is None:
                self._refresh()
            else:
                # 如果有则购买
                pyautogui.leftClick(point.x, point.y)
                self._cooldown = 2
                self._buy()
                noMoney = pyautogui.locateOnScreen(r'resources/shop/no_money.png',
                                                   region=(frame.left, frame.top, frame.right, frame.bottom))
                if noMoney is not None:
                    break
                self._lastBuyTime = datetime.datetime.now().timestamp()
            # 七点停止
            if datetime.datetime.now().hour == self.hour:
                break
            # 20分钟没买到东西
            if datetime.datetime.now().timestamp() - self._lastBuyTime > 60 * 20:
                self._cooldown = 12
            cooldown(self._cooldown)

    def openSop(self):
        cooldown(5)
        Util.leftClick(1, 6)
        cooldown(5)


if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    time.sleep(2)
    print("start task....")
    Shopping().do()
