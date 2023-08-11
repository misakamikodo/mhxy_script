from mhxy import *

class AutoBattle:

    def do(self):
        click = False
        while True:
            linglongshi = Util.locateCenterOnScreen(r'resources/small/linglongshi.png')
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
    pyautogui.PAUSE = 0.5
    print("start task....")
    init()
    AutoBattle().do()

