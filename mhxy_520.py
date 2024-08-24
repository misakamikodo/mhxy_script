from mhxy_fuben import *
from mhxy_ghost import *

# 520
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', default=0, type=int)
    # xiashi50,norm70,norm50_1,norm50_2
    parser.add_argument('-m', '--mission', default='xiashi50,norm70,norm50_1,norm50_2', type=str)
    parser.add_argument('-gr', '--ground', default=2, type=int)
    parser.add_argument('-sd', '--shutdown', default="False", type=str)
    args = parser.parse_args()

    def func(idx):
        try:
            log("start task....")
            fuben = Fuben(mission=args.mission.split(","),
                          idx=idx)
            fuben.do()
            ghost = Ghost(idx=idx)
            ghost.maxRound = args.ground
            ghost.go()
            ghost.do()
            # pl.playsound('resources/common/music.mp3')
        except (FailSafeException):
            pl.playsound('resources/common/music.mp3')

    if args.idx == -1:
        i = 0
        while args.idx == -1 and len(getWindowList()) > i:
            func(i)
            i = i + 1
    else:
        func(args.idx)

    if args.shutdown == "True":
        os.system("shutdown -s")
