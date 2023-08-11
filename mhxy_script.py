from tkinter import *

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
        # python只能通过标志符结束进程，部分程序没有设计结束标志。所以暂时放着不实现了。手动关闭窗口或者鼠标移动到边缘关闭吧
        target.stop()
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
    ghostBtn.place(x=40, y=60, anchor=NW)


def packFuben():
    def change2Fuben():
        changeThread(Fuben(changWinPos=False))

    fubenBtn = myButton(root, text='副本', width=8, command=change2Fuben)
    fubenBtn.place(x=130, y=60, anchor=NW)

def packMenpai():
    def changMission():
        changeThread(Menpai(changWinPos=False))

    fubenBtn = myButton(root, text='门派', width=8, command=changMission)
    fubenBtn.place(x=40, y=100, anchor=NW)

def packHaidi():
    def changMission():
        changeThread(Haidi(changWinPos=False))

    fubenBtn = myButton(root, text='海底', width=8, command=changMission)
    fubenBtn.place(x=130, y=100, anchor=NW)

def packMihunta():
    def changMission():
        changeThread(Mihunta(changWinPos=False))

    fubenBtn = myButton(root, text='迷魂塔', width=8, command=changMission)
    fubenBtn.place(x=40, y=140, anchor=NW)


def packBangpai():
    global bangpaiBtn

    def change2bangpai():
        changeThread(Bangpai(changWinPos=False))

    bangpaiBtn = myButton(root, text='帮派任务', width=8, command=change2bangpai)
    bangpaiBtn.place(x=130, y=140, anchor=NW)


def packMine():
    def change2Mine():
        changeThread(Mine(changWinPos=False))

    mineBtn = myButton(root, text='挖矿', width=8, command=change2Mine)
    mineBtn.place(x=90, y=230, anchor=NW)

# 界面程序 此部分封装了参数没有大量写死的程序
# pyinstaller --onefile --noconsole mhxy_script.py
if __name__ == '__main__':
    root = Tk()
    root.title("mhxy_script")
    root.geometry('260x430')
    x = int((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)
    y = int((root.winfo_screenheight() - root.winfo_reqheight()) / 2)
    # 将窗口居中显示
    root.geometry("+{}+{}".format(x, y))
    # root.iconbitmap('mhxy.ico')
    gameProcess = GameProcess()

    smallWinBtn = myButton(root, text='初始化为小窗口', width=12, command=gameProcess.moveZhuomianban)
    smallWinBtn.place(x=80, y=10, anchor=NW)

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
    # 帮派任务
    packBangpai()
    # ================原始大小窗口

    originWinBtn = myButton(root, text='初始化为原始窗口', width=12, command=gameProcess.moveZhuomianban2Origin)
    originWinBtn.place(x=80, y=180, anchor=NW)

    # 挖矿
    packMine()

    t = Text(root, width=32, height=10)
    t.insert(END, "说明\n"
                  "1 如果出现后台运行的程序无法关闭情况，请通过关闭本窗口程序关闭正在运行的脚本。\n"
                  "2 程序不受控可以通过将鼠标快速移动到右上角强制终止。\n"
                  "3 对应功能程序配置文件和说明放在resources下相应文件夹内\n"
             )
    t.place(x=10, y=270, anchor=NW)

    packStop()
    root.mainloop()
