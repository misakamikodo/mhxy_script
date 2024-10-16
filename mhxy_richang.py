from mhxy_baotu import *
from mhxy_dati import *
from mhxy_mijing import *
from mhxy_yabiao import *

# 秘境、押镖、答题、宝图
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-ir', '--idxArray', required=False, default='0', type=str)
    parser.add_argument('-m', '--mission', required=False, default='baotu,mijing,dati,yabiao', type=str)
    parser.add_argument('-sd', '--shutdown', required=False, default="False", type=str)
    parser.add_argument('-w', '--wait', required=False, default="False", type=str)
    args = parser.parse_args()
    missionSet = set(args.mission.split(","))
    cooldown(1)
    indexArr = args.idxArray.split(',')

    def func(idx):
        config = init(idx=idx)
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

    if args.wait == "True":
        time = datetime.datetime.now()
        while datetime.datetime.now() - time < datetime.timedelta(minutes=3):
            # 一定要小于一次战斗的时间
            cooldown(5)
            if pyautogui.locateOnScreen(r'resources/small/enter_battle_flag.png', confidence=0.9) is not None:
                time = datetime.datetime.now()
        allEscapeTeam(bugFix=True)

    if len(indexArr) != 1:
        for each in indexArr:
            func(int(each))
    else:
        func(int(indexArr[0]))

    if args.shutdown == "True":
        os.system("shutdown -s")




