from mhxy_ghost import *
from mhxy_mine_withshop import *
from mhxy_shopping2 import *

# 晚上挂机
if __name__ == '__main__':
    try:
        print("start task....")
        # cf = CheckFuben()

        # print("跟队520")
        # cf = CheckFuben()
        # cf.main()
        # while datetime.datetime.now().hour <= 2:
        #     cooldown(60)

        # 2
        print("抢公示")
        shopping = Shopping2()
        shopping.openSop()
        shopping.shopping2()
        shopping.close()

        # 2
        # print("抢公示2")
        # shopping = Shopping3()
        # shopping.shopping3()
        # shopping.close()

        # 2
        print("挖矿")
        mine = Mine()
        mine.mineMain()

        # print("捉鬼")
        # ghost = Ghost(idx = 0)
        # ghost.maxRound = 10
        # ghost.getDialog()
        # ghost.ghost()

        # 1
        # print("收非珍品")
        # shopping = Shopping()
        # shopping.hour = 5
        # shopping.do()
        # shopping.closeShop()

        # 2
        # print("挖矿WithShop")
        # mine = MineWithShop()
        # mine.mineMain()

        # 1
        # print("收非珍品")
        # shopping = Shopping()
        # shopping.hour = 7
        # shopping.openShop()
        # shopping.do()

        # print("挖矿2")
        # mine = Mine(idx=1)
        # mine.mineMain()

        print("关机")
        # shopping.close()
        # if datetime.datetime.now().hour != 7:
        #     pl.playsound('resources/common/music.mp3')
        os.system("shutdown -s")
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
