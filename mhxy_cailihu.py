from mhxy import *


class Cailiwu:
    _caiguode = []

    def quanfuCailiwu(self):
        itemY = 1
        for i in range(0, 10):
            y = 1
            for i in range(0, 4):
                # 资料
                Util.leftClick(1, y)
                # 空间
                Util.leftClick(1, 1)
                # 踩
                Util.leftClick(1, 1)
                # 关闭
                Util.leftClick(1, 1)
                y += itemY
            pyautogui.moveTo(winRelativeX(1), winRelativeY(1))
            pyautogui.dragTo(winRelativeX(1), winRelativeY(1), duration=1.3)

    def cailiwu(self):
        while True:
            gift = pyautogui.locateCenterOnScreen(r'resources/gift.png',
                                                  region=(
                                                  winRelativeX(1), winRelativeY(1), winRelativeX(1), winRelativeY(1)),
                                                  confidence=0.9)
            if gift is not None:
                # 查看id
                Util.leftClick(1, 1)
                hanzi = Util.oci((winRelativeX(1), winRelativeY(1), winRelativeX(1), winRelativeY(1)), type="number")
                if hanzi not in self._caiguode:
                    # 空间
                    Util.leftClick(1, 1)
                    # 踩
                    Util.leftClick(1, 1)
                    # 关闭
                    Util.leftClick(1, 1)
                    self._caiguode.append(hanzi)
                else:
                    # 关闭明细
                    Util.leftClick(1, 1)

            cooldown(2)


# 喊话
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    init()
    Cailiwu().cailiwu()
