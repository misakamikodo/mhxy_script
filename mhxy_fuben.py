import argparse

from mhxy import *


class Fuben(MhxyScript):
    # 暂时没用，请忽视
    xiashi_fix = 5.6 + 2
    _fubenIdx = 0
    fubenPos = [

    ]
    config = {
        'lastFuben': r'resources/fuben/fuben_flag.png'
    }

    def __init__(self, mission=None,
                 idx=0, changWinPos=True, resizeToSmall=False) -> None:
        super().__init__(idx, changWinPos, resizeToSmall)
        if mission is None:
            mission = ['xiashi50', 'norm70', 'norm50_1', 'norm50_2']
        if 'xiashi70' in mission:
            self.fubenPos.append(("xiashi", 13, 15))
        if 'xiashi50' in mission:
            self.fubenPos.append(("xiashi", 7, 15))
        if 'norm70' in mission:
            self.fubenPos.append(("norm", 19, 15))
        if 'norm50_1' in mission:
            self.fubenPos.append(("norm", 13, 15))
        if 'norm50_2' in mission:
            self.fubenPos.append(("norm", 7, 15))

    def _changan(self):
        return Util.locateCenterOnScreen(r'resources/fuben/activity.png',
                                         region=(int(frame.left + relativeX2Act(5)), frame.top,
                                                 int(frameSize[0] - relativeX2Act(5)), int(relativeY2Act(2.8))),
                                         confidence=0.95)

    # 流程任务
    def _do(self):
        def clickSkip(locate, idx, times):
            if not self._stopCheck():
                sys.exit(0)
            reachPos = Util.locateCenterOnScreen(r'resources/fuben/select.png')
            if reachPos is not None:
                # 对话
                pyautogui.leftClick(reachPos.x, reachPos.y + relativeY2Act(1.5))
            elif Util.locateCenterOnScreen(r'resources/fuben/skipJuqing.png') is not None:
                # 跳过剧情动画
                Util.leftClick(-3, 7)
            elif Util.locateCenterOnScreen(r'resources/fuben/juqingskip_new.png') is not None:
                # 新版本阅读剧情
               Util.leftClick(-1.5, 1.8)
            elif Util.locateCenterOnScreen(r'resources/small/blood.png') is None:
                # 阅读剧情
                Util.leftClick(-3, 1.8)
            else:
                # 追踪任务 如果 xiashi_fix 不是在第一个任务，可能会使得 到长安点到第一个任务出现弹窗使得脚本出错，此时确认下没到达长安，可降低发生的概率
                if self.xiashi_fix < 6 or self._changan() is None:
                    Util.leftClick(-3, 5.5)
            cooldown(1)

        def doUntil2Changan():
            changanPos = self._changan()
            while changanPos is None:
                # 找不到头像则正在对话点击头像位置跳过 直到找到头像位置
                doUtilFindPic([r'resources/small/enter_battle_flag.png',
                               {"pic": r'resources/fuben/activity.png',
                                "region": (int(frame.left + relativeX2Act(5)), frame.top,
                                           int(frameSize[0] - relativeX2Act(5)), int(relativeY2Act(2.8)))}], clickSkip,
                              warnTimes=30)
                changanPos = self._changan()
                cooldown(2)

        #  进入第一个副本为起点
        doUntil2Changan()

        if self._fubenIdx >= len(self.fubenPos):
            return False
        #elif self.fubenPos[self._fubenIdx][0] == "xiashi":
        #    # 已领取的侠士任务所在坐标
        #    Util.leftClick(-3, self.xiashi_fix)
        #    cooldown(2.0)
        #    Util.leftClick(self.fubenPos[self._fubenIdx][1], self.fubenPos[self._fubenIdx][2])
        #    self._fubenIdx += 1
        #    log("下一个副本" + str(log("下一个副本" + str())))
        else:
            cooldown(1)
            Util.leftClick(7.5, 1.5)
            cooldown(0.5)
            Util.leftClick(3, 4.5)
            cooldown(1)
            lastFuben = Util.locateCenterOnScreen(self.config['lastFuben'])
            i = 0
            while lastFuben is None and i in range(0, 2):
                pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
                pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)
                cooldown(2)
                lastFuben = Util.locateCenterOnScreen(self.config['lastFuben'])
                i += 1
            if lastFuben is not None:
                cooldown(1)
                pyautogui.leftClick(lastFuben.x + relativeX2Act(3), lastFuben.y + relativeY2Act(0.2))
                se, idx = waitUtilFindPic(r'resources/fuben/selectfuben.png')
                cooldown(0.3)
                #  11
                pyautogui.leftClick(se.x, se.y)
                cooldown(2)
                if self.fubenPos[self._fubenIdx][0] == "xiashi":
                    Util.leftClick(9, 5)
                    cooldown(1)
                # 下一个副本
                Util.leftClick(self.fubenPos[self._fubenIdx][1], self.fubenPos[self._fubenIdx][2])
                self._fubenIdx += 1
                log("下一个副本" + str(self._fubenIdx))
            else:
                pass
                pl.playsound('resources/common/music.mp3')
        return True

    def loginIn(self):
        cooldown(1)
        loginInBtn = Util.locateCenterOnScreen(r'resources/fuben/loginin.png')
        if loginInBtn is not None:
            pyautogui.leftClick(loginInBtn.x, loginInBtn.y)
        cooldown(5)
        Util.leftClick(12, 13.5)

    def do(self):
        while self._do() and self._stopCheck():
            cooldown(2)


# 副本 进入第一个副本为起点 小窗口
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', required=False, default=0, type=int)
    parser.add_argument('-m', '--mission', required=False, default='xiashi50,norm70,norm50_1,norm50_2', type=str)
    args = parser.parse_args()
    pyautogui.PAUSE = 0.2
    log("start task....")
    def func(idx):
        Fuben(mission=args.mission.split(","), idx=idx).do()

    if args.idx == -1:
        i = 0
        while args.idx == -1 and len(getWindowList()) > i:
            func(i)
            i = i + 1
    else:
        func(args.idx)
