import os
import sys
import threading
import time

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from qtpy.QtCore import (Qt)

from game_process import GameProcess
from ui.dialog.bangpai_cfg_dialog import BangpaiCfgDialog
from ui.dialog.baotu_cfg_dialog import BaotuCfgDialog
from ui.dialog.ghost_cfg_dialog import GhostCfgDialog
from ui.dialog.menpai_cfg_dialog import MenpaiCfgDialog
from ui.win.script import Ui_MainWindow as main_win


class StopAbleThread(threading.Thread):
    def __init__(self, target, daemon=True, args=()):
        super(StopAbleThread, self).__init__(target=target, daemon=daemon, args=args)
        self.stop_event = threading.Event()

    def stopFlag(self):
        return self.stop_event.isSet()

    def stop(self):
        self.stop_event.set()

class MhxyApplication(QMainWindow, main_win):
    BN = 0
    _threadMap = {}

    def __init__(self):
        super(MhxyApplication, self).__init__()
        self.setupUi(self)
        self.baotu_cfg_btn.clicked.connect(self.openBaotuCfgDialog)
        self.ghost_cfg_btn.clicked.connect(self.openGhostCfgDialog)
        self.menpai_cfg_btn.clicked.connect(self.openMenpaiCfgDialog)
        self.bangpai2_cfg_btn.clicked.connect(self.openBangpaiCfgDialog)
        self.game_process_small_btn.clicked.connect(self.gamoprocess2Small)
        self.game_process_origin_btn.clicked.connect(self.gamoprocess2Origin)
        self.log_btn.clicked.connect(self.openLog)
        self.close_mission_btn.clicked.connect(self.closeTask)
        # 日常
        self.batch_richang.clicked.connect(self.richangTask)
        self.baotu_btn.clicked.connect(self.baotuTask)
        self.mijing_btn.clicked.connect(self.mijingTask)
        self.dati_btn.clicked.connect(self.datiTask)
        self.yabiao_btn.clicked.connect(self.tabiaoTask)
        # 520
        self.batch_mission520.clicked.connect(self.mission520Task)
        self.fuben_xiashi70_btn.clicked.connect(self.xiashi70Task)
        self.fuben_xiashi50_btn.clicked.connect(self.xiashi50Task)
        self.fuben_norm70_btn.clicked.connect(self.norm70Task)
        self.fuben_norm50_btn2.clicked.connect(self.norm50Task2)
        self.fuben_norm50_btn1.clicked.connect(self.norm50Task1)
        self.ghost2_btn.clicked.connect(self.ghost2Task)
        self.ghost5_btn.clicked.connect(self.ghost5Task)
        self.ghost_btn.clicked.connect(self.ghostTask)
        # 周常
        self.menpai_btn.clicked.connect(self.menpaiTask)
        self.haidi_btn.clicked.connect(self.haidiTask)
        self.mihunta_btn.clicked.connect(self.mihuntaTask)
        # 工具
        self.batch_tool_btn.clicked.connect(self.toolTask)
        self.shopping1_btn.clicked.connect(self.shopping1Task)
        self.shopping2_btn.clicked.connect(self.shopping2Task)
        self.shopping3_btn.clicked.connect(self.shopping3Task)
        self.mine_btn.clicked.connect(self.mineTask)
        self.bangpai2_btn.clicked.connect(self.bangpai2Task)

        def threadMapCheck(threadName):
            while True:
                rmKey=[]
                for key in self._threadMap:
                    value = self._threadMap[key]
                    if not value.is_alive():
                        rmKey.append(key)
                for each in rmKey:
                    self._threadMap.pop(each)
                    for item in self.listWidget.items():
                        self.listWidget.takeItem(self.listWidget.row(item))
                time.sleep(10)

        threadMapCheckThread = StopAbleThread(target=threadMapCheck, daemon=True, args=("threadMapCheckThread", ))
        threadMapCheckThread.start()

    # 工具
    def toolTask(self):
        arr=[]
        if self.shopping1_rdo.isChecked():
            arr.append(self.shopping1_btn.text())
        elif self.shopping2_rdo.isChecked():
            arr.append(self.shopping2_btn.text())
        elif self.shopping3_rdo.isChecked():
            arr.append(self.shopping3_btn.text())
        if self.mine_chk.isChecked():
            arr.append(self.mine_btn.text())
        if self.tool_shutdown_chk.isChecked():
            pass
        self.addTask("test", f'批量任务[{str.join(",",arr)}]')

    def shopping1Task(self):
        self.addTask("test", f'{self.shopping1_btn.text()}')

    def shopping2Task(self):
        self.addTask("test", f'{self.shopping2_btn.text()}')

    def shopping3Task(self):
        self.addTask("test", f'{self.shopping3_btn.text()}')

    def mineTask(self):
        self.addTask("test", f'{self.mine_btn.text()}')

    def bangpai2Task(self):
        self.addTask("test", f'{self.bangpai2_btn.text()}')


    # 周常
    def menpaiTask(self):
        self.addTask("test", f'{self.menpai_btn.text()}')

    def haidiTask(self):
        self.addTask("test", f'{self.haidi_btn.text()}')

    def mihuntaTask(self):
        self.addTask("test", f'{self.mihunta_btn.text()}')


    # 多人日常任务

    def mission520Task(self):
        arr=[]
        fubenNum=0
        if self.xiashi70_chk.isChecked():
            fubenNum+=1
        if self.xiashi50_chk.isChecked():
            fubenNum+=1
        if self.norm70_chk.isChecked():
            fubenNum+=1
        if self.norm50_chk2.isChecked():
            fubenNum+=1
        if self.norm50_chk1.isChecked():
            fubenNum+=1
        if fubenNum>=1:
            arr.append(f"{fubenNum}本")
        if self.ghost_chk.isChecked():
            if self.ghost_2_rdo.isChecked():
                arr.append(self.ghost2_btn.text())
            elif self.ghost_5_rdo.isChecked():
                arr.append(self.ghost5_btn.text())
            elif self.ghost_rdo.isChecked():
                rd = int(self.ghost_ipt.text())
                arr.append(f"{rd}鬼")
        if self.mission520_shutdown_chk.isChecked():
            pass
        self.addTask("test", f'多人日常[{str.join(",",arr)}]')

    def xiashi70Task(self):
        self.addTask("test", f'{self.fuben_xiashi70_btn.text()}')

    def xiashi50Task(self):
        self.addTask("test", f'{self.fuben_xiashi50_btn.text()}')

    def norm70Task(self):
        self.addTask("test", f'{self.fuben_norm70_btn.text()}')

    def norm50Task2(self):
        self.addTask("test", f'{self.fuben_norm50_btn2.text()}')

    def norm50Task1(self):
        self.addTask("test", f'{self.fuben_norm50_btn1.text()}')

    def ghost2Task(self):
        self.addTask("test", f'{self.ghost2_btn.text()}')

    def ghost5Task(self):
        self.addTask("test", f'{self.ghost5_btn.text()}')

    def ghostTask(self):
        rd = int(self.ghost_ipt.text())
        self.addTask("test", f'{rd}{self.ghost_btn.text()}')


    # 日常

    def richangTask(self):
        arr=[]
        if self.baotu_chk.isChecked():
            arr.append(self.baotu_btn.text())
        if self.mijing_chk.isChecked():
            arr.append(self.mijing_btn.text())
        if self.dati_chk.isChecked():
            arr.append(self.dati_btn.text())
        if self.yabiao_chk.isChecked():
            arr.append(self.yabiao_btn.text())
        self.addTask("test", f'单人日常[{str.join(",",arr)}]')

    def baotuTask(self):
        def testThread(threadName):
            def stopCheck():
                return self._threadMap.get(threadName).stopFlag()
            raise KeyError
            # b = Baotu(stopCheck=stopCheck)
            # b.do()

        th = "baotu"
        _backgroundThread = StopAbleThread(target=testThread, daemon=True, args=(th, ))
        self._threadMap[th] = _backgroundThread
        _backgroundThread.start()
        self.addTask(th, f'{self.baotu_btn.text()}')

    def mijingTask(self):
        self.addTask("test", f'{self.mijing_btn.text()}')

    def datiTask(self):
        self.addTask("test", f'{self.dati_btn.text()}')

    def tabiaoTask(self):
        self.addTask("test", f'{self.yabiao_btn.text()}')

    # 配置对话框

    def openGhostCfgDialog(self):
        popup = GhostCfgDialog()
        popup.exec()

    def openBaotuCfgDialog(self):
        popup = BaotuCfgDialog()
        popup.exec()

    def openMenpaiCfgDialog(self):
        popup = MenpaiCfgDialog()
        popup.exec()

    def openBangpaiCfgDialog(self):
        popup = BangpaiCfgDialog()
        popup.exec()

    # 界面互动

    def gamoprocess2Small(self):
        g = GameProcess()
        g.moveZhuomianban2Origin()

    def gamoprocess2Origin(self):
        g = GameProcess()
        if self.target_left_rdo.isChecked():
            g.moveZhuomianban(0)
        else:
            g.moveZhuomianban(1)

    def openLog(self):
        os.system(f'notepad.exe mhxy_script.log')

    def addTask(self, bindThread, text):
        lwi = QListWidgetItem(text)
        lwi.setData(Qt.UserRole, bindThread)
        self.listWidget.addItem(lwi)

    def closeTask(self):
        target = self.listWidget.selectedItems()
        for each in target:
            self.listWidget.takeItem(self.listWidget.row(each))
            threadName = each.data(Qt.UserRole)
            if threadName is not None and self._threadMap.get(threadName) is not None:
                self._threadMap.get(threadName).stop()
                # self._threadMap.pop(threadName)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MyUiStart = MhxyApplication()
    MyUiStart.setFixedSize(MyUiStart.width(), MyUiStart.height())
    MyUiStart.show()
    app.exec()
