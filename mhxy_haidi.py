from mhxy import *

class Haidi:

    def haidi(self, chaseWin):
        # 流程任务 领取任务后起点
        def do():
            def reach():
                return pyautogui.locateCenterOnScreen(r'resources/haidi/select.png')
            # 下一个
            pink = pyautogui.locateCenterOnScreen(r'resources/haidi/pink.png')
            if pink is None:
                pyautogui.leftClick(chaseWin[0], chaseWin[1])
                pyautogui.leftClick(chaseWin[0], chaseWin[1])
            else:
                pyautogui.leftClick(pink.x, pink.y)
            reachPos = reach()
            while reachPos is None:
                reachPos = reach()
                cooldown(1)
            pyautogui.leftClick(reachPos.x, reachPos.y)
        escapeBattleDo(do)

# 副本 进入第一个副本为起点
if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    print("start task....")
    init()
    Haidi().haidi((winRelativeX(-4), winRelativeY(6)))

