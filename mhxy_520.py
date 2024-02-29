from mhxy_fuben import *
from mhxy_ghost import *

# 520
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', default=0, type=int)
    # xiashi50,norm70,norm50_1,norm50_2
    parser.add_argument('-m', '--mission', default='xiashi50,norm70,norm50_1,norm50_2', type=str)
    parser.add_argument('-gr', '--ground', default=5, type=int)
    parser.add_argument('-gp', '--gpos', default=1, type=float)
    parser.add_argument('-sd', '--shutdown', default="False", type=str)
    args = parser.parse_args()
    try:
        log("start task....")
        fuben = Fuben(mission=args.mission.split(","),
                      idx=args.idx)
        fuben.do()
        ghost = Ghost(idx=args.idx)
        ghost.maxRound = args.ground
        ghost.chasepos = args.gpos
        ghost.go()
        ghost.do()
        # pl.playsound('resources/common/music.mp3')
        if args.shutdown == "True":
            os.system("shutdown -s")
    except (FailSafeException):
        pl.playsound('resources/common/music.mp3')
