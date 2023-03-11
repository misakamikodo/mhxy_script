from mhxy import *


class Fuben:
    _fix = 5.6 + 2
    _fubenIdx = 0
    fubenPos = [
        # ("xiashi", 13, 15),
        ("xiashi", 7, 15),

        ("norm", 19, 15),
        ("norm", 13, 15),
        ("norm", 7, 15)
    ]
    config = {
        # 'lastFuben': r'resources/fuben/lvyanrumeng.png',
        # 'lastFuben': r'resources/fuben/erchongying.png',
        'lastFuben': r'resources/fuben/jinchanxin.png',
        # 'lastFuben': r'resources/fuben/liulisui.png',

        # 'avatar': r'resources/small/avatar_mll.png',
        'avatar': r'resources/small/avatar_spl.png',
        # 'avatar': r'resources/small/avatar_hmr.png',
        # 'avatar': r'resources/small/avatar_wmr.png',

        # 'zhen': r'resources/small/zhen_hu5.png',
        'zhen': r'resources/small/zhen_long.png',
        # 'zhen': r'resources/small/zhen_ying.png',
        # 'zhen': r'resources/small/zhen_tian.png',
    }

    def __init__(self, idx=0) -> None:
        # init(resizeToNice=True)
        init(idx=idx, resizeToNice=False)

    def _changan(self):
        return Util.locateCenterOnScreen(r'resources/fuben/activity.png')

    # 流程任务
    def _do(self):
        def clickSkip(locate, idx):
            reachPos = Util.locateCenterOnScreen(r'resources/fuben/select.png')
            if reachPos is not None:
                # 对话
                pyautogui.leftClick(reachPos.x, reachPos.y + relativeY2Act(1.5))
            elif Util.locateCenterOnScreen(r'resources/fuben/skipJuqing.png') is not None:
                # 跳过剧情动画
                Util.leftClick(-3, 7)
            elif Util.locateCenterOnScreen(self.config['avatar']) is None:
                # 阅读剧情
                Util.leftClick(-3, 1.8)
            else:
                # 追踪任务
                Util.leftClick(-3, 5.5)
            cooldown(1)

        def doUntil2Changan():
            changanPos = self._changan()
            while changanPos is None:
                # 找不到头像则正在对话点击头像位置跳过 直到找到头像位置
                doUtilFindPic([self.config['zhen'], r'resources/fuben/activity.png'], clickSkip)
                changanPos = self._changan()
                cooldown(2)

        #  进入第一个副本为起点
        doUntil2Changan()
        if self._fubenIdx >= len(self.fubenPos):
            return False
        elif self.fubenPos[self._fubenIdx][0] == "xiashi":
            # 已领取的侠士任务所在坐标
            Util.leftClick(-3, self._fix)
            cooldown(2.0)
            Util.leftClick(self.fubenPos[self._fubenIdx][1], self.fubenPos[self._fubenIdx][2])
            self._fubenIdx += 1
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
                cooldown(1)
                lastFuben = Util.locateCenterOnScreen(self.config['lastFuben'])
                i += 1
            if lastFuben is not None:
                cooldown(1)
                pyautogui.leftClick(lastFuben.x + relativeX2Act(3.5), lastFuben.y + relativeY2Act(0.2))
                cooldown(4.5)
                Util.leftClick(-4, 11)
                cooldown(2)
                # 下一个副本
                Util.leftClick(self.fubenPos[self._fubenIdx][1], self.fubenPos[self._fubenIdx][2])
                self._fubenIdx += 1
        return True

    def fuben(self):
        while self._do():
            cooldown(2)


# 副本 进入第一个副本为起点 小窗口
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    Fuben().fuben()
