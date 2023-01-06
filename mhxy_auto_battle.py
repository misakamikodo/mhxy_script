from mhxy import *

class AutoBattle:

    def do(self):
        click = False
        while True:
            if battling(r'resources/common/zhen_niao.png'):
                if not click:
                    cooldown(3)
                    Util.leftClick(-1.2, -1.2)
                    click = True
                cooldown(5)
            else:
                click = False
                cooldown(5)

if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    print("start task....")
    init()
    AutoBattle().do()

