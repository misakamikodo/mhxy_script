import argparse
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

    def take_mission(self, startPos):
        pyautogui.leftClick(startPos.x, startPos.y)
        cooldown(0.5)
        Util.leftClick(-4, 12.5)
        cooldown(0.5)

    def do(self):

        def start_pos():
            return Util.locateCenterOnScreen(r'resources/menpai/start.png')

        def reach_pos():
            return Util.locateCenterOnScreen(r'resources/menpai/select.png')

        # 流程任务 领取任务开始
        def do_out_of_battle():
            if datetime.datetime.now().minute >= 41:
                self._flag=False
            # 离开战斗后点击启动
            Util.leftClick(18, 16)
            cooldown(0.2)
            Util.leftClick(self.chaseWin[0], self.chaseWin[1])
            cooldown(1)
            startPos = start_pos()
            reachPos = reach_pos()
            times = 0
            while reachPos is None and startPos is None and times < 10:
                if not self._stopCheck():
                    sys.exit(0)
                reachPos = reach_pos()
                if reachPos is None:
                    startPos = start_pos()
                cooldown(1)
                times += 1
                # 新的一个战斗或完成一轮
                if times >= 6 and reachPos is None:
                    log("恢复流程")
                    # 10秒左右还没进入战斗 重新追踪
                    Util.leftClick(self.chaseWin[0], self.chaseWin[1])
                    times = 0

            cooldown(0.5)
            if reachPos is not None:
                pyautogui.leftClick(reachPos.x, reachPos.y)
            elif startPos is not None:
                self.take_mission(startPos)
                Util.leftClick(18, 16)
                cooldown(0.2)
                Util.leftClick(self.chaseWin[0], self.chaseWin[1])
                while reachPos is None:
                    reachPos = reach_pos()
                    cooldown(0.5)
                pyautogui.leftClick(reachPos.x, reachPos.y)

        cooldown(1)
        startPos = start_pos()
        if startPos is not None:
            self.take_mission(startPos)
        escapeBattleDo(do_out_of_battle)


# 副本 进入第一个副本为起点
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', required=False, default=0, type=str)
    args = parser.parse_args()
    pyautogui.PAUSE = 0.5
    log("start task....")
    while datetime.datetime.now().hour != 21:
        cooldown(2)
    Menpai(idx=int(args.idx)).do()
