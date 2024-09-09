import argparse

from mhxy import *


# 目前只取红色玲珑石
class Linlingshi(MhxyScript):

    def do(self):
        for _ in range(0, 5):
            waitThenClickUtilFindPic(r'resources/linlongshi/start.png')
            cooldown(0.2)
            Util.leftClick(-3.5, 10.6)
            waitUtilFindPic(r'resources/linlongshi/confirmed.png')
            # 关闭对话框用防止影响接下来的脚本
            Util.leftClick(11, 11)
            cooldown(0.2)
            for i in range(0, 3):
                Util.leftClick(-1, 3.5 + 2)
                waitThenClickUtilFindPic(r'resources/linlongshi/start.png')
                waitEscapeBattle()
                cooldown(0.2)

            findAndUseInBag(r'resources/linlongshi/red.png')



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
