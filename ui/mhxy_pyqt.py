import os
import sys
from configparser import ConfigParser

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from qtpy.QtCore import (Qt)

from dialog.bangpai_cfg_dialog import BangpaiCfgDialog
from dialog.baotu_cfg_dialog import BaotuCfgDialog
from dialog.ghost_cfg_dialog import GhostCfgDialog
from dialog.linlongshi_cfg_dialog import LinlongshiCfgDialog
from dialog.menpai_cfg_dialog import MenpaiCfgDialog
from dialog.mihunta_cfg_dialog import MihuntaCfgDialog
from win.script import Ui_MainWindow as main_win


class MhxyApplication(QMainWindow, main_win):
    BN = 0
    _threadMap = {}
    conn = None
    file_path = None
    singleChkMode = False

    def __init__(self):
        super(MhxyApplication, self).__init__()
        self.setupUi(self)
        self.baotu_cfg_btn.clicked.connect(self.openBaotuCfgDialog)
        self.ghost_cfg_btn.clicked.connect(self.openGhostCfgDialog)
        self.menpai_cfg_btn.clicked.connect(self.openMenpaiCfgDialog)
        self.bangpai2_cfg_btn.clicked.connect(self.openBangpaiCfgDialog)
        self.linlongshi_cfg_btn.clicked.connect(self.openLinlongshiCfgDialog)
        self.mihunta_cfg_btn.clicked.connect(self.openMihuntaCfgDialog)
        self.game_process_small_btn.clicked.connect(self.gamoprocess2Small)
        self.game_process_origin_btn.clicked.connect(self.gamoprocess2Origin)
        self.log_btn.clicked.connect(self.openLog)
        # self.close_mission_btn.clicked.connect(self.closeTask)
        self.run_customer_btn.clicked.connect(self.runCustomerTask)
        # regexp = QRegularExpression(r"[a-zA-Z]:(\\[\w\u4e00-\u9fa5-{}][\w\u4e00-\u9fa5\s-{}])([.a-z-{}\\]{0,99}[\w\u4e00-\u9fa5-{}])*")
        # validator_regx = QRegularExpressionValidator(self)
        # validator_regx.setRegularExpression(regexp)
        # self.lineEdit.setValidator(validator_regx)
        self.file_path = os.path.join(os.path.abspath('.'), r'script.ini')
        dir = self.lineEdit.text()
        self.conn = ConfigParser()
        if os.path.exists(self.file_path):
            self.conn.read(self.file_path)
            dir = self.conn.get('main', 'dir')
        if dir == "" or dir is None:
            dir = os.path.abspath('.').replace("\\ui", "")
            if self.conn.has_section("main"):
                self.conn.set('main', 'dir', dir)
                self.conn.write(open(self.file_path, 'w'))
        self.cusomer_ipt.setText(self.conn.get('main', 'lastscript'))
        self.lineEdit.setText(dir)
        os.chdir(dir)
        self.lineEdit.textChanged.connect(self.dirChange)
        self.tabWidget.currentChanged.connect(self.tabWidgetChange)
        self.target_rdo_allchk.clicked.connect(self.allChk)
        self.target_rdo_nochk.clicked.connect(self.noChk)
        self.target_rdo1.clicked.connect(self.chk1)
        self.target_rdo2.clicked.connect(self.chk2)
        self.target_rdo3.clicked.connect(self.chk3)
        self.target_rdo4.clicked.connect(self.chk4)
        self.target_rdo5.clicked.connect(self.chk5)
        # 日常
        self.batch_richang.clicked.connect(self.richangTask)
        self.baotu_btn.clicked.connect(self.baotuTask)
        self.mijing_btn.clicked.connect(self.mijingTask)
        self.dati_btn.clicked.connect(self.datiTask)
        self.yabiao_btn.clicked.connect(self.yabiaoTask)
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
        self.shopping1_btn.clicked.connect(self.shopping1Task)
        self.shopping2_btn.clicked.connect(self.shopping2Task)
        self.shopping3_btn.clicked.connect(self.shopping3Task)
        # self.mine_btn.clicked.connect(self.mineTask)
        self.bangpai2_btn.clicked.connect(self.bangpai2Task)
        self.linlongshi_btn.clicked.connect(self.linlongshiTask)
        self.auto_battle_btn.clicked.connect(self.autoBattleTask)
        # temp
        # self.listWidget.hide()
        # self.close_mission_btn.hide()
        # self.label.hide()

    def exec_script(self, target, args=""):
        # subprocess.check_call(f'python {self.lineEdit.text()}\\{target}.py {args}')
        cmd = f'start python{"" if self.black_win.isChecked() else "w"} "{self.lineEdit.text()}\\{target}.py" {args}'
        print("执行脚本：" + cmd)
        res = os.system(cmd)

    def dirChange(self, content):
        os.chdir(content)
        # print(content)

    def tabWidgetChange(self, evt):
        self.singleChkMode = evt != 0
        if self.singleChkMode:
            rdo = [self.target_rdo1, self.target_rdo2, self.target_rdo3, self.target_rdo4, self.target_rdo5]
            for radio in rdo:
                if radio.isChecked():
                    index = rdo.index(radio)
                    for next_radio in rdo[index + 1:]:
                        next_radio.setChecked(False)
                    break

    def allChk(self, evt):
        self.target_rdo1.setChecked(True)
        self.target_rdo2.setChecked(True)
        self.target_rdo3.setChecked(True)
        self.target_rdo4.setChecked(True)
        self.target_rdo5.setChecked(True)

    def noChk(self, evt):
        self.target_rdo1.setChecked(False)
        self.target_rdo2.setChecked(False)
        self.target_rdo3.setChecked(False)
        self.target_rdo4.setChecked(False)
        self.target_rdo5.setChecked(False)

    def chk(self, no):
        if self.singleChkMode:
            rdo = [self.target_rdo1,self.target_rdo2,self.target_rdo3,self.target_rdo4,self.target_rdo5]
            for i in range(0, 5):
                if i != no:
                    rdo[i].setChecked(False)

    def chk1(self, evt):
        self.chk(0)

    def chk2(self, evt):
        self.chk(1)

    def chk3(self, evt):
        self.chk(2)

    def chk4(self, evt):
        self.chk(3)

    def chk5(self, evt):
        self.chk(4)

    def shopping1Task(self):
        self.exec_script('mhxy_shopping1')
        self.addTask("test", f'{self.shopping1_btn.text()}')

    def shopping2Task(self):
        self.exec_script('mhxy_shopping2')
        self.addTask("test", f'{self.shopping2_btn.text()}')

    def shopping3Task(self):
        self.exec_script('mhxy_shopping3')
        self.addTask("test", f'{self.shopping3_btn.text()}')

    # def mineTask(self):
    #     self.exec_script('mhxy_mine')
    #     self.addTask("test", f'{self.mine_btn.text()}')

    def autoBattleTask(self):
        if self.auto_battle_none_rdo.isChecked():
            self.exec_script('mhxy_auto_battle', f'-i {self.getTarget()}')
        elif self.auto_battle_jingjichang_rdo.isChecked():
            self.exec_script('mhxy_auto_battle', f'-i {self.getTarget()} -t jingjichang')
        elif self.auto_battle_huashang_rdo.isChecked():
            self.exec_script('mhxy_auto_battle', f'-i {self.getTarget()} -t huashang')
        elif self.auto_battle_linglongshi_rdo.isChecked():
            self.exec_script('mhxy_auto_battle', f'-i {self.getTarget()} -t linglongshi')
        self.addTask("test", f'{self.bangpai2_btn.text()}')

    def bangpai2Task(self):
        self.exec_script('mhxy_bangpai2', f'-i {self.getTarget()}')
        self.addTask("test", f'{self.bangpai2_btn.text()}')

    def linlongshiTask(self):
        self.exec_script('mhxy_linlongshi', f'-i {self.getTarget()}')
        self.addTask("test", f'{self.linlongshi_btn.text()}')

    # 周常
    def menpaiTask(self):
        self.exec_script('mhxy_menpai', f'-i {self.getTarget()}')
        self.addTask("test", f'{self.menpai_btn.text()}')

    def haidiTask(self):
        self.exec_script('mhxy_haidi', f'-i {self.getTarget()}')
        self.addTask("test", f'{self.haidi_btn.text()}')

    def mihuntaTask(self):
        self.exec_script('mhxy_mihunta', f'-i {self.getTarget()}')
        self.addTask("test", f'{self.mihunta_btn.text()}')

    # 多人日常任务

    def mission520Task(self):
        mission = []
        ground = 2
        arr = []
        fubenNum = 0
        if self.xiashi70_chk.isChecked():
            fubenNum += 1
            mission.append("xiashi70")
        if self.xiashi50_chk.isChecked():
            fubenNum += 1
            mission.append("xiashi50")
        if self.norm70_chk.isChecked():
            fubenNum += 1
            mission.append("norm70")
        if self.norm50_chk2.isChecked():
            fubenNum += 1
            mission.append("norm50_1")
        if self.norm50_chk1.isChecked():
            fubenNum += 1
            mission.append("norm50_2")
        if fubenNum >= 1:
            arr.append(f"{fubenNum}本")
        if self.ghost_chk.isChecked():
            mission.append("ghost")
            if self.ghost_2_rdo.isChecked():
                ground=2
                arr.append(self.ghost2_btn.text())
            elif self.ghost_5_rdo.isChecked():
                ground=5
                arr.append(self.ghost5_btn.text())
            elif self.ghost_rdo.isChecked():
                rd = int(self.ghost_ipt.text())
                ground=rd
                arr.append(f"{rd}鬼")
        self.exec_script('mhxy_520', f'-i {self.getTarget()} '
                                     f'-m {str.join(",", mission)} '
                                     f'-gr {ground} '
                                     f'-rc {self.richang_chk.isChecked()} '
                                     f'--shutdown {self.mission520_shutdown_chk.isChecked()}')
        self.addTask("test", f'多人日常[{str.join(",", arr)}]')

    def xiashi70Task(self):
        self.exec_script('mhxy_fuben', f'-i {self.getTarget()} -m xiashi70')
        self.addTask("test", f'{self.fuben_xiashi70_btn.text()}')

    def xiashi50Task(self):
        self.exec_script('mhxy_fuben', f'-i {self.getTarget()} -m xiashi50')
        self.addTask("test", f'{self.fuben_xiashi50_btn.text()}')

    def norm70Task(self):
        self.exec_script('mhxy_fuben', f'-i {self.getTarget()} -m norm70')
        self.addTask("test", f'{self.fuben_norm70_btn.text()}')

    def norm50Task2(self):
        self.exec_script('mhxy_fuben', f'-i {self.getTarget()} -m norm50_1')
        self.addTask("test", f'{self.fuben_norm50_btn2.text()}')

    def norm50Task1(self):
        self.exec_script('mhxy_fuben', f'-i {self.getTarget()} -m norm50_2')
        self.addTask("test", f'{self.fuben_norm50_btn1.text()}')

    def ghost2Task(self):
        self.exec_script('mhxy_ghost', f'-i {self.getTarget()} -r 2')
        self.addTask("test", f'{self.ghost2_btn.text()}')

    def ghost5Task(self):
        self.exec_script('mhxy_ghost', f'-i {self.getTarget()} -r 5')
        self.addTask("test", f'{self.ghost5_btn.text()}')

    def ghostTask(self):
        rd = int(self.ghost_ipt.text())
        self.exec_script('mhxy_ghost', f'-i {self.getTarget()} -r {rd}')
        self.addTask("test", f'{rd}{self.ghost_btn.text()}')

    # 日常

    def richangTask(self):
        mission = []
        arr = []
        if self.baotu_chk.isChecked():
            arr.append(self.baotu_btn.text())
            mission.append("baotu")
        if self.mijing_chk.isChecked():
            arr.append(self.mijing_btn.text())
            mission.append("mijing")
        if self.dati_chk.isChecked():
            arr.append(self.dati_btn.text())
            mission.append("dati")
        if self.yabiao_chk.isChecked():
            arr.append(self.yabiao_btn.text())
            mission.append("yabiao")
        self.addTask("test", f'单人日常[{str.join(",", arr)}]')
        self.exec_script("mhxy_richang", f'-ir {self.getTargetArr()} '
                                         f'-m {str.join(",", mission)} '
                                         f'-w {self.wait_chk.isChecked()} '
                                         f'--shutdown {self.missionrichang_shutdown_chk.isChecked()}')

    # 获取执行目标
    def getTargetArr(self):
        arr = []
        if self.target_rdo1.isChecked():
            arr.append('0')
        if self.target_rdo2.isChecked():
            arr.append('1')
        if self.target_rdo3.isChecked():
            arr.append('2')
        if self.target_rdo4.isChecked():
            arr.append('3')
        if self.target_rdo5.isChecked():
            arr.append('4')
        return ','.join(arr)

    # 获取执行目标
    def getTarget(self):
        if self.target_rdo1.isChecked():
            return 0
        elif self.target_rdo2.isChecked():
            return 1
        elif self.target_rdo3.isChecked():
            return 2
        elif self.target_rdo4.isChecked():
            return 4
        elif self.target_rdo5.isChecked():
            return 5

    def baotuTask(self):
        self.exec_script('mhxy_baotu', f'-ir {self.getTargetArr()}')
        self.addTask("baotu", f'{self.baotu_btn.text()}')

    def mijingTask(self):
        self.exec_script('mhxy_mijing', f'-ir {self.getTargetArr()}')
        self.addTask("test", f'{self.mijing_btn.text()}')

    def datiTask(self):
        self.exec_script('mhxy_dati', f'-ir {self.getTargetArr()}')
        self.addTask("test", f'{self.dati_btn.text()}')

    def yabiaoTask(self):
        self.exec_script('mhxy_yabiao', f'-ir {self.getTargetArr()}')
        self.addTask("test", f'{self.yabiao_btn.text()}')

    def runCustomerTask(self):
        cmd = f'python{"" if self.black_win.isChecked() else "w"} {self.lineEdit.text()}\\{self.cusomer_ipt.text()} -i {self.getTarget()}'
        print("执行脚本：" + cmd)
        res = os.system(cmd)
        print(res)
        self.addTask("test", f'{self.yabiao_btn.text()}')
        if self.conn.has_section("main"):
            self.conn.set('main', 'lastscript', self.cusomer_ipt.text())
            self.conn.write(open(self.file_path, 'w'))

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

    def openMihuntaCfgDialog(self):
        popup = MihuntaCfgDialog()
        popup.exec()

    def openBangpaiCfgDialog(self):
        popup = BangpaiCfgDialog()
        popup.exec()

    def openLinlongshiCfgDialog(self):
        popup = LinlongshiCfgDialog()
        popup.exec()

    # # 获取所有正在运行的进程
    # all_processes = psutil.process_iter()
    # # 遍历所有进程并打印进程信息
    # for process in all_processes:
    #     print(f"Process ID: {process.pid}")
    #     print(f"Process Name: {process.name()}")
    #     print(f"Process Status: {process.status()}")
    #     print("\n")
    # 界面互动

    def gamoprocess2Small(self):
        # print(f'python {self.lineEdit.text()}\game_process.py')
        self.exec_script("game_process", "-s small")

    def gamoprocess2Origin(self):
        self.exec_script("game_process", "-s origin")

    def openLog(self):
        os.system(f'start notepad.exe mhxy_script.log')

    def addTask(self, bindThread, text):
        lwi = QListWidgetItem(text)
        lwi.setData(Qt.UserRole, bindThread)
        # self.listWidget.addItem(lwi)

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
