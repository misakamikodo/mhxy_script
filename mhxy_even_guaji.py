from pyautogui import FailSafeException

from mhxy_mine_withshop import *
from mhxy_other_fuben import *
from mhxy_shopping2 import *
from mhxy_shopping import *
from mhxy_fuben import *
from mhxy_ghost import *
from game_process import *

# 晚上挂机
if __name__ == '__main__':
    try:
        print("start task....")
        # print("跟队520")
        # cf = CheckFuben()
        # cf.main()
        # while datetime.datetime.now().hour <= 2:
        #     cooldown(60)

        # print("抢公示")
        # shopping = Shopping2()
        # shopping.openSop()
        # shopping.shopping2()
        # shopping.close()

        # print("捉鬼")
        # ghost = Ghost(idx = 0)
        # ghost.maxRound = 4
        # ghost.getDialog()
        # ghost.ghost()
        # process = GameProcess()
        # process.closeMoniqi()
        # process.moveZhuomianban2Origin()

        print("挖矿")
        mine = MineWithShop()
        mine.mineMain()

        # print("挖矿2")
        # mine = Mine(idx=1)
        # mine.mineMain()

        print("收非珍品")
        shopping = Shopping()
        shopping.hour = 9
        shopping.openShop()
        shopping.do()

        print("关机")
        # shopping.close()
        os.system("shutdown -s")
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
