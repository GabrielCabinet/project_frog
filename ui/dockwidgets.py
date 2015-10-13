#!/usr/bin/env python

############################################################################
# 
#  Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
# 
#  This file is part of the example classes of the Qt Toolkit.
# 
#  This file may be used under the terms of the GNU General Public
#  License version 2.0 as published by the Free Software Foundation
#  and appearing in the file LICENSE.GPL included in the packaging of
#  this file.  Please review the following information to ensure GNU
#  General Public Licensing requirements will be met:
#  http://www.trolltech.com/products/qt/opensource.html
# 
#  If you are unsure which license is appropriate for your use, please
#  review the following information:
#  http://www.trolltech.com/products/qt/licensing.html or contact the
#  sales department at sales@trolltech.com.
# 
#  This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
#  WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
# 
############################################################################

# This is only needed for Python v2 but is harmless for Python v3.
#import sip
#sip.setapi('QString', 2)

import qdarkstyle

from app.package import *
from app.comment import *

session_config = SessionConfig()
project = Project(session_config.session_project_name)
project_root = project.project_root
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.session_config = SessionConfig()
        self.project = Project(session_config.session_project_name)
        self.project_root = self.project.project_root

        self.textEdit = QtGui.QTextEdit()

        img_path = os.path.join(script_root_dir,'img/logo.jpg')
        pixmap = QtGui.QPixmap(img_path)
        self.lbl_logo = QtGui.QLabel()
        self.lbl_logo.setPixmap(pixmap)
        self.setCentralWidget(self.lbl_logo)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()
        self.create_dock_contact_sheet()
        self.create_dock_package_info()

        self.setWindowTitle("Dock Widgets")

        self.newLetter()
        self.setUnifiedTitleAndToolBarOnMac(True)

    def newLetter(self):
        self.textEdit.clear()

        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.Start)
        topFrame = cursor.currentFrame()
        topFrameFormat = topFrame.frameFormat()
        topFrameFormat.setPadding(16)
        topFrame.setFrameFormat(topFrameFormat)

        textFormat = QtGui.QTextCharFormat()
        boldFormat = QtGui.QTextCharFormat()
        boldFormat.setFontWeight(QtGui.QFont.Bold)
        italicFormat = QtGui.QTextCharFormat()
        italicFormat.setFontItalic(True)

        tableFormat = QtGui.QTextTableFormat()
        tableFormat.setBorder(1)
        tableFormat.setCellPadding(16)
        tableFormat.setAlignment(QtCore.Qt.AlignRight)
        cursor.insertTable(1, 1, tableFormat)
        cursor.insertText("The Firm", boldFormat)
        cursor.insertBlock()
        cursor.insertText("321 City Street", textFormat)
        cursor.insertBlock()
        cursor.insertText("Industry Park")
        cursor.insertBlock()
        cursor.insertText("Some Country")
        cursor.setPosition(topFrame.lastPosition())
        cursor.insertText(QtCore.QDate.currentDate().toString("d MMMM yyyy"),
                textFormat)
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertText("Dear ", textFormat)
        cursor.insertText("NAME", italicFormat)   
        cursor.insertText(",", textFormat)
        for i in range(3):
            cursor.insertBlock()
        cursor.insertText("Yours sincerely,", textFormat)
        for i in range(3):
            cursor.insertBlock()
        cursor.insertText("The Boss", textFormat)
        cursor.insertBlock()
        cursor.insertText("ADDRESS", italicFormat)  

    def print_(self):
        document = self.textEdit.document()
        printer = QtGui.QPrinter()

        dlg = QtGui.QPrintDialog(printer, self)
        if dlg.exec_() != QtGui.QDialog.Accepted:
            return

        document.print_(printer)

        self.statusBar().showMessage("Ready", 2000)

    def save(self):
        filename, filtr = QtGui.QFileDialog.getSaveFileName(self,
                "Choose a file name", '.', "HTML (*.html *.htm)")
        if not filename:
            return

        file = QtCore.QFile(filename)
        if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "Dock Widgets",
                    "Cannot write file %s:\n%s." % (filename, file.errorString()))
            return

        out = QtCore.QTextStream(file)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        out << self.textEdit.toHtml()
        QtGui.QApplication.restoreOverrideCursor()

        self.statusBar().showMessage("Saved '%s'" % filename, 2000)

    def undo(self):
        document = self.textEdit.document()
        document.undo()

    def insertCustomer(self, customer):
        if not customer:
            return
        customerList = customer.split(', ')
        document = self.textEdit.document()
        cursor = document.find('NAME')
        if not cursor.isNull():
            cursor.beginEditBlock()
            cursor.insertText(customerList[0])
            oldcursor = cursor
            cursor = document.find('ADDRESS')
            if not cursor.isNull():
                for i in customerList[1:]:
                    cursor.insertBlock()
                    cursor.insertText(i)
                cursor.endEditBlock()
            else:
                oldcursor.endEditBlock()

    def addParagraph(self, paragraph):
        if not paragraph:
            return
        document = self.textEdit.document()
        cursor = document.find("Yours sincerely,")
        if cursor.isNull():
            return
        cursor.beginEditBlock()
        cursor.movePosition(QtGui.QTextCursor.PreviousBlock,
                QtGui.QTextCursor.MoveAnchor, 2)
        cursor.insertBlock()
        cursor.insertText(paragraph)
        cursor.insertBlock()
        cursor.endEditBlock()

    def about(self):
        QtGui.QMessageBox.about(self, "About Dock Widgets",
                "The <b>Dock Widgets</b> example demonstrates how to use "
                "Qt's dock widgets. You can enter your own text, click a "
                "customer to add a customer name and address, and click "
                "standard paragraphs to add them.")

    def createActions(self):
        self.newLetterAct = QtGui.QAction(QtGui.QIcon(':/images/new.png'),
                "&New Letter", self, shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new form letter",
                triggered=self.newLetter)

        self.saveAct = QtGui.QAction(QtGui.QIcon(':/images/save.png'),
                "&Save...", self, shortcut=QtGui.QKeySequence.Save,
                statusTip="Save the current form letter",
                triggered=self.save)

        self.printAct = QtGui.QAction(QtGui.QIcon(':/images/print.png'),
                "&Print...", self, shortcut=QtGui.QKeySequence.Print,
                statusTip="Print the current form letter",
                triggered=self.print_)

        self.undoAct = QtGui.QAction(QtGui.QIcon(':/images/undo.png'),
                "&Undo", self, shortcut=QtGui.QKeySequence.Undo,
                statusTip="Undo the last editing action", triggered=self.undo)

        self.quitAct = QtGui.QAction("&Quit", self, shortcut="Ctrl+Q",
                statusTip="Quit the application", triggered=self.close)

        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newLetterAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAct)

        self.viewMenu = self.menuBar().addMenu("&View")

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newLetterAct)
        self.fileToolBar.addAction(self.saveAct)
        self.fileToolBar.addAction(self.printAct)

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.addAction(self.undoAct)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def picture_buttonClick(self):
        package_name = (self.sender().text())
        self.package = Package(package_name)
        self.create_metadata_package()
        self.create_comment_package()
        self.create_package_task(package_name)


    def create_dock_package_info(self, package=""):

        dock = QtGui.QDockWidget("Package Info", self)

        self.package_info_widget = QtGui.QWidget()
        self.package_info_layout = QtGui.QVBoxLayout(self.package_info_widget)
        self.package_info_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.package_comment_widget = QtGui.QWidget()
        self.package_comment_layout = QtGui.QVBoxLayout(self.package_comment_widget)
        self.package_comment_layout.addWidget(QtGui.QLabel("yo"))





        # Create package preview layout
        self.package_preview_widget =QtGui.QWidget()
        self.package_preview_layout = QtGui.QHBoxLayout(self.package_preview_widget)
        self.package_mini = QtGui.QLabel("Task Miniature:")               #INIT LABEL FOR MAX MINIATURE
        self.package_metadata = QtGui.QLabel("Metadata:")                 #LABEL POUR METADATA

        self.package_preview_layout.addWidget(self.package_mini)
        self.package_preview_layout.addWidget(self.package_metadata)

        self.package_info_splitter.addWidget(self.package_preview_widget)
        self.package_info_splitter.addWidget(self.package_comment_widget)


        self.package_info_layout.addWidget(self.package_info_splitter)


     #   self.create_metadata_package()

        dock.setWidget(self.package_info_splitter)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

    def create_comment_package(self):
        clearLayout(self.package_comment_layout)
        self.comment_edit_button = QtGui.QPushButton("Edit")
        self.comment_add_button = QtGui.QPushButton("Add")
        self.comment_button_layout = QtGui.QHBoxLayout()
        self.comment_button_layout.addWidget(self.comment_edit_button)
        self.comment_button_layout.addWidget(self.comment_add_button)
        self.package_comment_layout.addLayout(self.comment_button_layout)

    def create_metadata_package(self):
        '''
        Get information package.
        :param package: package class
        :type package: class
        :return:
        '''

        # SET METADATA
        if os.path.isfile(self.package.package_metadata_path) :
            self.metadata = read_dictionary_from_file(self.package.package_metadata_path)
            self.metadata_str = ""
            for key, value in self.metadata.iteritems():
                self.metadata_str = "%s<P><b>%s</b>: %s </P>"%(self.metadata_str, underscore_to_camelcase(key), value)
            self.package_metadata.setText(self.metadata_str)
        #SET PIXMAP
        if os.path.isfile(self.package.package_mini_path):

            pixmap = QtGui.QPixmap(self.package.package_mini_path)
        else:
            pixmap = QtGui.QPixmap(os.path.join(script_root_dir,'img','defaut_package_icon.jpg'))
        self.package_mini.setPixmap(pixmap)

        return
    def create_dock_contact_sheet(self):
        '''
        Create a contact sheet of all package
        :return:
        '''


        self.contact_sheet_widget = QtGui.QWidget()
        self.contact_sheet_layout = QtGui.QGridLayout(self.contact_sheet_widget)


        row = 0
        colum = -1
        #Create Dock
        dock = QtGui.QDockWidget("Contact Sheet", self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)

        #Create defaut pixmap
        self.defaut_pixmap = QtGui.QPixmap(os.path.join(script_root_dir,'img','defaut_package_icon.jpg'))
        self.defaut_package_ico = QtGui.QIcon(self.defaut_pixmap)

        #List package and create miniature
        self.list_packages = list_packages(project_root)

        for package in self.list_packages:

            # Create layout for package img and metadata

            self.package = package
            #Create miniature and comment.
            mini_filename = "%s_mini.jpg"%(package)

            self.mini_file_path = os.path.join(project_root,package,mini_filename)


            #Create pushbutton
            self.picture_button = QtGui.QToolButton()
            self.picture_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            self.picture_button.setText(package)
            if os.path.isfile(self.mini_file_path):
                self.pixmap = QtGui.QPixmap(self.mini_file_path)

            else:
                self.pixmap = self.defaut_pixmap
            self.ico = QtGui.QIcon(self.pixmap)
            self.picture_button.setIcon(self.ico)
            self.picture_button.setIconSize(QtCore.QSize(50,50))

            #Connect Button
            self.picture_button.clicked.connect(self.picture_buttonClick)


            if colum >= 5:
                colum = 0
                row = row +1
            else:
                colum = colum+1

            self.contact_sheet_layout.addWidget(self.picture_button,row,colum)

        self.scroll = QtGui.QScrollArea()

        self.scroll.setWidgetResizable(True)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scroll.setWidget(self.contact_sheet_widget)




        dock.setWidget(self.scroll)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

    def createDockWindows(self):
        dock = QtGui.QDockWidget("Yo", self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.customerList = QtGui.QListWidget(dock)
        self.customerList.addItems((
            "John Doe, Harmony Enterprises, 12 Lakeside, Ambleton",
            "Jane Doe, Memorabilia, 23 Watersedge, Beaton",
            "Tammy Shea, Tiblanka, 38 Sea Views, Carlton",
            "Tim Sheen, Caraba Gifts, 48 Ocean Way, Deal",
            "Sol Harvey, Chicos Coffee, 53 New Springs, Eccleston",
            "Sally Hobart, Tiroli Tea, 67 Long River, Fedula"))
        dock.setWidget(self.customerList)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

        dock = QtGui.QDockWidget("Paragraphs", self)
        self.paragraphsList = QtGui.QListWidget(dock)
        self.paragraphsList.addItems((
            "Thank you for your payment which we have received today.",
            "Your order has been dispatched and should be with you within "
                "28 days.",
            "We have dispatched those items that were in stock. The rest of "
                "your order will be dispatched once all the remaining items "
                "have arrived at our warehouse. No additional shipping "
                "charges will be made.",
            "You made a small overpayment (less than $5) which we will keep "
                "on account for you, or return at your request.",
            "You made a small underpayment (less than $1), but we have sent "
                "your order anyway. We'll add this underpayment to your next "
                "bill.",
            "Unfortunately you did not send enough money. Please remit an "
                "additional $. Your order will be dispatched as soon as the "
                "complete amount has been received.",
            "You made an overpayment (more than $5). Do you wish to buy more "
                "items, or should we return the excess to you?"))
        dock.setWidget(self.paragraphsList)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

        self.customerList.currentTextChanged.connect(self.insertCustomer)
        self.paragraphsList.currentTextChanged.connect(self.addParagraph)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
