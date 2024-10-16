import argparse

from mhxy import *


# 秘境 死亡一次或者点两进入战斗停止
class MiJing(MhxyScript):

    def do(self):
        def escape():
            cooldown(1)
            Util.leftClick(-1.5, 9.5)
            cooldown(1)
            mijingEscape = Util.locateCenterOnScreen(r'resources/richang/mijing_escape.png')
            if mijingEscape is not None:
                pyautogui.leftClick(mijingEscape.x, mijingEscape.y)
            else:
                Util.leftClick(1, 2)
                cooldown(0.5)
                waitThenClickUtilFindPic(r'resources/richang/daxue.png')
        print("开始位置是点击陆萧然的对话框")
        cooldown(2)
        Util.leftClick(-3, 9.3)
        cooldown(0.8)
        if Util.locateCenterOnScreen(r'resources/richang/mijing_select.png') is not None:
            Util.leftClick(7, 15.5)  # 选择普通秘境 日月 17
            cooldown(0.8)
            Util.leftClick(14, 11.5)  # 确定
            cooldown(0.8)
        btl = Util.locateCenterOnScreen(r'resources/richang/mijing_btl.png')
        times = 0
        while btl is None and times < 10:
            cooldown(1)
            Util.leftClick(-2.5, 12.3)
            btl = Util.locateCenterOnScreen(r'resources/richang/mijing_btl.png')
            print("关闭可使用物品对继续战斗的遮挡")
            times += 1
        if btl is None:
            pl.playsound('resources/common/music.mp3')
        pyautogui.leftClick(btl.x, btl.y)  # 继续战斗
        cooldown(2.5)
        self.chase()
        cooldown(2 * 60)
        resumeTimes = 0
        lastBattleTime = datetime.datetime.now()
        while True:
            resume = Util.locateCenterOnScreen(r'resources/richang/mijing_resume.png')
            if battling():
                lastBattleTime = datetime.datetime.now()
            elif datetime.datetime.now()-lastBattleTime>datetime.timedelta(seconds=50):
                self.chase()
            if resume is not None:
                resumeTimes += 1
                if resumeTimes <= 2: # 设置为 2 的话可能死
                    pyautogui.leftClick(resume.x, resume.y)
                else:
                    escape()
                    break
            if Util.locateCenterOnScreen(r'resources/small/fail.png') is not None:
                escape()
                break
            cooldown(10)

    def chase(self):
        mis = Util.locateCenterOnScreen(r'resources/richang/mijing_mission.png', confidence=0.8)

        if mis is not None:
            pyautogui.leftClick(mis.x, mis.y)  # 日月之井
        else:
            Util.leftClick(-3, 8)  # 普通秘境


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-ir', '--idxArray', required=False, default='0', type=str)
    args = parser.parse_args()
    indexArr = args.idxArray.split(',')

    def func(idx):
        MiJing(idx=idx).do()

    if len(indexArr) != 1:
        for each in indexArr:
            func(int(each))
    else:
        func(int(indexArr[0]))
