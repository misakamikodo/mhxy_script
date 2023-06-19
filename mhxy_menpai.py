from mhxy import *


class Menpai:
    def menpai(self, chaseWin):
        def start():
            return pyautogui.locateCenterOnScreen(r'resources/menpai/start.png')

        # 流程任务 领取任务开始
        def do():
            def reach():
                return pyautogui.locateCenterOnScreen(r'resources/menpai/select.png')

            pyautogui.doubleClick(chaseWin[0], chaseWin[1])
            startPos = start()
            reachPos = None
            if startPos is None:
                reachPos = reach()
            else:
                pyautogui.leftClick(startPos.x, startPos.y)
                pyautogui.doubleClick(chaseWin[0], chaseWin[1])
            while reachPos is None and startPos is None:
                reachPos = reach()
                if reachPos is None:
                    startPos = start()
                cooldown(1)
            if reachPos is not None:
                pyautogui.leftClick(reachPos.x, reachPos.y)
            else:
                pyautogui.leftClick(startPos.x, startPos.y)
                cooldown(0.2)
                Util.leftClick(-4, 12.5)
                pyautogui.doubleClick(chaseWin[0], chaseWin[1])
                while reachPos is None:
                    reachPos = reach()
                    cooldown(0.5)
                pyautogui.leftClick(reachPos.x, reachPos.y)

        startPos = start()
        if startPos is not None:
            pyautogui.leftClick(startPos.x, startPos.y)
        escapeBattleDo(do)


# 副本 进入第一个副本为起点
if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    print("start task....")
    init()
    Menpai().menpai((winRelativeX(-3), winRelativeY(5.8 + 2)))
