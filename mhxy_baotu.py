import argparse
import os
from configparser import ConfigParser

from mhxy import *


class Baotu(MhxyScript):
    _chasepos = 2


    def __init__(self, idx=0, changWinPos=True, resizeToSmall=False, config=None, stopCheck=None) -> None:
        super().__init__(idx, changWinPos, resizeToSmall, config, stopCheck=stopCheck)
        file_path = os.path.join(os.path.abspath('.'), 'resources/richang/richang.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")
        conn = ConfigParser()
        conn.read(file_path)
        chasepos = float(conn.get('main', 'baotupos'))
        self._chasepos = chasepos

    def _find_baotu(self):
        baotuLocation = Util.locateCenterOnScreen('resources/baotu/baotu_item.png', confidence=0.85)
        if baotuLocation is not None:
            return baotuLocation
        for _ in range(0, 2):
            pyautogui.moveTo(winRelativeX(17.3), winRelativeY(6))
            pyautogui.dragTo(winRelativeX(17.3), winRelativeY(14), duration=0.3)
            cooldown(1)
        for _ in range(0, 3):
            pyautogui.moveTo(winRelativeX(17.3), winRelativeY(14))
            pyautogui.dragTo(winRelativeX(17.3), winRelativeY(6), duration=0.8)
            cooldown(1)
            baotuLocation = Util.locateCenterOnScreen('resources/baotu/baotu_item.png')
            if baotuLocation is not None:
                return baotuLocation
            cooldown(2)

    def _run_baotu(self):
        Util.leftClick(23, 16)
        cooldown(0.5)
        baotuLocation = self._find_baotu()
        if baotuLocation is None:
            Util.leftClick(-2.5, 3)
            return False
        pyautogui.doubleClick(baotuLocation.x, baotuLocation.y)
        return True


    def mission(self):
        def locateBaotuMission():
            ms = Util.locateCenterOnScreen(r'resources/richang/baotu_mission.png',
                                           region=(
                                           int(frame.left + frameSize[0] / 2), frame.top, int(frameSize[0] / 2), frameSize[1]),
                                           confidence=0.8)
            return ms
        cooldown(0.5)
        ms = locateBaotuMission()
        if ms is not None:
            pyautogui.leftClick(ms.x, ms.y)
        else:
            waitThenClickUtilFindPic(r'resources/richang/baotu_mission_start.png')
        cooldown(0.5)
        ms = locateBaotuMission()
        if ms is not None:
            pyautogui.doubleClick(ms.x, ms.y)
        else:
            Util.doubleClick(-3, 3.8 + self._chasepos * 2)
        # 等待任务完成
        timep = datetime.datetime.now()
        btl = battling()
        while btl or datetime.datetime.now() - timep < datetime.timedelta(minutes=1, seconds=30):
            if btl:
                timep = datetime.datetime.now()
            cooldown(10)
            btl = battling()
        ms = locateBaotuMission()
        if ms is not None:
            self.mission()
        log("end")

    def do(self):
        # 关闭九转、九幽地狱提示弹窗
        # dialog = Util.locateCenterOnScreen('resources/baotu/baotu_dialog.png')
        # if dialog is not None:
        #     pyautogui.leftClick(dialog.x, dialog.y)
        cooldown(1)
        if self._run_baotu() is False:
            return
        i = 0
        while self._stopCheck():
            useBaotuLocation = Util.locateCenterOnScreen('resources/baotu/use_baotu.png')
            # 防止点到包裹
            if useBaotuLocation is not None and useBaotuLocation.x < frame.right - relativeX2Act(1.8):
                cooldown(0.5)
                pyautogui.leftClick(useBaotuLocation.x,
                                    useBaotuLocation.y + 50)
                # log("挖宝图中 ", useBaotuLocation)
                i = 0
            cooldown(2)
            i += 1
            if i % 60 == 0:
                return
                # 3分钟没有宝图可以挖了，可能就是没宝图了，再检测一下
                # if self.run_baotu() is False:
                #     return
                # i = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-ir', '--idxArray', required=False, default='0', type=str)
    args = parser.parse_args()
    indexArr = args.idxArray.split(',')

    def func(idx):
        Baotu(idx=idx).do()

    if len(indexArr) != 1:
        for each in indexArr:
            func(int(each))
    else:
        func(int(indexArr[0]))
