# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Oct 10 00:40:57 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

# libraries
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(732, 570)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tablesTW = QtGui.QTableWidget(self.centralwidget)
        self.tablesTW.setEnabled(True)
        self.tablesTW.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # disable editing of cell contents
        self.tablesTW.setGeometry(QtCore.QRect(10, 30, 211, 251))
        self.tablesTW.setStyleSheet(_fromUtf8(""))
        self.tablesTW.setAutoScroll(False)
        self.tablesTW.setAlternatingRowColors(True)
        self.tablesTW.setTextElideMode(QtCore.Qt.ElideNone)
        self.tablesTW.setShowGrid(True)
        self.tablesTW.setGridStyle(QtCore.Qt.SolidLine)
        self.tablesTW.setWordWrap(False)
        self.tablesTW.setCornerButtonEnabled(False)
        self.tablesTW.setObjectName(_fromUtf8("tablesTW"))
        self.tablesTW.setColumnCount(1)
        self.tablesTW.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablesTW.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablesTW.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablesTW.setItem(0, 0, item)
        self.tablesTW.horizontalHeader().setVisible(True)
        self.tablesTW.horizontalHeader().setCascadingSectionResizes(False)
        self.tablesTW.horizontalHeader().setHighlightSections(False)
        self.tablesTW.horizontalHeader().setStretchLastSection(True)
        self.tablesTW.verticalHeader().setVisible(False)
        self.tablesTW.verticalHeader().setSortIndicatorShown(False)
        self.tablesTW.verticalHeader().setStretchLastSection(False)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.tablesTW.cellClicked.connect(self.tableClick)

        self.coldatatypeTW = QtGui.QTableWidget(self.centralwidget)
        self.coldatatypeTW.setEnabled(True)
        self.coldatatypeTW.setGeometry(QtCore.QRect(10, 290, 211, 231))
        self.coldatatypeTW.setStyleSheet(_fromUtf8(""))
        self.coldatatypeTW.setAutoScroll(False)
        self.coldatatypeTW.setAlternatingRowColors(True)
        self.coldatatypeTW.setTextElideMode(QtCore.Qt.ElideNone)
        self.coldatatypeTW.setShowGrid(True)
        self.coldatatypeTW.setGridStyle(QtCore.Qt.SolidLine)
        self.coldatatypeTW.setWordWrap(False)
        self.coldatatypeTW.setCornerButtonEnabled(False)
        self.coldatatypeTW.setObjectName(_fromUtf8("coldatatypeTW"))
        self.coldatatypeTW.setColumnCount(2)
        self.coldatatypeTW.setRowCount(0)

        item = QtGui.QTableWidgetItem()
        self.coldatatypeTW.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.coldatatypeTW.setHorizontalHeaderItem(1, item)
        self.coldatatypeTW.horizontalHeader().setVisible(True)
        self.coldatatypeTW.horizontalHeader().setCascadingSectionResizes(False)
        self.coldatatypeTW.horizontalHeader().setHighlightSections(False)
        self.coldatatypeTW.horizontalHeader().setStretchLastSection(True)
        self.coldatatypeTW.verticalHeader().setVisible(False)
        self.coldatatypeTW.verticalHeader().setSortIndicatorShown(False)
        self.coldatatypeTW.verticalHeader().setStretchLastSection(False)
        # self.coldatatypeTW.setText('hello world!')
        
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 10, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.queryResultTW = QtGui.QTableWidget(self.centralwidget)
        self.queryResultTW.setEnabled(True)
        self.queryResultTW.setGeometry(QtCore.QRect(230, 320, 491, 201))
        self.queryResultTW.setStyleSheet(_fromUtf8(""))
        self.queryResultTW.setAutoScroll(False)
        self.queryResultTW.setAlternatingRowColors(True)
        self.queryResultTW.setTextElideMode(QtCore.Qt.ElideNone)
        self.queryResultTW.setShowGrid(True)
        self.queryResultTW.setGridStyle(QtCore.Qt.SolidLine)
        self.queryResultTW.setWordWrap(False)
        self.queryResultTW.setCornerButtonEnabled(False)
        self.queryResultTW.setObjectName(_fromUtf8("queryResultTW"))
        self.queryResultTW.setColumnCount(0)
        self.queryResultTW.setRowCount(0)
        self.queryResultTW.horizontalHeader().setVisible(True)
        self.queryResultTW.horizontalHeader().setCascadingSectionResizes(False)
        self.queryResultTW.horizontalHeader().setHighlightSections(False)
        self.queryResultTW.horizontalHeader().setStretchLastSection(True)
        self.queryResultTW.verticalHeader().setVisible(False)
        self.queryResultTW.verticalHeader().setSortIndicatorShown(False)
        self.queryResultTW.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)

        # execute one line push button
        self.lineBtn = QtGui.QPushButton(self.centralwidget)
        self.lineBtn.setGeometry(QtCore.QRect(300, 285, 211, 27))
        self.lineBtn.setObjectName(_fromUtf8("lineBtn"))
        self.lineBtn.setStatusTip("Execute line under cursor")
        self.lineBtn.clicked.connect(self.lineExec)     # save a line in text edit content

        # execute all push button
        self.allBtn = QtGui.QPushButton(self.centralwidget)
        self.allBtn.setGeometry(QtCore.QRect(520, 285, 98, 27))
        self.allBtn.setObjectName(_fromUtf8("allBtn"))
        self.allBtn.setStatusTip("Execute all")
        self.allBtn.clicked.connect(self.allExec)       # save all text edit contents

        # text edit
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 30, 491, 251))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        # menubar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        # menubar files
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)

        # status bar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # actions
        # import action
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionImport.setShortcut("Ctrl+I")
        self.actionImport.setStatusTip("Import database file")
        self.actionImport.triggered.connect(self.importDB)
        # exit action
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut("Ctrl+X")
        self.actionExit.setStatusTip("Close the application")
        self.actionExit.triggered.connect(self.exitApp)
        
        # add actions to respective menu file
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.populateTables()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tablesTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tables", None))
        self.label.setText(_translate("MainWindow", "Database Schema", None))
        item = self.coldatatypeTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Column", None))
        item = self.coldatatypeTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Datatype", None))
        self.lineBtn.setText(_translate("MainWindow", "Execute Line Under Cursor", None))
        self.allBtn.setText(_translate("MainWindow", "Execute All", None))
        self.label_2.setText(_translate("MainWindow", "Command Editor", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))

    # exit function
    def exitApp(self):
        print("Application closed")
        sys.exit()

    # import db function (edit this)
    def importDB(self):
        print("Edit importDB function")
        sys.exit()

    def populateTables(self):
        i=0
        # print(tables)
        for i in range(0,len(tables2),1):                        # for each table specified in the metadata
            pos = self.tablesTW.rowCount()       # create a corresponding row
            # print("pos", pos)
            self.tablesTW.insertRow(pos)
            # item = QtGui.QTableWidgetItem()
            # self.coldatatypeTW.setVerticalHeaderItem(pos, item)

            # item = QtGui.QTableWidgetItem()
            # item.setText(table)
            # self.tablesTW.setItem(i,0,item)
            self.tablesTW.setItem(i,0, QtGui.QTableWidgetItem(tables2[i]))
            # print(table)        

                    # pos = self.tableWidget.rowCount()       # create a corresponding row
                    # self.tableWidget.insertRow(pos)
                    # item = QtGui.QTableWidgetItem()
                    # self.tableWidget.setVerticalHeaderItem(pos, item)
                    #
                    # item = QtGui.QTableWidgetItem()
                    # item.setText(table)
                    # self.tableWidget.setItem(i,0,item)
                    # i=i+1

            # item.itemClicked.connect(self.addColumnNamesAndDataTypes)
            # @pyqtSlot()
            # item.tableSelect():
            #     print("a table entry was selected")
            #     item.itemClicked.connect(tableSelect)
    @pyqtSlot()
    def addColumnNamesAndDataTypes():
        for column in tables['table']:                        # for each table specified in the metadata
            print(column)

    # button + text editor functions
    def lineExec(self):                             # execute one line in text edit
        lineText = self.textEdit.toPlainText()
        print("line: " + lineText)
        self.showQueryResult()
    
    def allExec(self):                              # execute all in text edit
        allText = self.textEdit.toPlainText()
        print("all: " + allText)
        self.showQueryResult()

    def showQueryResult(self):
        rowPosition = self.queryResultTW.rowCount()
        self.queryResultTW.insertRow(rowPosition)

        item = QtGui.QTableWidgetItem()
        self.queryResultTW.setVerticalHeaderItem(rowPosition,item)

        item = QtGui.QTableWidgetItem()
        item.setText("Text 1")
        self.queryResultTW.setItem(rowPosition,0,item)

        # self.queryResultTW.setItem(rowPosition , 0, QtGui.QTableWidgetItem("Text 1"))
        # self.queryResultTW.setItem(rowPosition , 1, QtGui.QTableWidgetItem("Text 2"))
        # self.queryResultTW.setItem(rowPosition , 2, QtGui.QTableWidgetItem("Text 3"))

    @pyqtSlot()
    def tableClick(self, row, column):
            print(tables[tables2[row]])
            self.coldatatypeTW.clearContents()

            self.coldatatypeTW.setRowCount(len(tables[tables2[row]])/2)

            j = 0
            for i in range(0, len(tables[tables2[row]])/2, 1):                
                self.coldatatypeTW.setItem(i,0, QtGui.QTableWidgetItem(tables[tables2[row]][j]))
                self.coldatatypeTW.setItem(i,1, QtGui.QTableWidgetItem(tables[tables2[row]][j+1]))
                j += 2  


tables = {}
tables2 = {}

def readMetadata():
    metadata = open("metadata.txt", "r")
    row = 0
    for line in metadata:
        nonewline = line.rstrip('\n')
        # print(nonewline);
        tokens = nonewline.split(" ")
        tokens.reverse()
        tablename = tokens.pop()
        # print(tablename)
        tokens.reverse()
        for i in range(0,len(tokens),2):
            tokens[i] = tokens[i]
            # print(tokens[i], tokens[i+1])
            # tokens[i] = str.lower(tokens[i])
        tables[str.lower(tablename)] = tokens

        tables2[row] = str.lower(tablename)         
        row += 1
    # print(tables2)

if __name__ == "__main__":
    readMetadata()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
