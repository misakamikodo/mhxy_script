from mhxy_baotu import *
from mhxy_dati import *
from mhxy_mijing import *
from mhxy_yabiao import *

# 秘境、押镖、答题、宝图
if __name__ == '__main__':
    cooldown(1)
    config = init(idx=1)
    if gotoActivity(r'resources/richang/baotu.png'):
       baotu = Baotu(config=config)
       baotu.mission()
       baotu.do()

    if gotoActivity(r'resources/richang/mijing.png'):
        MiJing(config=config).do()

    DaTi(config=config).do()

    if gotoActivity(r'resources/richang/yabiao.png'):
        YaBiao(config=config).do()
