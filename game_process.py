import argparse

from mhxy import *


class GameProcess:

    def __moveZhuomianbanFunc(self, size, target=None):
        winList = getWindowList()
        zhuomianban = (0, smallSize[0] - 15, smallSize[0] * 2 - 30, int(smallSize[0] / 2) - 15, int(smallSize[0] / 2) + smallSize[0] - 30)
        i = 0
        if target is not None:
            winList.sort(key=lambda x: (x.left, x.top))
            winList = [winList[min(target, len(winList) - 1)]]
        for idx, item in enumerate(winList):
            log(item)
            item.resizeTo(smallSize[0], smallSize[1])
            cooldown(1)
            sz = pyautogui.size()
            # 这里任务栏写死36
            no2LineTop = (sz.height - item.height - 36 if sz.height - item.height * 2 < 0 else item.height) * int(
                i / 3)
            item.moveTo(zhuomianban[i], no2LineTop)
            i += 1
            log("处理后：", item)

    def moveZhuomianbanVertical(self):
        windows = pyautogui.getAllWindows()
        sz = pyautogui.size()
        i = 0
        for item in list(filter(lambda x: x.title.startswith("梦幻西游："), windows)):
            log(item)
            item.resizeTo(smallSize[0], smallSize[1])
            item.moveTo(int((sz.width - smallSize[0]) / 2),
                        int(min(i * (smallSize[1] - 15), sz.height - smallSize[1] - 36)))
            cooldown(1)
            i += 1
            log("处理后：", item)

    def moveZhuomianban(self, target=None):
        self.__moveZhuomianbanFunc(smallSize, target=target)

    def moveZhuomianban2Origin(self):
        windows = pyautogui.getAllWindows()
        item = list(filter(lambda x: x.title.startswith("梦幻西游"), windows))[0]
        log(item)
        item.resizeTo(originSize[0], originSize[1])
        cooldown(3)
        log("处理后：", item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-tg', '--target', required=False, default=None, type=int)
    parser.add_argument('-s', '--size', default='small', type=str)
    parser.add_argument('-d', '--direct', default='h', type=str)
    parser.add_argument('--type', default='zhuomian', type=str)
    args = parser.parse_args()

    resize = GameProcess()
    if args.size == 'small':
        if args.direct == 'h':
            resize.moveZhuomianban(target=args.target)
        else: # v
            resize.moveZhuomianbanVertical()
    else:
        resize.moveZhuomianban2Origin()
    # 模拟器分辨率设置为：1600*1095 再调整窗口大小可使用脚本
    # resize.moveMoniqi()
