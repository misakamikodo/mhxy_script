import os
from configparser import ConfigParser

from PyQt6.QtWidgets import QDialog
from win.ghost_config import Ui_Dialog


class GhostCfgDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(GhostCfgDialog, self).__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.save)
        self.file_path = os.path.join(os.path.abspath('.'), r'resources\ghost\ghost.ini')
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("文件不存在")
        self.conn = ConfigParser()
        self.conn.read(self.file_path)

        self.chasepos = float(self.conn.get('main', 'chasepos'))
        # self.maxRound = int(self.conn.get('main', 'maxRound'))
        self.doublePointNumPer100 = int(self.conn.get('main', 'doublePointNumPer100'))
        # self.resize = bool(int(self.conn.get('main', 'resize')))
        # self.warnMinute = int(self.conn.get('main', 'warnMinute'))

        self.lineEdit.setText(str(self.chasepos))
        self.lineEdit_2.setText(str(self.doublePointNumPer100))

    def save(self):
        self.conn.set('main', 'chasepos', self.lineEdit.text())
        self.conn.set('main', 'doublePointNumPer100', self.lineEdit_2.text())
        self.conn.write(open(self.file_path, 'w'))
        self.close()
