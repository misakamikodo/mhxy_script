import os
from configparser import ConfigParser

from mhxy import *


class Menpai(MhxyScript):
    chaseWin = [-3, 5.8 + 0]

    def __init__(self, idx=0, changWinPos=True, resizeToSmall=False) -> None:
        super().__init__(idx, changWinPos, resizeToSmall)
        file_path = os.path.join(os.path.abspath('.'), 'resources/menpai/menpai.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")
        conn = ConfigParser()
        conn.read(file_path)
        chasepos = float(conn.get('main', 'chasepos'))
        self.chaseWin[1] = 3.8 + chasepos * 2

    def do(self):
        def start():
            return pyautogui.locateCenterOnScreen(r'resources/menpai/start.png')

        # 流程任务 领取任务开始
        def do():
            def reach():
                return pyautogui.locateCenterOnScreen(r'resources/menpai/select.png')

            # 离开战斗后点击启动
            Util.doubleClick(self.chaseWin[0], self.chaseWin[1])
            startPos = start()
            reachPos = reach()
            times = 0
            while reachPos is None and startPos is None and times < 10:
                if not self._flag:
                    exit(0)
                reachPos = reach()
                if reachPos is None:
                    startPos = start()
                cooldown(1)
                times += 1
                # 新的一个战斗或完成一轮
                if times >= 6:
                    print("恢复流程")
                    # 10秒左右还没进入战斗 重新追踪
                    Util.leftClick(self.chaseWin[0], self.chaseWin[1])
                    times = 0

            if reachPos is not None:
                pyautogui.leftClick(reachPos.x, reachPos.y)
            elif startPos is not None:
                pyautogui.leftClick(startPos.x, startPos.y)
                cooldown(1)
                Util.leftClick(-4, 12.5)
                cooldown(0.2)
                Util.doubleClick(self.chaseWin[0], self.chaseWin[1])
                while reachPos is None:
                    reachPos = reach()
                    cooldown(0.5)
                pyautogui.leftClick(reachPos.x, reachPos.y)

        startPos = start()
        if startPos is not None:
            pyautogui.leftClick(startPos.x, startPos.y)
            cooldown(1)
            Util.leftClick(-4, 12.5)
            cooldown(0.2)
            Util.doubleClick(self.chaseWin[0], self.chaseWin[1])
        escapeBattleDo(do)


# 副本 进入第一个副本为起点
if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    print("start task....")
    Menpai(idx=1).do()
