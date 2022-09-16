# -*- coding: utf-8 -*-
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd
import PySimpleGUI as sg
from PyQt5.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget,QItemDelegate,QLineEdit, QMessageBox, QAbstractItemView, QMainWindow)
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt
from unidecode import unidecode


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        splash_pix = QtGui.QPixmap('Assets/welcome.png')
        splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
        # add fade to splashscreen 
        opaqueness = 0.0
        step = 0.1
        splash.setWindowOpacity(opaqueness)
        splash.show()
        while opaqueness < 1:
            splash.setWindowOpacity(opaqueness)
            time.sleep(step) # Gradually appears
            opaqueness+=step
        time.sleep(1) # hold image on screen for a while
        splash.close() # close the splash screen

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 558)
        MainWindow.showMaximized()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMaximumSize(QtCore.QSize(101, 91))
        self.checkBox.setStyleSheet("QCheckBox::indicator {\n"
"    width: 50px;\n"
"    height:50px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(Assets/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(Assets/switch-off.png);\n"
"}\n"
"")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Screen_1 = QtWidgets.QTableWidget(self.centralwidget)
        self.Screen_1.setFrameShape(QtWidgets.QFrame.Box)
        self.Screen_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Screen_1.setLineWidth(3)
        self.Screen_1.setObjectName("Screen_1")
        self.Screen_1.setColumnCount(0)
        self.Screen_1.setRowCount(0)
        self.verticalLayout_3.addWidget(self.Screen_1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(3)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.WR_T = QtWidgets.QLabel(self.centralwidget)
        self.WR_T.setStyleSheet("")
        self.WR_T.setFrameShape(QtWidgets.QFrame.Box)
        self.WR_T.setLineWidth(3)
        self.WR_T.setObjectName("WR_T")
        self.horizontalLayout_3.addWidget(self.WR_T)
        self.R_T = QtWidgets.QLabel(self.centralwidget)
        self.R_T.setFrameShape(QtWidgets.QFrame.Box)
        self.R_T.setLineWidth(3)
        self.R_T.setObjectName("R_T")
        self.horizontalLayout_3.addWidget(self.R_T)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Button_WR = QtWidgets.QPushButton(self.centralwidget)
        self.Button_WR.setObjectName("Button_WR")
        self.horizontalLayout_7.addWidget(self.Button_WR)
        self.Button_R = QtWidgets.QPushButton(self.centralwidget)
        self.Button_R.setObjectName("Button_R")
        self.horizontalLayout_7.addWidget(self.Button_R)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.horizontalLayout_9.setStretch(0, 3)
        self.horizontalLayout_9.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Button_Find = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Find.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Lup1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Find.setIcon(icon)
        self.Button_Find.setIconSize(QtCore.QSize(27, 16))
        self.Button_Find.setCheckable(False)
        self.Button_Find.setChecked(False)
        self.Button_Find.setObjectName("Button_Find")
        self.horizontalLayout_8.addWidget(self.Button_Find)
        self.FindBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FindBox.setObjectName("FindBox")
        self.horizontalLayout_8.addWidget(self.FindBox)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(3)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.Button_Write = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Write.setObjectName("Button_Write")
        self.verticalLayout_4.addWidget(self.Button_Write)
        self.verticalLayout_4.setStretch(0, 10)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 12)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        self.menuC_i_t = QtWidgets.QMenu(self.menubar)
        self.menuC_i_t.setObjectName("menuC_i_t")
        self.menuNg_n_ng = QtWidgets.QMenu(self.menuC_i_t)
        self.menuNg_n_ng.setObjectName("menuNg_n_ng")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionM_h_a = QtWidgets.QAction(MainWindow)
        self.actionM_h_a.setObjectName("actionM_h_a")
        self.actionTi_ng_Vi_t = QtWidgets.QAction(MainWindow)
        self.actionTi_ng_Vi_t.setObjectName("actionTi_ng_Vi_t")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.menuNg_n_ng.addAction(self.actionTi_ng_Vi_t)
        self.menuNg_n_ng.addAction(self.actionEnglish)
        self.menuC_i_t.addAction(self.menuNg_n_ng.menuAction())
        self.menuC_i_t.addAction(self.actionM_h_a)
        self.menubar.addAction(self.menuC_i_t.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Button_WR.clicked.connect(self.WR)
        self.Button_R.clicked.connect(self.R)
        self.actionTi_ng_Vi_t.triggered.connect(self.set_Vi)
        self.actionEnglish.triggered.connect(self.set_En)
        self.Ename = sg.popup_get_file("Sellect file", file_types=(("Excel file","*.xlsx"),),)
        self.tableWidget.selectionModel().selectionChanged.connect(self.dada)
        xl = pd.ExcelFile(self.Ename)
        Sname = xl.sheet_names
        for x in Sname:
            self.comboBox.addItem(x)
       
        self.comboBox.activated.connect(self.LuaCot)

        self.Button_Find.clicked.connect(self.FindInfor)
        self.ff = ["0101-22-3893", "4/8"]
        self.tableWidget.cellChanged.connect(self.ThayDoi)
        self.jj = 0
        self.vv = []
        self.pushButton.clicked.connect(self.DongY)
        self.uu ={}
        self.Button_Write.hide()
        self.Button_Write.clicked.connect(self.GhiDuLieu)
        self.DuLieu = []
        self.DieuKien = "False"
        self.mm ={}
        self.ooo = "False"
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Đọc và Ghi thẻ"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Cổng USB</span></p></body></html>"))
        self.WR_T.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:\'red\';background:\'red\'\">000</span></p></body></html>"))
        self.R_T.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:\'red\';background:\'red\'\">000</span></p></body></html>"))
        self.Button_WR.setText(_translate("MainWindow", "Chờ đọc"))
        self.Button_R.setText(_translate("MainWindow", "Đọc từng thẻ"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tên Sheet</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Đồng ý"))
        self.Button_Write.setText(_translate("MainWindow", "Ghi vào thẻ"))
        self.menuC_i_t.setTitle(_translate("MainWindow", "Cài đặt"))
        self.menuNg_n_ng.setTitle(_translate("MainWindow", "Ngôn ngữ"))
        self.actionM_h_a.setText(_translate("MainWindow", "Mã hóa"))
        self.actionTi_ng_Vi_t.setText(_translate("MainWindow", "Tiếng Việt"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))

    # def LoadData(self):
    #     df = pd.read_excel(self.Ename, str(self.comboBox.currentText())) #Câu lệnh lấy tên của sheet được chọn
        
    #     if df.size == 0:
    #         return

    #     df.fillna('', inplace=True)
    #     self.tableWidget.setRowCount(df.shape[0])
    #     self.tableWidget.setColumnCount(df.shape[1])
    #     self.tableWidget.setHorizontalHeaderLabels(df.columns)
    #     for i in range(df.shape[0]):
    #         for j in range(df.shape[1]):
    #             self.tableWidget.setItem(i,j, QTableWidgetItem(str(df.iloc[i,j])))
    #     self.tableWidget.setColumnWidth(2, 300)
    #     self.FindBox.setText("")
        
    def WR(self):
        
        self.WR_T.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:\'green\';background:\'green\'\">000</span></p></body></html>")
        self.R_T.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:\'red\';background:\'red\'\">000</span></p></body></html>")
        self.Screen_1.clear()
        self.DieuKien = "False"
        # print(self.gg)
    
    def R(self):#Tạo 1 bảng để in dữ liệu từ thẻ lên màn hình theo quy ước cho trước
        self.R_T.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:\'green\';background:\'green\'\">000</span></p></body></html>")
        self.WR_T.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:\'red\';background:\'red\'\">000</span></p></body></html>")
        #aa = self.Infor = ReadKey().RKey()
        aa = self.ff
        self.DieuKien ="True"
        
       
        
        self.Screen_1.setRowCount(2)
        self.Screen_1.setColumnCount(2)
        self.Screen_1.setItem(0,0,QTableWidgetItem("Lớp"))
        self.Screen_1.setItem(0,1,QTableWidgetItem("Mã học sinh"))
        self.Screen_1.setItem(1,0,QTableWidgetItem(str(aa[1])))
        self.Screen_1.setItem(1,1,QTableWidgetItem(str(aa[0])))
        
        

    def set_Vi(self):
        self.label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Cổng USB</span></p></body></html>")
        self.Button_WR.setText( "Chờ đọc")
        self.Button_R.setText( "Đọc từng thẻ")
        self.label_2.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tên Sheet</span></p></body></html>")
        self.Button_Write.setText( "Ghi vào thẻ")
        self.menuC_i_t.setTitle( "Cài đặt")
        self.menuNg_n_ng.setTitle( "Ngôn ngữ")
        self.actionM_h_a.setText( "Mã hóa")
        self.actionTi_ng_Vi_t.setText( "Tiếng Việt")
        self.actionEnglish.setText( "English")

    def set_En(self):
        self.label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">USB Gate</span></p></body></html>")
        self.Button_WR.setText( "Waiting to read")
        self.Button_R.setText( "Read each card")
        self.label_2.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Sheet name</span></p></body></html>")
        self.Button_Write.setText( "Write")
        self.menuC_i_t.setTitle( "Setting")
        self.menuNg_n_ng.setTitle( "Language")
        self.actionM_h_a.setText( "Encode")
        self.actionTi_ng_Vi_t.setText( "Tiếng Việt")
        self.actionEnglish.setText( "English")

    def dada(self, selected):#Kiểm tra tính đúng sai của dữ liệu trong thẻ so với bảng Excel

        aa = self.ff
       
        yy = self.uu
        
        
        
        try:
            if self.ooo == "False":
                a = []
                for ix in selected.indexes():
                    a.append(unidecode(yy.iloc[ix.row(),ix.column()]))
            elif self.ooo == "True":
                a = []
                gg = self.mm
                #print(gg)
                for gx in selected.indexes():
                    a.append(unidecode(gg.iloc[gx.row(),gx.column()]))
          
            if self.DieuKien == "True":
                if aa[1] in a and aa[0] in a:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)               
                    msg.setInformativeText("Thông tin viết vào thẻ đã đúng")
                    msg.setWindowTitle("Thông báo")
                    retval = msg.exec_()
                    # QMessageBox.information(self, "Thông báo", "Dữ liệu ghi vào đã đúng")
                    #print("True")
                else:
                    # print("False")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)               
                    msg.setInformativeText("Thông tin viết vào thẻ sai")
                    msg.setWindowTitle("Thông báo")
                    retval = msg.exec_()
                    
                    # QMessageBox.information(self,"Thông báo", "Dữ liệu ghi sai")
            if self.DieuKien == "False":
                Break
        except:
            print("Sai ở dada")
        print(a)
        # print(self.ooo)
        self.DuLieu = a
    def FindInfor(self):
        self.ooo = "True"
        df = pd.read_excel(self.Ename, str(self.comboBox.currentText()))
        Fi = self.FindBox.text()
        aaa = df['Họ và tên']
        bbb = df['Mã học sinh']
        ccc = df['Lớp']
        ddd = df['Giới tính']
        eee = df['Dân tộc']
        fff = df['Ghi chú']
        self.tableWidget.setRowCount(0)
        self.tableWidget.selectionModel().Clear
        if Fi in aaa.unique():
            ff = df[aaa == Fi]

            ff.fillna('', inplace=True)
            self.tableWidget.setRowCount(ff.shape[0])
            self.tableWidget.setColumnCount(ff.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(df.columns)
            for i in range(ff.shape[0]):
                for j in range(ff.shape[1]):
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(ff.iloc[i,j])))

            self.tableWidget.setColumnWidth(2, 300)
            self.label_4.setText("")
            self.mm = ff
        elif Fi in eee.unique():
            ff = df[eee == Fi]
            ff.fillna('', inplace=True)
            self.tableWidget.setRowCount(ff.shape[0])
            self.tableWidget.setColumnCount(ff.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(df.columns)
            for i in range(ff.shape[0]):
                for j in range(ff.shape[1]):
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(ff.iloc[i,j])))
            self.tableWidget.setColumnWidth(2, 300)
            self.label_4.setText("")
            self.mm = ff
        elif Fi in fff.unique():
            ff = df[fff == Fi]
            ff.fillna('', inplace=True)
            self.tableWidget.setRowCount(ff.shape[0])
            self.tableWidget.setColumnCount(ff.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(df.columns)
            for i in range(ff.shape[0]):
                for j in range(ff.shape[1]):
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(ff.iloc[i,j])))
            self.tableWidget.setColumnWidth(2, 300)
            self.label_4.setText("")
            self.mm = ff
        elif Fi in bbb.unique():
            ff = df[bbb == Fi]
            ff.fillna('', inplace=True)
            self.tableWidget.setRowCount(ff.shape[0])
            self.tableWidget.setColumnCount(ff.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(df.columns)
            for i in range(ff.shape[0]):
                for j in range(ff.shape[1]):
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(ff.iloc[i,j])))
            self.tableWidget.setColumnWidth(2, 300)
            self.label_4.setText("")
            self.mm = ff
        elif Fi in ccc.unique():
            ff = df[ccc == Fi]
            ff.fillna('', inplace=True)
            self.tableWidget.setRowCount(ff.shape[0])
            self.tableWidget.setColumnCount(ff.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(df.columns)
            for i in range(ff.shape[0]):
                for j in range(ff.shape[1]):
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(ff.iloc[i,j])))
            self.tableWidget.setColumnWidth(2, 300) 
            self.label_4.setText("")   
            self.mm = ff    
        elif Fi in ddd.unique():
            ff = df[ddd == Fi]
            # ff.fillna('', inplace=True)
            self.tableWidget.setRowCount(ff.shape[0])
            self.tableWidget.setColumnCount(ff.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(df.columns)
            for i in range(ff.shape[0]):
                for j in range(ff.shape[1]):
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(ff.iloc[i,j])))
            self.tableWidget.setColumnWidth(2, 300)
            self.label_4.setText("")
            self.mm = ff
            
        else:
            self.label_4.setText("Dữ liệu nhập chưa đúng so với mẫu hoặc không có dữ liệu này")

    def LuaCot(self):
        self.ooo ="False"
        self.pushButton.show()
        self.vv.clear()
        df = pd.read_excel(self.Ename, str(self.comboBox.currentText()))
        #print(df)
        column_names = df.columns.values.tolist()
        #print(column_names)
        self.tableWidget.setRowCount(len(column_names)+1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0,QTableWidgetItem(""))
        self.tableWidget.setItem(0,1,QTableWidgetItem("Tên cột"))
        # self.tableWidget.setItem(0,2,QTableWidgetItem("Thứ tự in lên"))
        row = 1
        
        # boxcheck = Ite
        for val in column_names:
            self.tableWidget.setItem(row,1,QTableWidgetItem(val))
            row = row +1
        for row in range(len(column_names)+1):
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            chkBoxItem.setCheckState(Qt.CheckState.Unchecked)
            self.tableWidget.setItem(row+1, 0, chkBoxItem)
        
        self.tableWidget.setColumnWidth(2, 300)


    def ThayDoi(self, row, column):
        
        
        item = self.tableWidget.item(row, column)
        boxcheck = item.checkState()

        try:
            if boxcheck == Qt.CheckState.Checked:
                nn = self.tableWidget.item(row, column+1)
                self.vv.append(nn.text())
            #print(str(self.vv))
            elif boxcheck == Qt.CheckState.Unchecked and len(self.vv)>=1:
                mm = self.tableWidget.item(row, column+1)
                self.vv.remove(mm.text())
            print(str(self.vv))
        except:
            print("Sai ở Thay Đổi")   

    def DongY(self):
        self.pushButton.hide()
        self.Button_Write.show()
        ll = self.vv
        df = pd.read_excel(self.Ename, str(self.comboBox.currentText()))
        qq = df[ll]
        print(qq)
        if qq.size == 0:
            return

        qq.fillna('', inplace=True)
        self.tableWidget.setRowCount(qq.shape[0])
        self.tableWidget.setColumnCount(qq.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(qq.columns)
        for i in range(qq.shape[0]):
            for j in range(qq.shape[1]):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(qq.iloc[i,j])))
        self.tableWidget.setColumnWidth(2, 300)
        self.FindBox.setText("")
        self.uu = qq
    
    def GhiDuLieu(self):
        LayDuLieu = self.DuLieu

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)               
        msg.setInformativeText("Thông tin đã được thêm vào thẻ")
        msg.setWindowTitle("Thông báo")
        retval = msg.exec_()

        print(LayDuLieu)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
