import argparse

from mhxy import *


class GameProcess:
    _moveOffset = (60, 20)

    def __moveZhuomianbanFunc(self, size, target=None):
        winList = getWindowList()
        zhuomianban = (71, 964, 71, 964)
        i = 0
        if target is not None:
            winList.sort(key=lambda x: (x.left, x.top))
            winList = [winList[min(target, len(winList) - 1)]]
        for idx, item in enumerate(winList):
            log(item)
            item.resizeTo(smallSize[0], smallSize[1])
            cooldown(1)
            sz = pyautogui.size()
            if idx == 4:
                p = (sz.width - item.width) / 2, (sz.height - item.height) / 2
                item.moveTo(int(p[0]), int(p[1]))
            else:
                # 这里任务栏写死36
                no2LineTop = (sz.height - item.height - 36 if sz.height - item.height * 2 < 0 else item.height) * int(
                    i / 2)
                item.moveTo(zhuomianban[i], no2LineTop)
                i += 1
            log("处理后：", item)

    def moveZhuomianbanVertical(self):
        windows = pyautogui.getAllWindows()
        sz = pyautogui.size()
        no3LineTop = (sz.height - 707 - 36 if sz.height - 707 * 3 < 0 else 707 * 2 + 1)
        zhuomianban = (0, 707 + 1, no3LineTop)
        i = 0
        for item in list(filter(lambda x: x.title.startswith("梦幻西游："), windows)):
            log(item)
            item.resizeTo(smallSize[0], smallSize[1])
            pyautogui.moveTo(item.left + self._moveOffset[0], item.top + self._moveOffset[1])
            cooldown(1)
            item.moveTo(71, zhuomianban[i])
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
    parser.add_argument('-d', '--direct', default='horizontal', type=str)
    parser.add_argument('--type', default='zhuomian', type=str)
    args = parser.parse_args()

    resize = GameProcess()
    if args.size == 'small':
        if args.direct == 'horizontal':
            resize.moveZhuomianban(target=args.target)
        else:
            resize.moveZhuomianbanVertical()
    else:
        resize.moveZhuomianban2Origin()
    # 模拟器分辨率设置为：1600*1095 再调整窗口大小可使用脚本
    # resize.moveMoniqi()
