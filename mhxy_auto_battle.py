import argparse

from mhxy import *


class AutoBattle:
    type=None

    def __init__(self, type=None) -> None:
        super().__init__()
        self.type=type

    def do(self):
        click = False
        while True:
            # linglongshi jingjichang huashang
            if self.type is not None:
                linglongshi = Util.locateCenterOnScreen(rf'resources/small/{self.type}.png')
                if linglongshi is not None:
                    pyautogui.leftClick(linglongshi.x, linglongshi.y - 10)
            if battling(r'resources/small/no_auto_battle.png'):
                if not click:
                    cooldown(1.5)
                    # 花果山
                    pyautogui.moveTo(winRelativeX(-1.2), winRelativeY(-1.2))
                    pyautogui.rightClick()
                    cooldown(0.2)
                    Util.leftClick(-1.2, -1.2)
                    click = True
                cooldown(2)
            else:
                click = False
                cooldown(2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', default=0, type=int)
    parser.add_argument('-t', '--type', default=None, type=str)
    args = parser.parse_args()
    pyautogui.PAUSE = 0.5
    log("start task....")
    init(idx=args.idx)
    AutoBattle(type=args.type).do()

