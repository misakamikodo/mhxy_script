import argparse

from mhxy import *


class AutoBattle:

    def do(self):
        click = False
        while True:
            # linglongshi jingjichang
            linglongshi = Util.locateCenterOnScreen(r'resources/small/jingjichang.png')
            if linglongshi is not None:
                pyautogui.leftClick(linglongshi.x, linglongshi.y - 10)
            if battling(r'resources/small/no_auto_battle.png'):
                if not click:
                    cooldown(2)
                    Util.leftClick(-1.2, -1.2)
                    click = True
                cooldown(2)
            else:
                click = False
                cooldown(2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', default=0, type=int)
    args = parser.parse_args()
    pyautogui.PAUSE = 0.5
    log("start task....")
    init(idx=args.idx)
    AutoBattle().do()

