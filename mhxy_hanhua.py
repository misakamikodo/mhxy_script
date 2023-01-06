from mhxy import *


class Hanhua:
    def hanhua(self):
        while True:
            Util.leftClick(9, 2)
            Util.leftClick(3.5, 11.5)
            # 第二个 14 第一个 x 9
            Util.leftClick(9, 12)
            Util.leftClick(11, 2)
            cooldown(4)

    def hanhuaWithText(self):
        cooldown(3)
        Util.write("哈哈哈哈哈")
        # while True:
        #     Util.leftClick(5, 2)
        #     cooldown(1)
        #     Util.write("哈哈哈哈哈")
        #     cooldown(1)
        #     Util.leftClick(13, 2)
        #     cooldown(2)


# 喊话
if __name__ == '__main__':
    Util.PAUSE = 0.2
    print("start task....")
    init(resizeToNice=True)
    Hanhua().hanhua()
