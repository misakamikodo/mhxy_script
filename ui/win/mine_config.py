# Form implementation generated from reading ui file 'mine_config.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 111)
        self.radioButton_7 = QtWidgets.QRadioButton(parent=Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 20, 89, 16))
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(parent=Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(130, 20, 89, 16))
        self.radioButton_8.setObjectName("radioButton_8")
        self.checkBox = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "挖矿配置"))
        self.radioButton_7.setText(_translate("Dialog", "花果"))
        self.radioButton_8.setText(_translate("Dialog", "长寿"))
        self.checkBox.setText(_translate("Dialog", "记住选择"))
        self.pushButton_4.setText(_translate("Dialog", "确定"))
