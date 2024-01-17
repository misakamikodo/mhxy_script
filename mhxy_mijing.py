from mhxy import *


# 秘境 死亡一次或者点两进入战斗停止
class MiJing(MhxyScript):

    def do(self):
        Util.leftClick(-3, 9.3)
        cooldown(0.8)
        if Util.locateCenterOnScreen(r'resources/richang/mijing_select.png') is not None:
            Util.leftClick(7, 15.5)  # 选择普通秘境 日月 17
            cooldown(0.8)
            Util.leftClick(14, 11.5)  # 确定
            cooldown(0.8)
        btl = Util.locateCenterOnScreen(r'resources/richang/mijing_btl.png')
        pyautogui.leftClick(btl.x, btl.y)  # 继续战斗
        cooldown(2.5)
        Util.leftClick(-3, 8)  # 追踪
        cooldown(2 * 60)
        resumeTimes = 0
        while True:
            resume = Util.locateCenterOnScreen(r'resources/richang/mijing_resume.png')
            if resume is not None:
                resumeTimes += 1
                if resumeTimes <= 2:
                    pyautogui.leftClick(resume.x, resume.y)
                else:
                    cooldown(1)
                    Util.leftClick(-1.5, 9.5)
                    cooldown(1)
                    waitThenClickUtilFindPic(r'resources/richang/mijing_escape.png')
                    break
            if Util.locateCenterOnScreen(r'resources/small/fail.png') is not None:
                cooldown(1)
                Util.leftClick(-1.5, 9.5)
                cooldown(1)
                waitThenClickUtilFindPic(r'resources/richang/mijing_escape.png')
                break
            cooldown(10)


if __name__ == '__main__':
    MiJing().do()
