from mhxy_fuben import *
from mhxy_ghost_withshop import *

# 晚上挂机
if __name__ == '__main__':
    try:
        print("start task....")
        fuben = Fuben(idx=0)
        fuben.fubenPos = [
            # ("xiashi", 13, 15),
            ("xiashi", 7, 15),

            ("norm", 19, 15),
            ("norm", 13, 15),
            ("norm", 7, 15)
        ]
        fuben.do()

        ghost = Ghost(idx=0)
        ghost.maxRound = 2
        ghost.chasepos = 1
        ghost.go()
        ghost.do()
        # pl.playsound('resources/common/music.mp3')
        # os.system("shutdown -s")
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
