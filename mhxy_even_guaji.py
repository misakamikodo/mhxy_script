from game_process import *
from mhxy_baotu import Baotu
from mhxy_ghost import *
from mhxy_mijing import MiJing
from mhxy_shopping2 import *

# 挖矿、抢公示
if __name__ == '__main__':
    # os.chdir(r"/")
    try:
        pyautogui.PAUSE = 0.1
        # log("start task....")

        # 2
        log("抢公示")
        shopping = Shopping2()
        # shopping.openSop()
        shopping.shopping2()
        shopping.close()

        # 1
        # log("收非珍品")
        # shopping = Shopping()
        # shopping.hour = 5
        # shopping.openShop()
        # shopping.do()
        # shopping.close()

        # log("挖矿")
        # mine = Mine(idx=0)
        # mine.do()

        # 3
        # mine = Mine(idx=1)
        # mine.do()

        # log("捉鬼")
        # ghost = Ghost(idx = 0)
        # ghost.maxRound = 10
        # ghost.getDialog()
        # ghost.ghost()

        # 清一波日常
        g = GameProcess()
        g.moveZhuomianbanVertical()

        config = init(idx=0)
        baotu = Baotu(config=config)
        if gotoActivity(r'resources/richang/baotu.png'):
           baotu.mission()
        baotu.do()
        if datetime.datetime.now().weekday() != 0 and gotoActivity(r'resources/richang/mijing.png'):
            MiJing(config=config).do()

        log("关机")
        # shopping.close()
        # if datetime.datetime.now().hour != 7:
        #     pl.playsound('resources/common/music.mp3')
        os.system("shutdown -s")
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
