from pyautogui import FailSafeException

from mhxy_fuben import *
from mhxy_ghost import *

# 晚上挂机
if __name__ == '__main__':
    try:
        print("start task....")
        fuben = Fuben(idx=0)
        fuben.config['lastFuben'] = r'resources/fuben/jinchanxin.png'
        # fuben.config['lastFuben'] = r'resources/fuben/erchongying.png'
        fuben.config['avatar'] = r'resources/small/avatar_gjl.png'
        # fuben.config['avatar'] = r'resources/small/avatar_spl.png'
        # fuben.config['avatar'] = r'resources/small/avatar_mll.png'
        fuben.config['zhen'] = r'resources/small/zhen_tian.png'
        fuben.fuben()

        ghost = Ghost(picNo=0)
        ghost.maxRound = 2
        ghost.go()
        ghost.ghost()
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
