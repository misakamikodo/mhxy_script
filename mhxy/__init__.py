import datetime
import json
import logging
import threading
import time

import playsound as pl
import pyautogui
import pyperclip
from pygetwindow import PyGetWindowException, BaseWindow

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个处理器，用于写入日志文件
fh = logging.FileHandler('mhxy_script.log')
fh.setLevel(logging.DEBUG)
# 添加到 logger 中
logger.addHandler(fh)


class Frame:
    left = 0
    top = 0
    right = 0
    bottom = 0

    def __init__(self, left, top):
        self.left = left
        self.top = top

    def __str__(self):
        return "left:" + str(self.left) + " top:" + str(self.top) + " right:" + str(self.right) + " bottom:" + str(
            self.bottom)

# 窗口左上侧位置 init后修改
frame = Frame(0, 0)

# 窗口固定大小
originSize = [1040, 807]
smallSize = (907, 707)
# 鼠标到变化态需要向做微调距离
resizeOffset = (10, 7)
frameSize = [0, 0]

frameOriginSizeCm = [28.1, 21.8]
frameSizeCm = [28.1, 21.8]

def relativeSize(x, y):
    return (frameSize[0] * x / frameSizeCm[0],
            frameSize[1] * y / frameSizeCm[1])


def relativeX2Act(xCm):
    return frameSize[0] * abs(xCm) / frameSizeCm[0]


def relativeY2Act(yCm):
    return frameSize[1] * abs(yCm) / frameSizeCm[1]


def winRelativeX(x):
    return frame.right - relativeX2Act(x) if x < 0 else frame.left + relativeX2Act(x)


def winRelativeY(y):
    return frame.bottom - relativeY2Act(y) if y < 0 else frame.top + relativeY2Act(y)


def winRelativeXY(x, y):
    return (winRelativeX(x), winRelativeY(y))


# 百分比方法不是很实用，因为窗口大小变化，ui并不是百分比变化的
def percentX(x):
    return frameSize[0] * (abs(x) / 100)


def percentY(y):
    return frameSize[1] * (abs(y) / 100)


def winPercentX(x):
    return frame.right - percentX(x) if x < 0 else frame.left + percentX(x)


def winPercentY(y):
    return frame.bottom - percentY(y) if y < 0 else frame.top + percentY(y)


def winPercentXY(x, y):
    return (winPercentX(x), winPercentY(y))


def battling(battleingPic=r'resources/origin/zhen_tian.png'):
    return Util.locateOnScreen(battleingPic) is not None

def notBattling(notBattlingPic):
    return Util.locateOnScreen(notBattlingPic) is not None


# 关闭任务侧边栏
def closeMission():
    Util.leftClick(-7, 4.3)
    # print("关闭任务侧边栏")
    # pyautogui.hotkey('alt', 'p')

# 结束战斗后进行操作
def escapeBattleDo(do,
                   notBattlingPic=None,
                   battleingPic=r'resources/small/enter_battle_flag.png',
                   battleDoFunc=None):
    alreadyDo = False
    battleDo = False
    while True:
        if (battleingPic is not None and not battling(battleingPic=battleingPic)) or \
                (notBattlingPic is not None and notBattling(notBattlingPic)):
            battleDo = False
            if not alreadyDo:
                # 脱离战斗
                print("escape battle")
                cooldown(1.5)
                alreadyDo = True
                do()
                cooldown(2)
            else:
                # 战斗外当已完成了动作
                cooldown(2)
        else:
            # 战斗中
            alreadyDo = False
            if not battleDo:
                # 进入战斗
                print("enter battle")
                cooldown(3)
                battleDo = True
                # 进入战斗后做一次
                if battleDoFunc is not None:
                    battleDoFunc()
                cooldown(2)
            else:
                # 战斗中当已完成了动作
                cooldown(2)



def doUtilFindPic(pic, do, warnTimes=None):
    def find():
        if isinstance(pic, list):
            for idx, each in enumerate(pic):
                locate = Util.locateCenterOnScreen(each)
                if locate is not None:
                    return locate, idx
            return None, None
        else:
            return Util.locateCenterOnScreen(pic), None

    locate, idx = find()
    # 最少执行一次
    times = 0
    while locate is None:
        do(locate, idx=idx, times=times)
        locate, idx = find()
        times+=1
        cooldown(1)
        if warnTimes is not None and times>warnTimes:
            naozhong = threading.Thread(target=pl.playsound('resources/common/music.mp3'))
            # 闹钟提醒
            naozhong.start()
    return locate, idx

def waitUtilFindPic(pic):
    def do():
        cooldown(1)
    doUtilFindPic(pic, do)

# 副本式任务
def doNormFubenMission():
    def reach():
        return Util.locateCenterOnScreen(r'resources/fuben/select.png')

    # 流程任务
    def do():
        reachPos = reach()
        while reachPos is None:
            def clickSkip():
                Util.leftClick(-1, -2)

            # 找不到头像则正在对话点击头像位置跳过 直到找到头像位置
            doUtilFindPic(r'resources/avatar.png', clickSkip)
            reachPos = reach()
            cooldown(2)
        pyautogui.leftClick(reachPos.x, reachPos.y)

    escapeBattleDo(do)


def cooldown(second):
    time.sleep(max(0, second))


class Util:

    @staticmethod
    def __openCVEnable():
        __openCVEnable = True
        try:
            import cv2
        except ImportError:
            __openCVEnable = False
        return __openCVEnable

    @staticmethod
    def locateCenterOnScreen(pic, confidence=0.9):
        cfd = confidence if Util.__openCVEnable() else None
        if isinstance(pic, list):
            res = None
            for i in pic:
                if cfd is not None:
                    res = pyautogui.locateCenterOnScreen(i, region=(frame.left, frame.top, frame.right, frame.bottom),
                                                         confidence=cfd)
                else:
                    res = pyautogui.locateCenterOnScreen(i, region=(frame.left, frame.top, frame.right, frame.bottom))
                if res is not None:
                    return res
            return res
        else:
            if cfd is not None:
                return pyautogui.locateCenterOnScreen(pic, region=(frame.left, frame.top, frame.right, frame.bottom),
                                                      confidence=cfd)
            else:
                return pyautogui.locateCenterOnScreen(pic,
                                                      region=(frame.left, frame.top, frame.right, frame.bottom))

    @staticmethod
    def locateOnScreen(pic, confidence=0.9):
        cfd = confidence if Util.__openCVEnable() else None
        if cfd is not None:
            return pyautogui.locateOnScreen(pic, region=(frame.left, frame.top, frame.right, frame.bottom), confidence=cfd)
        else:
            return pyautogui.locateOnScreen(pic, region=(frame.left, frame.top, frame.right, frame.bottom))

    @staticmethod
    def leftClick(x, y):
        pyautogui.leftClick(winRelativeX(x), winRelativeY(y))

    @staticmethod
    def doubleClick(x, y):
        pyautogui.doubleClick(winRelativeX(x), winRelativeY(y))

    @staticmethod
    def click(x, y, clicks, buttons):
        pyautogui.click(winRelativeX(x), winRelativeY(y), clicks=clicks, button=buttons)

    @staticmethod
    def write(text):
        # 不支持中文
        # pyautogui.typewrite(text)
        pyperclip.copy(text)
        # print(pyperclip.paste())
        pyautogui.hotkey('Ctrl', 'v')


def resize2Small(windows):
    while not windows.isActive:
        cooldown(1)
    pyautogui.moveTo(windows.right - resizeOffset[0], windows.bottom - resizeOffset[1])
    pyautogui.dragTo(windows.left + (smallSize[0] - resizeOffset[0]), windows.top + (smallSize[1] - resizeOffset[1]),
                     duration=1.3)
'''
@:param resizeToSmall 是否修改窗口为小窗口
@:param changWinPos 窗口位置是否发生移动
'''
def init(idx=0, resizeToSmall=False, changWinPos=True):
    global frameSizeCm
    global frame

    def getFrameSize(idx) -> BaseWindow:
        window = None
        while window is None or window.left < 0:
            windowsList = pyautogui.getWindowsWithTitle('梦幻西游：时空')
            windowsList = list(filter(lambda x: x.left > 0, windowsList))
            windowsList.sort(key=lambda x: x.left)

            moniqiWin = list(filter(lambda x: x.left > 0 and (x.title.startswith("MuMu模拟器12") or x.title.startswith("梦幻西游 - ")), pyautogui.getAllWindows()))
            moniqiWin.sort(key=lambda x: x.left)
            for each in moniqiWin:
                windowsList.append(each)

            if len(windowsList) > 0:
                window = windowsList[idx]
            cooldown(0.5)
        if window is not None:
            frameSize[0] = window.width
            frameSize[1] = window.height
        return window

    # 如果你是使用notepad++中添加命令运行则需要修改下工作目录，比如
    # os.chdir("D:\workspace\pyproject\mhxy_script")
    # pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
    pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常

    # location1 = Util.locateOnScreen(r'resources/mine_head.png')
    windows = getFrameSize(idx)
    print("窗口大小:", frameSize)
    print("窗口大小CM:", frameSizeCm)
    if resizeToSmall:
        resize2Small(windows)
        windows = getFrameSize(idx)
        print("调整后窗口大小:", frameSize)
    if resizeToSmall or frameSize[0] == smallSize[0]:
        frameSizeCm = [frameOriginSizeCm[0] * (smallSize[0] / originSize[0]), frameOriginSizeCm[1] * (smallSize[1] / originSize[1])]
        print("调整后窗口大小CM:", frameSizeCm)
    else:
        frameSizeCm = frameOriginSizeCm
    try:
        windows.activate()
    except PyGetWindowException:
        pass
    if frame.left == 0 or changWinPos:
        frame.left = windows.left
        frame.top = windows.top
        frame.right = frame.left + frameSize[0]
        frame.bottom = frame.top + frameSize[1]
        print("窗口四角位置:", frame)


def parse_request(request):
    raw_list = request.split("\r\n")
    # GET /search?sourceid=chrome&ie=UTF-8&q=ergterst HTTP/1.1
    fst = raw_list[0].split(' ')
    request = {"method": fst[0], "url": fst[1]}
    for index in range(1, len(raw_list)):
        item = raw_list[index].split(":")
        if len(item) == 2:
            request.update({item[0].lstrip(' '): item[1].lstrip(' ')})
    return request

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


class PicNode(object):

    def __init__(self, elem, completeFunc=None):
        if completeFunc is None:
            self.completeFunc = self.complete
        else:
            self.completeFunc = completeFunc
        self.elem = elem
        # [PicNode]
        self.next = None

    def complete(self, locate, chaseWin):
        pyautogui.leftClick(locate.x, locate.y)
        cooldown(0.5)
        # 叶子节点需要关闭对话
        Util.leftClick(chaseWin[0], chaseWin[1])

    def setNext(self, nxt):
        self.next = nxt
        # 防止卡了的情况，自己下一个包含自己
        self.next.append(self)

    def __str__(self) -> str:
        return str(self.elem)

class MhxyScriptInterrupt(Exception):
    pass

class MhxyScript:
    # 程序运行标志
    _flag = True

    def __init__(self, idx=0, changWinPos=True, resizeToSmall=False) -> None:
        init(idx=idx, resizeToSmall=resizeToSmall, changWinPos=changWinPos)

    def interruptWork(self):
        raise MhxyScriptInterrupt()

    def stop(self):
        self._flag = False

    def do(self):
        pass