import argparse

from mhxy_baotu import *
from mhxy_dati import *
from mhxy_mijing import *
from mhxy_yabiao import *

# 秘境、押镖、答题、宝图
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', default=0, type=int)
    args = parser.parse_args()
    cooldown(1)
    # 早上跑一次宝图秘境
    config = init(idx=args.idx)
    baotu = Baotu(config=config)
    if gotoActivity(r'resources/richang/baotu.png'):
       baotu.mission()
    baotu.do()
    if gotoActivity(r'resources/richang/mijing.png'):
        MiJing(config=config).do()
    DaTi(config=config).do()
    if gotoActivity(r'resources/richang/yabiao.png'):
        YaBiao(config=config).do()

    # config = init(idx=1)
    # baotu = Baotu(config=config)
    # if gotoActivity(r'resources/richang/baotu.png'):
    #    baotu.mission()
    # baotu.do()
    # if gotoActivity(r'resources/richang/mijing.png'):
    #     MiJing(config=config).do()
    # DaTi(config=config).do()
    # if gotoActivity(r'resources/richang/yabiao.png'):
    #     YaBiao(config=config).do()
