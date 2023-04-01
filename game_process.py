import os

from mhxy import *


class GameProcess:
    moveOffset = (60, 20)

    def __moveZhuomianbanFunc(self, size):
        windows = pyautogui.getAllWindows()
        zhuomianban = (71, 963)
        i = 0
        for item in list(filter(lambda x: x.title.startswith("梦幻西游："), windows)):
            item.activate()
            print(item)
            pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
            pyautogui.dragTo(item.left + (size[0] - resizeOffset[0]), item.top + (size[1] - resizeOffset[1]),
                             duration=1)
            if item.left < 0:
                print("notSafe")
            else:
                pyautogui.moveTo(item.left + self.moveOffset[0], item.top + self.moveOffset[1])
                cooldown(1)
                pyautogui.dragTo(zhuomianban[i] + self.moveOffset[0], 0 + self.moveOffset[1], duration=1)
                i += 1
            print("处理后：", item)

    def moveZhuomianban(self):
        self.__moveZhuomianbanFunc(niceSize)

    def moveZhuomianban2Origin(self):
        windows = pyautogui.getAllWindows()
        item = list(filter(lambda x: x.title.startswith("梦幻西游"), windows))[0]
        item.activate()
        print(item)
        pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
        pyautogui.dragTo(item.left + (originSize[0] - resizeOffset[0]), item.top + (originSize[1] - resizeOffset[1]),
                         duration=1)
        cooldown(3)
        print("处理后：", item)

    def moveMoniqi(self):
        global niceSize, resizeOffset, windows, item
        moniqi = (64, 969)
        niceSize = (907, 545)
        resizeOffset = (1, 2)
        windows = pyautogui.getAllWindows()
        i = 0
        windowsList = list(filter(lambda x: x.title.startswith("MuMu模拟器"), windows))

        def splitFun(title):
            s = title.split("-", 2)
            return int(s[1]) if len(s) > 1 else 0

        windowsList.sort(key=lambda x: splitFun(x.title))
        for item in windowsList:
            item.activate()
            print(item)
            pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
            pyautogui.dragTo(item.left + (niceSize[0] - resizeOffset[0]), item.top + (niceSize[1] - resizeOffset[1]),
                             duration=1)
            pyautogui.dragTo(item.left + (niceSize[0] - resizeOffset[0]), item.top + (niceSize[1] - resizeOffset[1]),
                             duration=1)
            if item.left < 0:
                print("notSafe")
            else:
                pyautogui.moveTo(item.left + self.moveOffset[0], item.top + self.moveOffset[1])
                cooldown(1)
                pyautogui.dragTo(moniqi[i] + self.moveOffset[0], 496 + self.moveOffset[1], duration=1)
                pyautogui.dragTo(moniqi[i] + self.moveOffset[0], 496 + self.moveOffset[1], duration=1)
                i += 1
            print("处理后：", item)


    def closeMoniqi(self):
        #根据进程名杀死进程 NemuPlayer.exe QtWebEngineProcess.exe NemuHeadless.exe || mymain.exe CCMini.exe
        pro = 'taskkill /f /im %s'% 'NemuHeadless.exe'
        os.system(pro)
        pro = 'taskkill /f /im %s'% 'QtWebEngineProcess.exe'
        os.system(pro)

if __name__ == '__main__':
    resize = GameProcess()
    resize.moveZhuomianban()
    # resize.moveZhuomianban2Origin()
    # resize.moveMoniqi()
