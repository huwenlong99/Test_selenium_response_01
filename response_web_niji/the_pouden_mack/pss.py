# -*- coding: utf-8 -*-
# 随便画一个界面
# Form implementation generated from reading ui file 'pss.ui'
# 定义窗口和布局
# Created by: PyQt5 UI code generator 5.11.3
# 使用pyqt制作的页面，然后打开
# WARNING! All changes made in this file will be lost!

from tkinter import *
from mailcap import show
root =Tk()

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1007, 732)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.dialogButtonBox.setGeometry(QtCore.QRect(200, 650, 341, 32))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(160, 350, 661, 261))
        self.listView.setObjectName("listView")
        self.columnView = QtWidgets.QColumnView(Dialog)
        self.columnView.setGeometry(QtCore.QRect(160, 150, 256, 192))
        self.columnView.setObjectName("columnView")
        self.treeView = QtWidgets.QTreeView(Dialog)
        self.treeView.setGeometry(QtCore.QRect(430, 150, 256, 192))
        self.treeView.setObjectName("treeView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(700, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(690, 150, 120, 80))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 118, 78))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        self.dialogButtonBox.accepted.connect(Dialog.accept)
        self.dialogButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))


mainloop()


# show(quit())


# Ui_Dialog.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui=Ui_Dialog()
    mainWindow = QtWidgets.QMainWindow()
    mainWindow.show()
    ui.setupUi(mainWindow)
    show>(quit(Ui_Dialog.retranslateUi()))
    sys.exit(app.exec_())
    mainloop()

