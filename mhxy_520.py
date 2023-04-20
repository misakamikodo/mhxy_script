from mhxy_fuben import *
from mhxy_ghost_withshop import *

# 晚上挂机
if __name__ == '__main__':
    try:
        print("start task....")
        fuben = Fuben(idx=0)
        fuben.xiashi_fix = 5.6
        fuben.fubenPos = [
            # ("xiashi", 13, 15),
            ("xiashi", 7, 15),

            ("norm", 19, 15),
            ("norm", 13, 15),
            ("norm", 7, 15)
        ]
        fuben.fuben()

        ghost = Ghost(idx=0)
        ghost.maxRound = 5
        ghost.chasepos = 1
        ghost.go()
        ghost.ghost()
        pl.playsound('resources/common/music.mp3')
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
