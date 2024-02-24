from mhxy_baotu import *
from mhxy_dati import *
from mhxy_mijing import *
from mhxy_yabiao import *

# 秘境、押镖、答题、宝图
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', default=0, type=int)
    parser.add_argument('-m', '--mission', default='baotu,mijing,dati,yabiao', type=str)
    args = parser.parse_args()
    missionSet = set(args.mission.split(","))
    cooldown(1)
    # 早上跑一次宝图秘境
    config = init(idx=args.idx)
    if 'baotu' in missionSet:
        baotu = Baotu(config=config)
        if gotoActivity(r'resources/richang/baotu.png'):
           baotu.mission()
        baotu.do()
    if 'mijing' in missionSet:
        if gotoActivity(r'resources/richang/mijing.png'):
            MiJing(config=config).do()
    if 'dati' in missionSet:
        DaTi(config=config).do()
    if 'yabiao' in missionSet:
        if gotoActivity(r'resources/richang/yabiao.png'):
            YaBiao(config=config).do()
