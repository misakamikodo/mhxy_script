from tkinter import *
from tkinter.ttk import Separator

from game_process import *
from mhxy_bangpai2 import *
from mhxy_fuben import *
from mhxy_ghost import *
from mhxy_haidi import *
from mhxy_menpai import *
from mhxy_mihunta import *
from mhxy_mine import *

_backgroundThread = None

class MyThread(threading.Thread):
    def __init__(self, target, daemon=True):
        super(MyThread, self).__init__(target=target, daemon=daemon)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

def myButton(root, text, width, command):
    return Button(root, text=text, width=width, bg='white', activebackground='grey', activeforeground='black',
                  font=('微软雅黑', 8),
                  command=command)


def changeThread(target):
    global _backgroundThread
    if _backgroundThread is not None:
        # FIXME python只能通过标志符结束进程，部分程序没有设计结束标志。所以暂时放着不实现了。手动关闭窗口或者鼠标移动到边缘关闭吧
        _backgroundThread.stop()
    _backgroundThread = MyThread(target=target.do, daemon=True)
    _backgroundThread.start()


def packStop():
    global bangpaiBtn

    def change2None():
        global _backgroundThread
        if _backgroundThread is not None:
            _backgroundThread.stop()
        _backgroundThread = None

    bangpaiBtn = myButton(root, text='停止当前任务', width=12, command=change2None)
    bangpaiBtn.pack(side=BOTTOM, expand=NO)


def packGhost():
    def change2Ghost():
        changeThread(Ghost(changWinPos=False))

    ghostBtn = myButton(root, text='捉鬼', width=8, command=change2Ghost)
    ghostBtn.pack(side=TOP, expand=NO)


def packFuben():
    def change2Fuben():
        changeThread(Fuben(changWinPos=False))

    fubenBtn = myButton(root, text='副本', width=8, command=change2Fuben)
    fubenBtn.pack(side=TOP, expand=NO)

def packMenpai():
    def changMission():
        changeThread(Menpai(changWinPos=False))

    fubenBtn = myButton(root, text='门派', width=8, command=changMission)
    fubenBtn.pack(side=TOP, expand=NO)

def packHaidi():
    def changMission():
        changeThread(Haidi(changWinPos=False))

    fubenBtn = myButton(root, text='海底', width=8, command=changMission)
    fubenBtn.pack(side=TOP, expand=NO)

def packMihunta():
    def changMission():
        changeThread(Mihunta(changWinPos=False))

    fubenBtn = myButton(root, text='迷魂塔', width=8, command=changMission)
    fubenBtn.pack(side=TOP, expand=NO)


def packMine():
    def change2Mine():
        changeThread(Mine(changWinPos=False))

    mineBtn = myButton(root, text='挖矿', width=8, command=change2Mine)
    mineBtn.pack(side=TOP, expand=NO)


def packBangpai():
    global bangpaiBtn

    def change2bangpai():
        changeThread(Bangpai(changWinPos=False))

    bangpaiBtn = myButton(root, text='帮派任务', width=8, command=change2bangpai)
    bangpaiBtn.pack(side=TOP, expand=NO)


if __name__ == '__main__':
    root = Tk()
    root.title("mhxy_script")
    root.geometry('300x500')
    # root.iconbitmap('mhxy.ico')
    gameProcess = GameProcess()

    smallWinBtn = myButton(root, text='初始化为小窗口', width=12, command=gameProcess.moveZhuomianban)
    smallWinBtn.pack(side=TOP, expand=NO)

    # 抓鬼
    packGhost()

    # 副本
    packFuben()
    # 门派
    packMenpai()
    # 海底
    packHaidi()
    # 迷魂塔
    packMihunta()
    # ================原始大小窗口
    sep = Separator(root, orient=HORIZONTAL)
    sep.pack(padx=10, fill=X)

    originWinBtn = myButton(root, text='初始化为原始窗口', width=12, command=gameProcess.moveZhuomianban2Origin)
    originWinBtn.pack(side=TOP, expand=NO)

    # 挖矿
    packMine()

    # 帮派任务
    packBangpai()

    packStop()
    root.mainloop()
