from mhxy import *

# 非珍品
class Shopping:
    mark = True
    hour = 99
    _lastBuyTime = None
    _cooldown = 10
    categoryPos = winRelativeXY(5, 8.5)
    # meigui suipian jifenquan
    __mode = 'suipian'

    def __init__(self) -> None:
        init()
        self._lastBuyTime = datetime.datetime.now().timestamp()
        super().__init__()

    def _refresh(self):
        pyautogui.leftClick(self.categoryPos[0], self.categoryPos[1])
        itemTab = ()
        if self.__mode == "suipian":
            itemTab = winRelativeXY(11, 9)
        elif self.__mode == "meigui":
            itemTab = winRelativeXY(11, 9 + 2.4)
        elif self.__mode == "jifenquan":
            itemTab = winRelativeXY(11, 13)
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
        if self.__mode in ["suipian", "jifenquan"]:
            self._multiSelect()

        # buy2Tab = winRelativeXY(18.5, 5)
        buy2Tab = winRelativeXY(16, 17)
        pyautogui.leftClick(buy2Tab[0], buy2Tab[1])

    def do(self):
        # 一次刷新购买的次数
        buyCount = 0
        while self.mark and Util.locateCenterOnScreen(r'resources/shop/shop_item.png') is not None:
            # 找三次是否有有廉价商品 r'resources/shop/item600.png',r'resources/shop/suipian.png',r'resources/shop/meigui.png',
            itemPic = [r'resources/shop/' + self.__mode + '.png']
            # itemPic = [r'resources/shop/suipian.png']
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
                buyCount = 0
                cooldown(self._cooldown)
                self._refresh()
            else:
                # 如果有则购买
                pyautogui.leftClick(point.x, point.y)
                self._cooldown = 10
                self._buy()
                buyCount += 1
                if buyCount >= 50:
                    self.mark = False
                    break
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
                self._cooldown = 30

    def openShop(self):
        cooldown(3)
        Util.leftClick(1, 6)
        cooldown(0.3)
        for i in range(0, 3):
            pyautogui.moveTo(winRelativeX(5), winRelativeY(17))
            pyautogui.dragTo(winRelativeX(5), winRelativeY(9), duration=1)
            cooldown(0.3)
        fabao = Util.locateCenterOnScreen("resources/shop/category.png")
        if fabao is not None:
            pyautogui.leftClick(fabao.x, fabao.y)
            cooldown(0.1)
            Util.leftClick(11, 9)
            cooldown(0.2)
            self.categoryPos = (fabao.x, fabao.y)
        cooldown(3)

    def closeShop(self):
        cooldown(1)
        Util.leftClick(-2.5, 3.5)
        cooldown(1)


if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    time.sleep(2)
    print("start task....")
    Shopping().do()
