import argparse

from mhxy import *


# 答题
class DaTi(MhxyScript):

    def sumMethod(self):
        picArr = [r'resources/richang/sanjieqiyuan.png',
                             r'resources/richang/keju.png',
                             r'resources/richang/quwen.png']
        idx = gotoActivity(picArr)
        if idx is None:
            return False
        elif idx==0:
            self.sanJieQiYuan()
        elif idx==1:
            self.keJu()
        elif idx==2:
            self.quwen()
        else:
            return False
        return True

    def sanJieQiYuan(self):
        while Util.locateCenterOnScreen(r'resources/richang/sanjieqiyuan_end.png') is None:
            Util.leftClick(10, 7)
            cooldown(2.3)
        Util.leftClick(-1.5, 4.5)
        cooldown(1)

    def keJu(self):
        for i in range(0, 10):
            Util.leftClick(10, 10)
            cooldown(2.3)
        Util.leftClick(-1.5, 5.5)
        cooldown(1)

    def quwen(self):
        cooldown(3)
        times = 0
        while times <= 5:
            # 用 locateAll导致返回的同个位置有重复
            heart = pyautogui.locateCenterOnScreen(r'resources/richang/quwen_heart.png',
                                                region=(frame.left, frame.top, frameSize[0], frameSize[1]),
                                                confidence=0.9)
            # 颜色不同会被识别
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
        now = datetime.datetime.now()
        week = now.weekday()
        hour = now.hour
        max = 1
        if hour >= 11:
            max += 1
        if hour >= 17 and week < 5:
            max += 1
        while self.sumMethod() and max > 1:
            max -= 1
        # if not gotoActivity(r'resources/richang/quwen.png'):
        #     return
        # self.quwen()
        # if hour >= 11:
        #     if not gotoActivity(r'resources/richang/sanjieqiyuan.png'):
        #         return
        #     self.sanJieQiYuan()
        # if hour >= 17 and week < 5:
        #     if not gotoActivity(r'resources/richang/keju.png'):
        #         return
        #     self.keJu()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', required=False, default=0, type=int)
    args = parser.parse_args()

    def func(idx):
        DaTi(idx=idx).do()

    if args.idx == -1:
        i = 0
        while args.idx == -1 and len(getWindowList()) > i:
            func(i)
            i = i + 1
    else:
        func(args.idx)

