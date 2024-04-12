import argparse

from mhxy import *


# 答题
class DaTi(MhxyScript):

    def sanJieQiYuan(self):
        if not gotoActivity(r'resources/richang/sanjieqiyuan.png'):
            return
        while Util.locateCenterOnScreen(r'resources/richang/sanjieqiyuan_end.png') is None:
            Util.leftClick(10, 7)
            cooldown(2.3)
        Util.leftClick(-1.5, 4.5)
        cooldown(1)

    def keJu(self):
        if not gotoActivity(r'resources/richang/keju.png'):
            return
        for i in range(0, 10):
            Util.leftClick(10, 10)
            cooldown(2.3)
        Util.leftClick(-1.5, 5.5)
        cooldown(1)

    def quwen(self):
        if not gotoActivity(r'resources/richang/quwen.png'):
            return
        cooldown(3)
        times = 0
        while times <= 5:
            # 用 locateAll导致返回的同个位置有重复
            heart = pyautogui.locateCenterOnScreen(r'resources/richang/quwen_heart.png',
                                                region=(frame.left, frame.top, frameSize[0], frameSize[1]),
                                                confidence=0.9)
            # 颜色不同会被识别，所以不能这样
            # while heart is not None:
            #     pyautogui.leftClick(heart.x, heart.y)
            #     cooldown(1)
            #     times += 1
            # else:
            #     pyautogui.moveTo(winRelativeX(7), winRelativeY(17))
            #     pyautogui.dragTo(winRelativeX(7), winRelativeY(5), duration=0.5)
            #     cooldown(2)
            if heart is not None:
                pyautogui.leftClick(heart.x, heart.y)
                cooldown(1)
                times += 1
            pyautogui.moveTo(winRelativeX(7), winRelativeY(17))
            pyautogui.dragTo(winRelativeX(7), winRelativeY(11), duration=0.5)
            cooldown(2)
        Util.leftClick(13, 10)
        cooldown(1)

    def do(self):
        self.quwen()
        now = datetime.datetime.now()
        week = now.weekday()
        hour = now.hour
        if hour >= 11:
            self.sanJieQiYuan()
        if hour >= 17 and week < 5:
            self.keJu()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', default=0, type=int)
    args = parser.parse_args()
    DaTi(idx=args.idx).do()
