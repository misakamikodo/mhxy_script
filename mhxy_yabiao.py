import argparse

from mhxy import *


# 押镖
class YaBiao(MhxyScript):

    def do(self):
        finishTimes = 0
        while True:
            locate, idx =  waitUtilFindPic(r'resources/small/dialogpick.png')
            cooldown(1)
            if locate is not None:
                cooldown(1)
                pyautogui.leftClick(locate.x, locate.y + relativeY2Act(1))
                cooldown(1)
                Util.leftClick(10.5, 8.2)
                finishTimes += 1
                cooldown(0.5)
                if Util.locateCenterOnScreen(r'resources/richang/yabiao_nopower.png') is not None:
                    log("活力不够50")
                    break
                if finishTimes >= 3:
                    while Util.locateCenterOnScreen(r'resources/small/activity.png') is None:
                        cooldown(30)
                    break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-ir', '--idxArray', required=False, default='0', type=str)
    args = parser.parse_args()
    indexArr = args.idxArray.split(',')

    def func(idx):
        YaBiao(idx=args.idx).do()

    if len(indexArr) != 1:
        for each in indexArr:
            func(int(each))
    else:
        func(int(indexArr[0]))
