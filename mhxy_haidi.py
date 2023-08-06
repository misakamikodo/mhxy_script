from mhxy import *

class Haidi(MhxyScript):

    def do(self, chaseWin = (-3, 5.8 + 0)):
        # 流程任务 领取任务后起点
        def do():
            def reach():
                return Util.locateCenterOnScreen(r'resources/haidi/select.png')
            Util.doubleClick(chaseWin[0], chaseWin[1])
            reachPos = reach()
            times = 0
            while reachPos is None:
                reachPos = reach()
                cooldown(1)
                times += 1
                # 新的一个战斗或完成一轮
                if times >= 6:
                    print("恢复流程")
                    # 10秒左右还没进入战斗 重新追踪
                    Util.leftClick(chaseWin[0], chaseWin[1])
                    times = 0
            Util.leftClick(reachPos.x, reachPos.y)
        escapeBattleDo(do)

# 副本 进入第一个副本为起点
if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    print("start task....")
    Haidi().do((-3, 6))

