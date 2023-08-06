from mhxy_mine import *


class MineWithShop(Mine):
    _lastMineTime = datetime.datetime.now().timestamp()
    mark = True

    def shop(self):
        cooldown(1)
        Util.leftClick(1, 6)
        cooldown(1.5)
        hasItem = True
        count = 0
        while hasItem and count in range(0, 20):
            # 找三次是否有有廉价商品 r'resources/shop/item600.png',r'resources/shop/suipian.png',r'resources/shop/meigui.png',
            itemPic = [r'resources/shop/' + 'suipian' + '.png']
            point = None
            for each in itemPic:
                point = pyautogui.locateCenterOnScreen(each, region=(frame.left, frame.top, frame.right, frame.bottom),
                                                       confidence=0.99)
                if point is not None:
                    break
            # 两次都没有刷新列表
            if point is not None:
                # 如果有则购买
                pyautogui.leftClick(point.x, point.y)
                self._cooldown = 2

                buyTab = winRelativeXY(24, 18.5)
                pyautogui.leftClick(buyTab[0], buyTab[1])
                # 如果是多数量的尝试选择最大数量,否则注释
                inputTab = winRelativeXY(15, 13.5)
                pyautogui.leftClick(inputTab[0], inputTab[1])
                numberTab = winRelativeXY(16, 11)
                pyautogui.doubleClick(numberTab[0], numberTab[1])

                buy2Tab = winRelativeXY(16, 17)
                pyautogui.leftClick(buy2Tab[0], buy2Tab[1])
            else:
                hasItem = False
        cooldown(1)
        Util.leftClick(-2.5, 3.5)
        cooldown(1)

    def do(self):
        mapPos = 0
        standPoint = self._changeMapPos(mapPos)
        # 没有改变过位置
        notChange = True
        shop = False
        while self.mark:
            self._mining(standPoint.mineList)
            # mine = mining()
            now = datetime.datetime.now()
            minute = now.minute
            second = now.second
            # 修改位置
            if minute % 5 == 0 and second > 10 and notChange:
                mapPos = 0
                standPoint = self._changeMapPos(mapPos)
                shop = False
                notChange = False
            elif mapPos < 2 * len(self._standPoints) - 1:
                mapPos += 1
                standPoint = self._changeMapPos(mapPos)
            elif not shop:
                shop = True
                self.shop()
            else:
                notChange = True
            cooldown(2)
            # 30 分钟没挖到矿 跳出循环
            if datetime.datetime.now().timestamp() - self._lastMineTime > 60 * 11:
                self.mark = False


# 大窗口
if __name__ == '__main__':
    time.sleep(2)
    print("start task....")
    MineWithShop().do()
    # 挖完矿关机
    print("结束挖矿")
