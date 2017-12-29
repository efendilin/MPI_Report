# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nmainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 900)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.pName = QtWidgets.QLineEdit(self.centralwidget)
        self.pName.setAcceptDrops(False)
        self.pName.setReadOnly(True)
        self.pName.setObjectName("pName")
        self.gridLayout.addWidget(self.pName, 2, 2, 1, 1)
        self.testDown = QtWidgets.QPushButton(self.centralwidget)
        self.testDown.setObjectName("testDown")
        self.gridLayout.addWidget(self.testDown, 2, 4, 1, 1)
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pID = QtWidgets.QLineEdit(self.centralwidget)
        self.pID.setObjectName("pID")
        self.gridLayout.addWidget(self.pID, 0, 2, 1, 1)
        self.saveOnly = QtWidgets.QPushButton(self.centralwidget)
        self.saveOnly.setObjectName("saveOnly")
        self.gridLayout.addWidget(self.saveOnly, 2, 5, 1, 1)
        self.genRep = QtWidgets.QPushButton(self.centralwidget)
        self.genRep.setObjectName("genRep")
        self.gridLayout.addWidget(self.genRep, 0, 5, 1, 1)
        self.saveClose = QtWidgets.QPushButton(self.centralwidget)
        self.saveClose.setObjectName("saveClose")
        self.gridLayout.addWidget(self.saveClose, 2, 7, 1, 1)
        self.dirPath = QtWidgets.QLineEdit(self.centralwidget)
        self.dirPath.setReadOnly(True)
        self.dirPath.setObjectName("dirPath")
        self.gridLayout.addWidget(self.dirPath, 0, 7, 1, 1)
        self.DirButton = QtWidgets.QToolButton(self.centralwidget)
        self.DirButton.setObjectName("DirButton")
        self.gridLayout.addWidget(self.DirButton, 0, 8, 1, 1)
        self.openSingle = QtWidgets.QToolButton(self.centralwidget)
        self.openSingle.setObjectName("openSingle")
        self.gridLayout.addWidget(self.openSingle, 2, 8, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 2, 9, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabEReport = QtWidgets.QTabWidget(self.centralwidget)
        self.tabEReport.setObjectName("tabEReport")
        self.nmotab = QtWidgets.QWidget()
        self.nmotab.setObjectName("nmotab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.nmotab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.nmorep = QtWidgets.QTextEdit(self.nmotab)
        font = QtGui.QFont()
        font.setFamily("細明體")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nmorep.setFont(font)
        self.nmorep.setStyleSheet("")
        self.nmorep.setObjectName("nmorep")
        self.gridLayout_4.addWidget(self.nmorep, 0, 0, 1, 1)
        self.tabEReport.addTab(self.nmotab, "")
        self.nmtab = QtWidgets.QWidget()
        self.nmtab.setObjectName("nmtab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.nmtab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nmreps = QtWidgets.QTextEdit(self.nmtab)
        font = QtGui.QFont()
        font.setFamily("細明體")
        self.nmreps.setFont(font)
        self.nmreps.setObjectName("nmreps")
        self.horizontalLayout_3.addWidget(self.nmreps)
        self.tabEReport.addTab(self.nmtab, "")
        self.pathtab = QtWidgets.QWidget()
        self.pathtab.setObjectName("pathtab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.pathtab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pathreps = QtWidgets.QTextEdit(self.pathtab)
        font = QtGui.QFont()
        font.setFamily("細明體")
        self.pathreps.setFont(font)
        self.pathreps.setObjectName("pathreps")
        self.horizontalLayout_4.addWidget(self.pathreps)
        self.tabEReport.addTab(self.pathtab, "")
        self.radiotab = QtWidgets.QWidget()
        self.radiotab.setObjectName("radiotab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.radiotab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radiorep = QtWidgets.QTextEdit(self.radiotab)
        font = QtGui.QFont()
        font.setFamily("細明體")
        self.radiorep.setFont(font)
        self.radiorep.setObjectName("radiorep")
        self.horizontalLayout_5.addWidget(self.radiorep)
        self.tabEReport.addTab(self.radiotab, "")
        self.scopytab = QtWidgets.QWidget()
        self.scopytab.setObjectName("scopytab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scopytab)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scopyrep = QtWidgets.QTextEdit(self.scopytab)
        font = QtGui.QFont()
        font.setFamily("細明體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.scopyrep.setFont(font)
        self.scopyrep.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.scopyrep.setObjectName("scopyrep")
        self.horizontalLayout_6.addWidget(self.scopyrep)
        self.tabEReport.addTab(self.scopytab, "")
        self.others = QtWidgets.QWidget()
        self.others.setObjectName("others")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.others)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.othersrep = QtWidgets.QTextEdit(self.others)
        font = QtGui.QFont()
        font.setFamily("細明體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.othersrep.setFont(font)
        self.othersrep.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.othersrep.setObjectName("othersrep")
        self.gridLayout_5.addWidget(self.othersrep, 0, 0, 1, 1)
        self.tabEReport.addTab(self.others, "")
        self.horizontalLayout.addWidget(self.tabEReport)
        self.tabCReport = QtWidgets.QTabWidget(self.centralwidget)
        self.tabCReport.setObjectName("tabCReport")
        self.horizontalLayout.addWidget(self.tabCReport)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.RBox = QtWidgets.QComboBox(self.centralwidget)
        self.RBox.setObjectName("RBox")
        self.horizontalLayout_2.addWidget(self.RBox)
        self.VBox = QtWidgets.QComboBox(self.centralwidget)
        self.VBox.setObjectName("VBox")
        self.horizontalLayout_2.addWidget(self.VBox)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_2.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFont_Size = QtWidgets.QAction(MainWindow)
        self.actionFont_Size.setObjectName("actionFont_Size")
        self.actionFcolor = QtWidgets.QAction(MainWindow)
        self.actionFcolor.setObjectName("actionFcolor")
        self.actionBcolor = QtWidgets.QAction(MainWindow)
        self.actionBcolor.setObjectName("actionBcolor")
        self.menuSetting.addAction(self.actionFont_Size)
        self.menuSetting.addAction(self.actionFcolor)
        self.menuSetting.addAction(self.actionBcolor)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        self.tabEReport.setCurrentIndex(0)
        self.tabCReport.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testDown.setText(_translate("MainWindow", "TEST"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.saveOnly.setText(_translate("MainWindow", "Save"))
        self.genRep.setText(_translate("MainWindow", "產生報告"))
        self.saveClose.setText(_translate("MainWindow", "Save and Close"))
        self.DirButton.setText(_translate("MainWindow", "..."))
        self.openSingle.setText(_translate("MainWindow", "..."))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.tabEReport.setTabText(self.tabEReport.indexOf(self.nmotab), _translate("MainWindow", "NM開單"))
        self.tabEReport.setTabText(self.tabEReport.indexOf(self.nmtab), _translate("MainWindow", "NM"))
        self.tabEReport.setTabText(self.tabEReport.indexOf(self.pathtab), _translate("MainWindow", "病理"))
        self.tabEReport.setTabText(self.tabEReport.indexOf(self.radiotab), _translate("MainWindow", "放射"))
        self.tabEReport.setTabText(self.tabEReport.indexOf(self.scopytab), _translate("MainWindow", "內視鏡"))
        self.tabEReport.setTabText(self.tabEReport.indexOf(self.others), _translate("MainWindow", "Others"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionFont_Size.setText(_translate("MainWindow", "Font Size"))
        self.actionFcolor.setText(_translate("MainWindow", "前景顏色"))
        self.actionBcolor.setText(_translate("MainWindow", "背景顏色"))
