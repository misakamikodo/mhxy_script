import argparse

from mhxy import *


# 答题
class DaTi(MhxyScript):

    def findThenExec(self):
        picArr = [r'resources/richang/sanjieqiyuan.png',
                             r'resources/richang/keju.png',
                             r'resources/richang/quwen.png']
        idx = gotoActivity(picArr)
        if idx is None:
            return False
        elif idx == 0:
            self.sanJieQiYuan()
        elif idx == 1:
            self.keJu()
        elif idx == 2:
            self.quwen()
        else:
            return False
        return True

    def sanJieQiYuan(self):
        i = 0
        while Util.locateCenterOnScreen(r'resources/richang/sanjieqiyuan_end.png') is None or i > 30:
            Util.leftClick(7.5, 6)
            i += 1
            cooldown(2.3)
        Util.leftClick(-1.2, 3.3)
        cooldown(1)

    def keJu(self):
        for i in range(0, 10):
            Util.leftClick(8, 7.2)
            cooldown(2.3)
        Util.leftClick(-1.2, 4.3)
        cooldown(1)

    def quwen(self):
        cooldown(3)
        times = 0
        while times <= 5:
            # 用 locateAll导致返回的同个位置有重复
            heart = pyautogui.locateCenterOnScreen(r'resources/richang/quwen_heart.png',
                                                region=(frame.left, frame.top, frameSize[0], frameSize[1]),
                                                confidence=0.8)
            # 颜色不同会被识别
            if heart is not None:
                pyautogui.leftClick(heart.x, heart.y)
                cooldown(1)
                times += 1
            pyautogui.moveTo(winRelativeX(6), winRelativeY(12))
            pyautogui.dragTo(winRelativeX(6), winRelativeY(7), duration=0.5)
            cooldown(2)
        Util.leftClick(9.3, 7)
        cooldown(1)

    def do(self):
        now = datetime.datetime.now()
        # 0~6
        week = now.weekday()
        hour = now.hour
        max = 1
        if hour >= 11:
            max += 1
        if hour >= 17 and week < 5:
            max += 1
        while self.findThenExec() and max > 1:
            max -= 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-ir', '--idxArray', required=False, default='0', type=str)
    args = parser.parse_args()
    indexArr = args.idxArray.split(',')

    def func(idx):
        DaTi(idx=idx).do()

    if len(indexArr) != 1:
        for each in indexArr:
            func(int(each))
    else:
        func(int(indexArr[0]))

