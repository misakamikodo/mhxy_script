from mhxy_baotu import *
from mhxy_dati import *
from mhxy_fuben import *
from mhxy_ghost import *
from mhxy_mijing import *
from mhxy_yabiao import *

# 520
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', required=False, default=0, type=int)
    # xiashi50,norm70,norm50_1,norm50_2
    parser.add_argument('-m', '--mission', required=False, default='xiashi50,norm70,norm50_1,norm50_2', type=str)
    parser.add_argument('-gr', '--ground', required=False, default=2, type=int)
    parser.add_argument('-rc', '--richang', required=False, default="False", type=str)
    parser.add_argument('-sd', '--shutdown', required=False, default="False", type=str)
    args = parser.parse_args()

    def func(idx):
        try:
            log("start task....")
            missionArr = args.mission.split(",")
            print(missionArr)
            if len(missionArr) > 0:
                fuben = Fuben(mission=missionArr, idx=idx)
                fuben.do()

            if args.ground > 0:
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

    # 如果日常勾选了，关机交给日常执行
    if args.richang != "True" and args.shutdown == "True":
        os.system("shutdown -s")
    elif args.richang == "True":
        allEscapeTeam(bugFix=True)
        i = 0
        while len(getWindowList()) > i:
            config = init(idx=i)
            baotu = Baotu(config=config)
            if gotoActivity(r'resources/richang/baotu.png'):
               baotu.mission()
            baotu.do()
            if gotoActivity(r'resources/richang/mijing.png'):
                MiJing(config=config).do()
            DaTi(config=config).do()
            if gotoActivity(r'resources/richang/yabiao.png'):
                YaBiao(config=config).do()
            i = i + 1
        if args.shutdown == "True":
            os.system("shutdown -s")
