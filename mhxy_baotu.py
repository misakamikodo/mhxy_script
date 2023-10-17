from mhxy import *

class Baotu(MhxyScript):

    def find_baotu(self):
        for _ in range(0, 3):
            pyautogui.moveTo(winRelativeX(17.3), winRelativeY(13))
            pyautogui.dragTo(winRelativeX(17.3), winRelativeY(6), duration=0.8)
            baotuLocation = Util.locateOnScreen('resources/baotu/baotu_item.png')
            if baotuLocation is not None:
                return baotuLocation
            cooldown(2)

    def run_baotu(self):
        Util.leftClick(23, 16)
        cooldown(0.5)
        baotuLocation = self.find_baotu()
        if baotuLocation is None:
            return False
        pyautogui.doubleClick(baotuLocation.left + baotuLocation.width - 50,
                            baotuLocation.top + baotuLocation.height - 20)
        return True


    def do(self):
        if self.run_baotu() is False:
            return
        i = 0
        while self._flag:
            useBaotuLocation = Util.locateOnScreen('resources/baotu/use_baotu.png')
            if useBaotuLocation is not None:
                cooldown(0.5)
                pyautogui.leftClick(useBaotuLocation.left + useBaotuLocation.width - 50,
                                    useBaotuLocation.top + useBaotuLocation.height - 20)
                # print("挖宝图中 ", useBaotuLocation)
                i = 0
            cooldown(2)
            i += 1
            if i % 60 == 0: # 3分钟没有宝图可以挖了，可能就是没宝图了，再检测一下
                if self.run_baotu() is False:
                    return
                i = 0


if __name__ == '__main__':
    Baotu().do()
