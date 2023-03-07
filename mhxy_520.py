from pyautogui import FailSafeException

from mhxy_fuben import *
from mhxy_ghost import *

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
        fuben.config['lastFuben'] = r'resources/fuben/jinchanxin.png'
        # fuben.config['lastFuben'] = r'resources/fuben/erchongying.png'
        fuben.config['avatar'] = r'resources/small/avatar_gjl.png'
        # fuben.config['avatar'] = r'resources/small/avatar_spl.png'
        fuben.config['avatar'] = r'resources/small/avatar_mll.png'
        fuben.config['zhen'] = r'resources/small/zhen_tian.png'
        # fuben.config['zhen'] = r'resources/small/zhen_long.png'
        fuben.fuben()

        ghost = Ghost(idx=0)
        ghost.maxRound = 5
        ghost.go()
        ghost.ghost()
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
