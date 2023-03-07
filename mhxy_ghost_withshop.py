from mhxy_ghost import *


class GhostWithShop(Ghost):
    __shopFlag = True

    def shop(self):
        while Util.locateOnScreen(r'resources/small/zhen_tian.png') is None:
            cooldown(3)
        Util.leftClick(1, 2)
        cooldown(1)
        Util.leftClick(1, 5.5)
        cooldown(1)
        while self.__shopFlag:
            completeLocation = Util.locateOnScreen('resources/ghost/complete_ghost0.png')
            if completeLocation is not None:
                # 选择继续捉鬼
                pyautogui.leftClick(completeLocation.left + completeLocation.width - 50,
                                    completeLocation.top + completeLocation.height - 20)
                print("结束抓鬼 ", completeLocation)
                cooldown(1)
                Util.leftClick(-2.5, 3.5)
                break
            # 找三次是否有有廉价商品 r'resources/shop/item600.png',r'resources/shop/suipian.png',r'resources/shop/meigui.png',
            itemPic = [r'resources/ghost/' + 'suipian' + '.png']
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

                buyTab = winRelativeXY(20, 16.5)
                pyautogui.leftClick(buyTab[0], buyTab[1])
                # 如果是多数量的尝试选择最大数量,否则注释
                inputTab = winRelativeXY(13, 11.7)
                pyautogui.leftClick(inputTab[0], inputTab[1])
                numberTab = winRelativeXY(14, 9.5)
                pyautogui.doubleClick(numberTab[0], numberTab[1])

                buy2Tab = winRelativeXY(14, 15)
                pyautogui.leftClick(buy2Tab[0], buy2Tab[1])
            else:
                cooldown(10)
                leftTab = winRelativeXY(4, 7.5)
                pyautogui.leftClick(leftTab[0], leftTab[1])
                itemTab = winRelativeXY(10, 8)
                pyautogui.leftClick(itemTab[0], itemTab[1])
        cooldown(1)


    def _startMission(self, location):
        cooldown(1)
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
            pyautogui.click(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix(), clicks=1,
                            button=pyautogui.LEFT)
            cooldown(0.2)
            self.getPoint()
            pyautogui.click(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix(), clicks=1,
                            button=pyautogui.LEFT)
        else:
            pyautogui.click(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix(), clicks=1,
                            button=pyautogui.LEFT)
            # 关对话 + 追踪
        pyautogui.click(self._chaseWin[0], self._chaseWin[1] + self._chaseWinFix(), clicks=1,
                        button=pyautogui.LEFT)

    def _startGhostDo(self):
        self.shop()

# 小窗口 pyinstaller -F mhxy_ghost.py
if __name__ == '__main__':
    idx = 0 if len(sys.argv) <= 1 else sys.argv[1]
    pyautogui.PAUSE = 0.3  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
    pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
    try:
        GhostWithShop(idx=idx).ghost()
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
