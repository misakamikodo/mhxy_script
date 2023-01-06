from mhxy import *

class Mihunta:
    def _reach(self):
        r = pyautogui.locateCenterOnScreen(r'resources/mihunta/chuansong.png')
        return r

    def _meetEscape(self):
        r = pyautogui.locateCenterOnScreen(r'resources/mihunta/escape.png')
        return r

    def _reachEscape(self):
        return pyautogui.locateOnScreen(r'resources/mihunta/chuansong.png') is not None

    def mihunta(self):
        # 流程任务
        def do():
            Util.leftClick(-3, 8)
            escape = self._meetEscape()
            while escape is not None:
                # 点击逃跑怪等待点击成功
                pyautogui.leftClick(escape.x + relativeX2Act(1), escape.y + relativeY2Act(2))
                while not self._reachEscape():
                    cooldown(2)
                pyautogui.leftClick(winRelativeX(-3), winRelativeY(9))
                escape = self._meetEscape()
                Util.leftClick(-3, 8)
                pass
            reachPos = self._reach()
            while reachPos is None:
                reachPos = self._reach()
                cooldown(2)
            pyautogui.leftClick(reachPos.x, reachPos.y)

        escapeBattleDo(do, battleingPic=r'resources/miunta/tian.png')

# 喊话
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    init()
    Mihunta().mihunta()

