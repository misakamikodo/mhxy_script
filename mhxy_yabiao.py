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
                if finishTimes >= 3:
                    while Util.locateCenterOnScreen(r'resources/fuben/activity.png') is None:
                        cooldown(30)
                    break


if __name__ == '__main__':
    YaBiao().do()
