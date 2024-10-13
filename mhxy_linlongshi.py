import argparse
import os
from configparser import ConfigParser

from mhxy import *


# 目前只取红色玲珑石
class Linlingshi(MhxyScript):
    chasepos = 1

    def __init__(self, idx=0, changWinPos=True, resizeToSmall=False, config=None, stopCheck=None) -> None:
        super().__init__(idx, changWinPos, resizeToSmall, config, stopCheck)
        file_path = os.path.join(os.path.abspath('.'), 'resources/linlongshi/linlongshi.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")
        conn = ConfigParser()
        conn.read(file_path)
        self.chasepos = float(conn.get('main', 'chasepos'))

    def do(self):
        cooldown(2)
        for _ in range(0, 5):
            if Util.locateOnScreen(r'resources/linlongshi/start.png') is None:
                findAndUseInBag(r'resources/linlongshi/red.png')
            waitThenClickUtilFindPic(r'resources/linlongshi/start.png')
            cooldown(0.2)
            Util.leftClick(-3.5, 10.6)
            cooldown(0.5)
            Util.leftClick(-3.5, 12.6)
            waitUtilFindPic(r'resources/linlongshi/confirmed.png')
            # 关闭对话框用防止影响接下来的脚本
            Util.leftClick(11, 11)
            cooldown(0.2)
            for i in range(0, 3):
                # 有剧情 + 4
                Util.leftClick(-1, 3.5 + 2 * self.chasepos)
                waitThenClickUtilFindPic(r'resources/linlongshi/select.png')
                cooldown(1)
                # 花果山
                pyautogui.rightClick()
                cooldown(0.2)
                Util.leftClick(-1.2, -1.2)
                waitEscapeBattle()
                # 关闭对话框用防止影响接下来的脚本
                Util.leftClick(11, 11)
                cooldown(0.2)



# 副本 进入第一个副本为起点 小窗口
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', required=False, default=0, type=int)
    args = parser.parse_args()
    log("start task....")
    def func(idx):
        Linlingshi(idx=idx).do()

    if args.idx == -1:
        i = 0
        while args.idx == -1 and len(getWindowList()) > i:
            func(i)
            i = i + 1
    else:
        func(args.idx)
