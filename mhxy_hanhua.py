from mhxy import *


class Hanhua:
    def hanhua(self):
        while True:
            Util.leftClick(9, 2)
            Util.leftClick(3.5, 11.5)
            # 第二个 14 第一个 x 9
            Util.leftClick(9, 12)
            Util.leftClick(11, 2)
            cooldown(60*2)

    def hanhuaWithText(self):
        text = r'五本随便来#102'
        cooldown(3)
        while True:
            Util.leftClick(5, 2)
            cooldown(1)
            for i in range(0, int(len(text) / 50 + 1)):
                Util.write(text[i * 50:min(i * 50 + 50, len(text))])
                cooldown(1)
                Util.leftClick(11, 2)
                cooldown(2)


# 喊话
if __name__ == '__main__':
    Util.PAUSE = 0.2
    log("start task....")
    init()
    Hanhua().hanhuaWithText()
