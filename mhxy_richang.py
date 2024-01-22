from mhxy_baotu import *
from mhxy_dati import *
from mhxy_mijing import *
from mhxy_yabiao import *

# 秘境、押镖、答题、宝图
if __name__ == '__main__':
    cooldown(1)
    if datetime.datetime.now().hour <= 18:
        # 早上跑一次宝图秘境
        config = init(idx=0)
        baotu = Baotu(config=config)
        if gotoActivity(r'resources/richang/baotu.png'):
           baotu.mission()
        baotu.do()
        if gotoActivity(r'resources/richang/mijing.png'):
            MiJing(config=config).do()
        config = init(idx=1)
        baotu = Baotu(config=config)
        if gotoActivity(r'resources/richang/baotu.png'):
           baotu.mission()
        baotu.do()
        if gotoActivity(r'resources/richang/mijing.png'):
            MiJing(config=config).do()
    else:
        # 晚上跑一次答题押镖
        config = init(idx=0)
        DaTi(config=config).do()
        if gotoActivity(r'resources/richang/yabiao.png'):
            YaBiao(config=config).do()
        config = init(idx=1)
        DaTi(config=config).do()
        if gotoActivity(r'resources/richang/yabiao.png'):
            YaBiao(config=config).do()
