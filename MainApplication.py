# -*- coding: utf-8 -*-


'''

This is based upon examples in the book
Create GUI Applications with Python & QT5 5th Edition
by Martin Fitzpatrick

 See the file PyQt5 Examples.txt
 
'''

from PyQt5.QtCore import (PYQT_VERSION_STR,
                          QT_VERSION_STR,
                          QDate
                          )

from datetime import datetime
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets

from Main_ToDo import MainTodo, TodoModel

from Table_Model import TableModel, MainTable

from Custom_Control import PowerBar, _Bar

import sys
import os
import pandas as pd
import platform

import resources_rc 

__version__ = '1.0.1.0'

# use -> pyuic5 MainApp.ui -o MainApp.py
# use -> pyrcc5 resources.qrc -o resources_rc.py

# Form implementation generated from reading ui file 'MainApp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
#

class Ui_MainApp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 665)
        MainWindow.move(100, 100)   # added so splash screen is on mainwindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonToDo = QtWidgets.QPushButton(self.centralwidget)
        self.buttonToDo.setGeometry(QtCore.QRect(90, 130, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonToDo.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonToDo.setIcon(icon)
        self.buttonToDo.setObjectName("buttonToDo")
        self.buttonLoad_Table = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLoad_Table.setGeometry(QtCore.QRect(90, 170, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad_Table.setFont(font)
        self.buttonLoad_Table.setObjectName("buttonLoad_Table")
        self.buttonScroll_Text = QtWidgets.QPushButton(self.centralwidget)
        self.buttonScroll_Text.setGeometry(QtCore.QRect(90, 210, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonScroll_Text.setFont(font)
        self.buttonScroll_Text.setObjectName("buttonScroll_Text")
        self.buttonDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDisplay.setGeometry(QtCore.QRect(710, 530, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonDisplay.setFont(font)
        self.buttonDisplay.setObjectName("buttonDisplay")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(670, 260, 231, 161))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 229, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.labelContext = QtWidgets.QLabel(self.centralwidget)
        self.labelContext.setGeometry(QtCore.QRect(390, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelContext.setFont(font)
        self.labelContext.setObjectName("labelContext")
        self.buttonDate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDate.setGeometry(QtCore.QRect(90, 250, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonDate.setFont(font)
        self.buttonDate.setObjectName("buttonDate")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(670, 210, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(670, 440, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(670, 480, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setMaximum(11)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.labelDate = QtWidgets.QLabel(self.centralwidget)
        self.labelDate.setGeometry(QtCore.QRect(270, 250, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelDate.setFont(font)
        self.labelDate.setFrameShape(QtWidgets.QFrame.Box)
        self.labelDate.setObjectName("labelDate")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(670, 90, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(670, 130, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.labelToDo = QtWidgets.QLabel(self.centralwidget)
        self.labelToDo.setGeometry(QtCore.QRect(270, 130, 201, 21))
        self.labelToDo.setFrameShape(QtWidgets.QFrame.Box)
        self.labelToDo.setObjectName("labelToDo")
        self.labelTable = QtWidgets.QLabel(self.centralwidget)
        self.labelTable.setGeometry(QtCore.QRect(270, 170, 201, 21))
        self.labelTable.setFrameShape(QtWidgets.QFrame.Box)
        self.labelTable.setObjectName("labelTable")
        self.labelScroll = QtWidgets.QLabel(self.centralwidget)
        self.labelScroll.setGeometry(QtCore.QRect(270, 210, 201, 21))
        self.labelScroll.setFrameShape(QtWidgets.QFrame.Box)
        self.labelScroll.setObjectName("labelScroll")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(670, 170, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(930, 590, 281, 31))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/icons/Logo.PNG"))
        self.labelLogo.setObjectName("labelLogo")
        self.buttonCustom = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCustom.setGeometry(QtCore.QRect(90, 290, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonCustom.setFont(font)
        self.buttonCustom.setObjectName("buttonCustom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1219, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Sroll_Area_Text = QtWidgets.QAction(MainWindow)
        self.actionLoad_Sroll_Area_Text.setObjectName("actionLoad_Sroll_Area_Text")
        self.actionStart_ToDo_List = QtWidgets.QAction(MainWindow)
        self.actionStart_ToDo_List.setObjectName("actionStart_ToDo_List")
        self.actionDisplay_Table_Data = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Table_Data.setEnabled(False)
        self.actionDisplay_Table_Data.setObjectName("actionDisplay_Table_Data")
        self.actionDisplay_Main_Window_Selections = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Main_Window_Selections.setObjectName("actionDisplay_Main_Window_Selections")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPyQt_Demo_Help = QtWidgets.QAction(MainWindow)
        self.actionPyQt_Demo_Help.setObjectName("actionPyQt_Demo_Help")
        self.actionLoad_Table_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Table_Data.setObjectName("actionLoad_Table_Data")
        self.actionHelp_File = QtWidgets.QAction(MainWindow)
        self.actionHelp_File.setObjectName("actionHelp_File")
        self.menuFile.addAction(self.actionLoad_Sroll_Area_Text)
        self.menuFile.addAction(self.actionLoad_Table_Data)
        self.menuRun.addAction(self.actionStart_ToDo_List)
        self.menuRun.addAction(self.actionDisplay_Table_Data)
        self.menuRun.addAction(self.actionDisplay_Main_Window_Selections)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp_File)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonToDo.setText(_translate("MainWindow", "ToDo List"))
        self.buttonLoad_Table.setText(_translate("MainWindow", "Load Table Data"))
        self.buttonScroll_Text.setText(_translate("MainWindow", "Load Scroll Text"))
        self.buttonDisplay.setText(_translate("MainWindow", "Display Selections"))
        self.labelContext.setText(_translate("MainWindow", "Right Click for Context Menus"))
        self.buttonDate.setText(_translate("MainWindow", "Select Date"))
        self.labelDate.setText(_translate("MainWindow", "Date = "))
        self.radioButton.setText(_translate("MainWindow", "Radio Button Selection"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.labelToDo.setText(_translate("MainWindow", "Total ToDos = ?"))
        self.labelTable.setText(_translate("MainWindow", "No Table Data Loaded"))
        self.labelScroll.setText(_translate("MainWindow", "Scroll Data Not Loaded"))
        self.buttonCustom.setText(_translate("MainWindow", "Custom Control"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad_Sroll_Area_Text.setText(_translate("MainWindow", "Load Sroll Area Text"))
        self.actionStart_ToDo_List.setText(_translate("MainWindow", "Start ToDo List"))
        self.actionDisplay_Table_Data.setText(_translate("MainWindow", "Display Table Data"))
        self.actionDisplay_Main_Window_Selections.setText(_translate("MainWindow", "Display Main Window Selections"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPyQt_Demo_Help.setText(_translate("MainWindow", "PyQt% Demo Help"))
        self.actionLoad_Table_Data.setText(_translate("MainWindow", "Load Table Data"))
        self.actionHelp_File.setText(_translate("MainWindow", "Help File"))

        # --- Above generated with qtdesigner using command above ---

        self.actionLoad_Table_Data.setShortcut("Ctrl+l")
        self.actionDisplay_Table_Data.setShortcut("Ctrl+d")
        self.sizeLabel = QtWidgets.QLabel()
        self.sizeLabel.setFrameStyle(QtWidgets.QFrame.StyledPanel
                                     |QtWidgets.QFrame.Sunken)
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.sizeLabel)
        self.status.showMessage("Ready", 10000)
        # tooltips - can be created inside QtDesigner as well
        self.buttonToDo.setToolTip('Select to load ToDo list')
        self.buttonLoad_Table.setToolTip('Load the DataFrame Table')
        self.buttonScroll_Text.setToolTip('Load the text for the scroll area')
        self.buttonDate.setToolTip('Select for pop-up Calendar widget')
        self.radioButton.setToolTip('Select the radio button to do nothing')
        self.checkBox.setToolTip('Select the checkbox to do more nothing')
        self.comboBox.setToolTip('Select a current dog')
        self.lineEdit.setToolTip('Enter text here or through context menu')
        self.scrollArea.setToolTip('Load Text with button to the left')
        self.dateEdit.setToolTip('Select the date with this widget')
        self.horizontalSlider.setToolTip('Spinal Tap Amp Setting')
        self.buttonDisplay.setToolTip('Select to display the settings above')
        self.buttonCustom.setToolTip('Select to display custom control')
        iconLoad = self.style().standardIcon(QtWidgets.QStyle.SP_DialogOpenButton)
        self.buttonLoad_Table.setIcon(iconLoad)  #using Qt Standard Icons
                
       

class CalendarWindow(QtWidgets.QDialog):
    def __init__(self, query_dialog, parent=None):
        super().__init__()
        self.setWindowTitle(query_dialog)
        self.setGeometry(100,100, 400, 300)
        self.layout = QtWidgets.QVBoxLayout()
        self.calendar = QtWidgets.QCalendarWidget()
        today = QDate.currentDate()
        self.calendar.setMaximumDate(today)
        self.calendar.clicked.connect(self.date_selected)
        self.layout.addWidget(self.calendar)
        self.setLayout(self.layout)
    
    def date_selected(self, date):
        self.accept()

class DisplayWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setWindowTitle('Your Settings')
        # self.setGeometry(300, 300, 300,300 )
        labelradio = QtWidgets.QLabel('Radio Button checked = ' + str(window.radio))
        labelradio.setGeometry(QtCore.QRect(270, 250, 201, 21))
        labelradio.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(labelradio)
        labelcheck = QtWidgets.QLabel('CheckBox checked = ' + str(window.check))
        labelcheck.setGeometry(QtCore.QRect(270, 250, 201, 21))
        labelcheck.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(labelcheck)
        labelcombo = QtWidgets.QLabel('ComboBox selection = ' + window.pet)
        labelcombo.setGeometry(QtCore.QRect(270, 250, 201, 21))
        labelcombo.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(labelcombo)
        labellineedit = QtWidgets.QLabel('LineEdit Text = ' + window.edit)
        labellineedit.setGeometry(QtCore.QRect(270, 250, 201, 21))
        labellineedit.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(labellineedit)
        labelscroll = QtWidgets.QLabel(window.scroll)
        labelscroll.setGeometry(QtCore.QRect(270, 250, 201, 21))
        labelscroll.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(labelscroll)
        labeldate = QtWidgets.QLabel("Date Selected = " + window.dateselected)
        labeldate.setGeometry(QtCore.QRect(270, 250, 201, 21))
        labeldate.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(labeldate)
        labelslider = QtWidgets.QLabel("Spinal Tap Amp Setting = " + str(window.AmpSetting))
        labelslider.setGeometry(QtCore.QRect(270, 250, 201, 21))
        labelslider.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(labelslider)

        self.setLayout(layout)

class MainWindow(QtWidgets.QMainWindow, Ui_MainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.module_path = os.path.dirname(os.path.realpath("__file__"))
        self.dateEdit.setDate(QDate.currentDate())
        self.selectDate = QDate.currentDate()
        self.radio = False
        self.check = False
        self.pet = 'Elsa'
        self.comboBox.addItems(['Elsa', 'Milo', 'Rudy', 'Star', 'Wrigley', 'Birdsong'])
        self.edit = ' - '
        self.scroll = 'Scroll Text Not Loaded'
        self.dateselected = QDate.currentDate().toString()
        self.AmpSetting = 0
        
        self.show()
        
        self.actionStart_ToDo_List.triggered.connect(self.loadTodo)
        self.buttonToDo.clicked.connect(self.loadTodo)
        
        self.actionLoad_Table_Data.triggered.connect(self.loadTableData)
        self.buttonLoad_Table.clicked.connect(self.loadTableData)
        
        self.actionDisplay_Table_Data.triggered.connect(self.displayTable)
        self.buttonDate.clicked.connect(self.getDate)
        # no button for displaying table, only menu item
        
        self.actionLoad_Sroll_Area_Text.triggered.connect(self.readScrollText)
        self.buttonScroll_Text.clicked.connect(self.readScrollText)
        
        self.actionDisplay_Main_Window_Selections.triggered.connect(self.displaySelections)
        self.buttonDisplay.clicked.connect(self.displaySelections)
        
        # no menu item - button only
        self.buttonCustom.clicked.connect(self.displayCustom)
        
        self.radioButton.clicked.connect(self.radioClicked)
        self.checkBox.clicked.connect(self.checkClicked)
        self.comboBox.currentTextChanged.connect(self.getCombo)
        self.lineEdit.textEdited.connect(self.editChanged)
        self.dateEdit.dateChanged.connect(self.dateSelected)
        self.horizontalSlider.valueChanged.connect(self.sliderChanged)
        self.actionAbout.triggered.connect(self.helpAbout)
        self.actionHelp_File.triggered.connect(self.helpHelp)
        
        self.flashSplash()
        
    def flashSplash(self):
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap('Splash.png'))
        self.splash.show()
        self.splash.move(400,300)
        QtCore.QTimer.singleShot(3000, self.splash.close)


    def contextMenuEvent(self, event):
        context = QtWidgets.QMenu(self)
        action_1 = QtWidgets.QAction('QMessageBox OK', self)
        action_2 = QtWidgets.QAction('QMessageBox Choices', self)
        action_3 = QtWidgets.QAction('QMessageBox Entry', self)
     
        action_1.triggered.connect(lambda: self.messageok_triggered())
        action_2.triggered.connect(lambda: self.messagecustom_triggered())
        action_3.triggered.connect(lambda: self.messageentry_triggered())
        context.addAction(action_1)
        context.addAction(action_2)
        context.addAction(action_3)
        context.exec_(event.globalPos())

    def messageok_triggered(self):
        
        self.status.showMessage('OK MessageBox Selected', 3000)
        mesgOk = QtWidgets.QMessageBox()
        mesgOk.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mesgOk.setIcon(QtWidgets.QMessageBox.Critical)
        mesgOk.setWindowTitle('Context Menu Example')
        mesgOk.setText('This is a Message Box - OK')
        mesgOk.exec_()
        
    def displayCustom(self):
        
        self.status.showMessage('Custom Control Widget', 5000)
        self.volume = PowerBar(
            steps=[
        "green",
        "green",
        "green",
        "green",
        "green",
        "green",
        "yellow",
        "yellow",
        "orange",
        "orange",
        "red"
        ]
        )
        self.volume.show()
        

        # the below code does not work but I think it should
        # and may it later versions of PyQt
        # it should set the value of the horizontal slider
        # to the custom widget setting
        self.horizontalSlider.setValue(self.volume._bar.setting)
        self.horizontalSlider.update()
        self.horizontalSlider.repaint()
        
    def messagecustom_triggered(self):
        
        self.status.showMessage('Custom MessageBox Selected', 3000)
        custom = QtWidgets.QMessageBox()
        custom.setWindowTitle('Caution on your selection')
        custom.setText('Good luck picking')
        custom.setIcon(QtWidgets.QMessageBox.Question)
        custom.setStandardButtons(QtWidgets.QMessageBox.Discard
                                  | QtWidgets.QMessageBox.Ignore
                                  | QtWidgets.QMessageBox.Abort)
        
        custom.setDefaultButton(QtWidgets.QMessageBox.Abort)
        button = custom.exec_()
        if button == QtWidgets.QMessageBox.Ignore:
            print('Ignored!')                          
        elif button == QtWidgets.QMessageBox.Discard:
            print('Discarded!')
        else:
            print('\007')
            print('You chose poorly!')
        
    def messageentry_triggered(self):
        
        self.status.showMessage('Line Entry Pop Up Selected.', 3000)
        entry = QtWidgets.QInputDialog()
        title = 'Secret Phrase Decoder'
        label = 'Enter your secret phrase'
        text = 'my secret phrase'
        mode = QtWidgets.QLineEdit.Password
        phrase, ok = entry.getText(self, title, label, mode, text)
                                   
        secret_phrase = 'Secret Phrase  = ' + phrase             
        self.lineEdit.setText(secret_phrase)
        self.editChanged(secret_phrase)


    def GetMyFileNames(self, dialog, type):
        
        if type == '.csv':
            this_file = 'csv(*.csv)'
        filepath, filter = QtWidgets.QFileDialog.getOpenFileName(self, 
                            dialog, self.module_path, this_file)

        return filepath
    
    def radioClicked(self, checked):
        
        self.status.showMessage('RadioButton Updated', 3000)
        self.radio = checked
        
    def checkClicked(self, checked):
        
        self.status.showMessage('CheckBox Updated', 3000)
        self.check = checked

    def getCombo(self, dog):
        
        self.status.showMessage('Combo Box Updated', 3000)
        self.pet = dog
        
    def editChanged(self, text):
        self.status.showMessage('LineEdit changed', 3000)
        self.edit = text

    def readScrollText(self):
        
        #fixed file to read
        self.status.showMessage('Loading Scroll Area Text', 5000)
        with open('ScrollText.txt') as scroll:
            scrolltext = scroll.read()
            
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setWidgetResizable(True)
        content_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(content_widget)
        label = QtWidgets.QLabel(scrolltext)
        label.setWordWrap(False)
        layout.addWidget(label)
        self.scrollArea.setWidget(content_widget)
        self.labelScroll.setText('Scroll Text loaded from "ScrollText.txt" ')
        self.scroll = 'Scroll Text Was loaded'

    def dateSelected(self, date):
        
        self.dateselected = date.toString()
        
    def sliderChanged(self, value):
        
        self.status.showMessage('Slider Updated', 3000)
        self.AmpSetting = value

    def getDate(self):
        
        self.status.showMessage('Choose a date.', 5000)
        selected_date = CalendarWindow('Select the Start Date')
        if selected_date.exec_():
            selectdate = selected_date.calendar.selectedDate()
            self.selectDate = selectdate.toPyDate()
            self.labelDate.setText("Date = " + str(self.selectDate))

    def displayTable(self):
        
        self.status.showMessage('Display Table Data', 10000)
        self.table = MainTable(self.df_tabledata)
        self.table.show()
        
    def loadTodo(self, checked):
        
        self.status.showMessage('Loading the ToDo list', 10000)
        self.todo = MainTodo()
        self.todo.show()
        text = "Total ToDos = " + str(self.todo.model.length)
        self.labelToDo.setText(text)

    def loadTableData(self):
        
        self.status.showMessage('Loading Table Data', 10000)
        filename = self.GetMyFileNames("Load Table Data", '.csv')
        
        if filename != '':         
            self.df_tabledata = pd.read_csv(filename, index_col = None)
            self.actionDisplay_Table_Data.setEnabled(True)
        
            size = str(self.df_tabledata.shape[0]) + ' X ' + str(self.df_tabledata.shape[1])
            self.labelTable.setText("Table Size " + size + " Loaded")
        
    def displaySelections(self):
        
        self.status.showMessage('Displaying your selections', 10000)
        self.displayWindow = DisplayWindow()
        self.displayWindow.resize(300,150)
        self.displayWindow.show()

    def helpAbout(self):
        
        QtWidgets.QMessageBox.about(self, "About Do Nothing SW App",
                """<b>Refrigeration Analysis GEA3</b> v {0}
                <p>Developed by Wes Newton<p>
                <p>This application is used to do pretty <p>
                much nothing.<p>
                <p>Contact - wesandlori@windstream.net <p>
                <p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(
                __version__, platform.python_version(),
                QT_VERSION_STR, PYQT_VERSION_STR,
                platform.system()))

    def helpHelp(self):
        
         subprocess.Popen('Help.pdf', shell=True)        
        


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


# https://stackoverflow.com/questions/58661539/create-splash-screen-in-pyqt5
















