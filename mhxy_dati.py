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

    def do(self):
        now = datetime.datetime.now()
        week = now.weekday()
        hour = now.hour
        if hour >= 11:
            self.sanJieQiYuan()
        if hour >= 17 and week < 5:
            self.keJu()


if __name__ == '__main__':
    DaTi().do()
