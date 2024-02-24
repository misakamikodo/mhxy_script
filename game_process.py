import argparse
import os

from mhxy import *


class GameProcess:
    _moveOffset = (60, 20)

    def __moveZhuomianbanFunc(self, size, target=None):
        windows = pyautogui.getAllWindows()
        zhuomianban = (71, 964, 71)
        i = 0
        winList = list(filter(lambda x: x.title.startswith("梦幻西游："), windows))
        if target is not None:
            winList.sort(key=lambda x: (x.left / 4, x.top))
            winList = [winList[min(target, len(winList)-1)]]
        for item in winList:
            item.activate()
            log(item)
            if item.left < 0:
                log("notSafe")
            pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
            pyautogui.dragTo(item.left + (size[0] - resizeOffset[0]), item.top + (size[1] - resizeOffset[1]),
                             duration=1)
            pyautogui.moveTo(item.left + self._moveOffset[0], item.top + self._moveOffset[1])
            cooldown(1)
            sz = pyautogui.size()
            # 这里任务栏写死36
            no2LineTop = (sz.height-item.height-36 if sz.height-item.height*2<0 else item.height)*int(i/2)
            pyautogui.dragTo(zhuomianban[i] + self._moveOffset[0], no2LineTop + self._moveOffset[1], duration=1)
            i += 1
            log("处理后：", item)

    def moveZhuomianbanVertical(self):
        windows = pyautogui.getAllWindows()
        sz = pyautogui.size()
        no3LineTop = (sz.height - 707 - 36 if sz.height - 707 * 3 < 0 else 707*2 + 1)
        zhuomianban = (0, 707 + 1, no3LineTop)
        i = 0
        for item in list(filter(lambda x: x.title.startswith("梦幻西游："), windows)):
            item.activate()
            log(item)
            if item.left < 0:
                log("notSafe")
            pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
            pyautogui.dragTo(item.left + (smallSize[0] - resizeOffset[0]), item.top + (smallSize[1] - resizeOffset[1]),
                             duration=1)
            pyautogui.moveTo(item.left + self._moveOffset[0], item.top + self._moveOffset[1])
            cooldown(1)
            pyautogui.dragTo(71 + self._moveOffset[0], zhuomianban[i] + self._moveOffset[1], duration=1)
            i += 1
            log("处理后：", item)

    def moveZhuomianban(self, target=None):
        self.__moveZhuomianbanFunc(smallSize, target=target)

    def moveZhuomianban2Origin(self):
        windows = pyautogui.getAllWindows()
        item = list(filter(lambda x: x.title.startswith("梦幻西游"), windows))[0]
        item.activate()
        log(item)
        pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
        pyautogui.dragTo(item.left + (originSize[0] - resizeOffset[0]), item.top + (originSize[1] - resizeOffset[1]),
                         duration=1)
        cooldown(3)
        log("处理后：", item)

    def moveMoniqi(self):
        self.__moveMoniqiFunc(smallSize)

    def __moveMoniqiFunc(self, size):
        windows = pyautogui.getAllWindows()
        i = 0
        for item in list(filter(lambda x: x.title.startswith("MuMu模拟器12") or x.title.startswith("梦幻西游 - "), windows)):
            item.activate()
            log(item)
            if item.left < 0:
                log("notSafe")
            pyautogui.moveTo(item.right - 5, item.top + 15)
            pyautogui.dragTo(item.left + (size[0] - 5), item.top + 15,
                             duration=1)
            i += 1
            log("处理后：", item)


    def closeMoniqi(self):
        #根据进程名杀死进程 NemuPlayer.exe QtWebEngineProcess.exe NemuHeadless.exe || mymain.exe CCMini.exe
        pro = 'taskkill /f /im %s'% 'NemuHeadless.exe'
        os.system(pro)
        pro = 'taskkill /f /im %s'% 'QtWebEngineProcess.exe'
        os.system(pro)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-s', '--size', default='small', type=str)
    parser.add_argument('-d', '--direct', default='horizontal', type=str)
    parser.add_argument('--type', default='zhuomian', type=str)
    args = parser.parse_args()

    resize = GameProcess()
    if args.type == "zhuomian":
        if args.size == 'small':
            if args.direct == 'horizontal':
                resize.moveZhuomianban()
            else:
                resize.moveZhuomianbanVertical()
        else:
            resize.moveZhuomianban2Origin()
    else:
        resize.moveMoniqi()
    # 模拟器分辨率设置为：1600*1095 再调整窗口大小可使用脚本
    # resize.moveMoniqi()
