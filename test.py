from mhxy import *

if __name__ == '__main__':
    cooldown(3)
    init()
    pyautogui.moveTo(winRelativeX(10), winRelativeY(4.6))
    pyautogui.dragTo(winRelativeX(10), winRelativeY(15), duration=0.15)
    # init(idx=0)
    # cooldown(2)
    # res = pyautogui.locateAllOnScreen('#BEBD27')
    # print(res)
    # while True:
    #     t = Util.locateCenterOnScreen(r'resources/small/kuang.png')
    #     if t is not None:
    #         pyautogui.leftClick(t.x, t.y)
    #         cooldown(0.1)
    #         t = Util.locateCenterOnScreen(r'resources/small/select.png')
    #         if t is not None:
    #             pyautogui.leftClick(t.x, t.y)
    #         cooldown(5)
    #         t = Util.locateCenterOnScreen(r'resources/small/dig.png')
    #         if t is not None:
    #             pyautogui.leftClick(t.x, t.y)
    #             cooldown(5)
    #     cooldown(2)
