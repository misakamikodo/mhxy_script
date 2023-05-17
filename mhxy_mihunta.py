from mhxy import *

class Mihunta:
    def _reach(self):
        r = pyautogui.locateCenterOnScreen(r'resources/mihunta/chuansong.png')
        return r

    def mihunta(self):
        # 流程任务
        def do():
            Util.leftClick(-3, 6)
            reachPos = self._reach()
            while reachPos is None:
                reachPos = self._reach()
                cooldown(2)
            pyautogui.leftClick(reachPos.x, reachPos.y)

        escapeBattleDo(do)

# 喊话
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    init()
    Mihunta().mihunta()

