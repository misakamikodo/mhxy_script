from mhxy import *


class _MissionType:

    def complete(self, locate, **kwargs):
        # 点击任务选项
        pyautogui.leftClick(locate.x, locate.y)


class _Fanwen(_MissionType):
    _noSubmitList = []

    def __init__(self) -> None:
        super().__init__()
        self.pic = r'resources/bangpai/fanwen.png'


class _Wupin(_MissionType):
    _noSubmitList = []

    def __init__(self) -> None:
        super().__init__()
        self.pic = [r'resources/bangpai/wupin.png', r'resources/bangpai/shangjiao.png', r'resources/bangpai/wupin2.png']

    def complete(self, locate, **kwargs):
        if kwargs['itemIdx'] == 0 or kwargs['itemIdx'] == 2:
            shangchen = Util.locateCenterOnScreen(r'resources/bangpai/shangchen.png') is not None
            # 选择第二个商品（防止商品被买）
            # 顺势上交
            if shangchen:
                Util.leftClick(-7, 8)
                pyautogui.leftClick(locate.x, locate.y)
                cooldown(2)
                Util.leftClick(-5, -5)
            else:
                pyautogui.leftClick(locate.x, locate.y)
        else:
            pyautogui.leftClick(locate.x, locate.y)

class _Battle(_MissionType):
    def __init__(self) -> None:
        super().__init__()
        self.pic = [r'resources/bangpai/fanwen.png', r'resources/bangpai/qiecuo.png']

    def complete(self, locate, **kwargs):
        # 点击战斗后退出战斗
        pyautogui.leftClick(locate.x, locate.y)


class _Hanhua(_MissionType):
    def __init__(self) -> None:
        super().__init__()
        self.pic = r'resources/bangpai/hanhua.png'


class _Xunluo(_MissionType):

    def completeMark(self):
        # 完成一次战斗
        pass


class _Guaji(_Xunluo):
    def complete(self, locate, **kwargs):
        # 每次战斗后15秒不再次进入战斗 现在是不断点击追踪
        pass


class Bangpai:
    # 其他类型不断点击追踪做就完了，找不到特征判断
    _mayMissionList = [_Wupin(), _Battle(), _Fanwen(), _Hanhua()]

    # 有特征图片的任务
    def _findPic(self):
        itemIdx = None
        for idx, each in enumerate(self._mayMissionList):
            if each.pic is None:
                continue
            locate = None
            if isinstance(each.pic, list):
                for iid, item in enumerate(each.pic):
                    locate = pyautogui.locateCenterOnScreen(item, confidence=0.9)
                    itemIdx = iid
                    if locate is not None:
                        break
            else:
                locate = pyautogui.locateCenterOnScreen(each.pic, confidence=0.9)
            if locate is not None:
                return idx, locate, itemIdx
        return None, None, None

    def do(self, chaseWin):
        while True:
            pyautogui.leftClick(chaseWin[0], chaseWin[1])
            idx, locate, itemIdx = self._findPic()
            while locate is None:
                if battling(battleingPic=r'resources/origin/zhen_tian.png'):
                    cooldown(4)
                idx, locate, itemIdx = self._findPic()
                cooldown(1)
                if locate is None:
                    # 没法判断特征图片的任务都能通过不断点击追踪完成
                    pyautogui.leftClick(chaseWin[0], chaseWin[1])
                cooldown(1)

            self._mayMissionList[idx].complete(locate, itemIdx=itemIdx)
            cooldown(1)


# 大窗口
if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    log("start task....")
    init()
    Bangpai().do((winRelativeX(-0.5), winRelativeY(6 + 0)))
