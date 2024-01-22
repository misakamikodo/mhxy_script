import os
import sys
from configparser import ConfigParser

from mhxy import *


class Mihunta(MhxyScript):
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

    def _reach(self):
        r = pyautogui.locateCenterOnScreen(r'resources/mihunta/chuansong.png')
        return r

    def do(self):
        # 流程任务
        def do():
            Util.leftClick(self.chaseWin[0], self.chaseWin[1])
            reachPos = self._reach()
            times = 0
            while reachPos is None:
                if not self._flag:
                    sys.exit(0)
                reachPos = self._reach()
                cooldown(2)
                times += 1
                # 新的一个战斗或完成一轮
                if times >= 6:
                    log("恢复流程")
                    # 10秒左右还没进入战斗 重新追踪
                    Util.leftClick(self.chaseWin[0], self.chaseWin[1])
                    times = 0
            cooldown(0.5)
            pyautogui.leftClick(reachPos.x, reachPos.y)

        escapeBattleDo(do)


# 喊话
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    log("start task....")
    Mihunta().do()
