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
        baotuLocation = Util.locateOnScreen('resources/baotu/baotu_item.png', confidence=0.85)
        if baotuLocation is not None:
            return baotuLocation
        pyautogui.moveTo(winRelativeX(17.3), winRelativeY(6))
        pyautogui.dragTo(winRelativeX(17.3), winRelativeY(13), duration=0.3)
        for _ in range(0, 2):
            pyautogui.moveTo(winRelativeX(17.3), winRelativeY(13))
            pyautogui.dragTo(winRelativeX(17.3), winRelativeY(6), duration=0.8)
            baotuLocation = Util.locateOnScreen('resources/baotu/baotu_item.png')
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
        pyautogui.doubleClick(baotuLocation.left + baotuLocation.width - 50,
                            baotuLocation.top + baotuLocation.height - 20)
        return True


    def mission(self):
        cooldown(0.5)
        waitUtilFindPic(r'resources/fuben/select.png')
        Util.leftClick(-3, 13.5)
        cooldown(0.5)
        ms = Util.locateCenterOnScreen(r'resources/richang/baotu_mission.png', confidence=0.8)
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
        ms = Util.locateCenterOnScreen(r'resources/richang/baotu_mission.png', confidence=0.8)
        if ms is not None:
            self.mission()
        log("end")


    def do(self):
        if self._run_baotu() is False:
            return
        i = 0
        while self._stopCheck():
            useBaotuLocation = Util.locateCenterOnScreen('resources/baotu/use_baotu.png')
            if useBaotuLocation is not None:
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
    Baotu().do()
