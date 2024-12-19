import argparse

from mhxy import *


# 押镖
class YaBiao(MhxyScript):

    def do(self):
        finishTimes = 0
        while True:
            finish = Util.locateCenterOnScreen(r'resources/richang/yabiao_finish.png')
            if finish is not None:
                cooldown(1)
                pyautogui.leftClick(finish.x, finish.y)
                cooldown(1)
                Util.leftClick(14, 11)
                finishTimes += 1
                cooldown(0.5)
                if Util.locateCenterOnScreen(r'resources/richang/yabiao_nopower.png') is not None:
                    log("活力不够50")
                    break
                if finishTimes >= 3:
                    while Util.locateCenterOnScreen(r'resources/fuben/activity.png') is None:
                        cooldown(30)
                    break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-ir', '--idxArray', required=False, default='0', type=str)
    args = parser.parse_args()
    indexArr = args.idxArray.split(',')

    def func(idx):
        YaBiao(idx=idx).do()

    if len(indexArr) != 1:
        for each in indexArr:
            func(int(each))
    else:
        func(int(indexArr[0]))
