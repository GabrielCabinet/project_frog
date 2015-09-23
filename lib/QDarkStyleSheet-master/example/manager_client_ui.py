__author__ = 'GABI'


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created: Tue Jun 23 21:43:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)








        lbl =  QtGui.QLabel('Salut')

        top_window = TopWindow()

        bot_window =  BotWindow()


        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)




        #LAYOUT
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(top_window)
        mainLayout.addWidget(bot_window)
        mainLayout.addWidget(lbl)
        mainLayout.addWidget(buttonBox)


        self.setLayout(mainLayout)

class TabDialog(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TabDialog, self).__init__(parent)



        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(Browser(), "General")
        tabWidget.addTab(PermissionsTab(), "Permissions")
        tabWidget.addTab(ApplicationsTab(), "Applications")




        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)

        self.setLayout(mainLayout)

        self.setWindowTitle("Tab Dialog")


class Browser(QtGui.QWidget):
    def __init__(self,  parent=None):
        super(Browser, self).__init__(parent)

        current_asset = CurrentAsset()
        bibliotheque = Bibliotheque()
        arborescence = Arborescence()

        mainLayout = QtGui.QHBoxLayout()




        mainLayout.addStretch(1)

        mainLayout.addWidget(arborescence)
        mainLayout.addWidget(current_asset)
        mainLayout.addWidget(bibliotheque)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class CurrentAsset(QtGui.QWidget):
       def __init__(self,  parent=None):
        super(CurrentAsset, self).__init__(parent)

        fileNameLabel = QtGui.QLabel("Task Miniature:")
        fileNameEdit = QtGui.QLabel("Metadata:")

        mainLayout = QtGui.QHBoxLayout()

        mainLayout.addWidget(fileNameEdit)
        mainLayout.addStretch(1)

        mainLayout.addWidget(fileNameLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class Arborescence(QtGui.QWidget):

       def __init__(self,  parent=None):
        super(Arborescence, self).__init__(parent)

        mainLayout = QtGui.QVBoxLayout()
        lbl = QtGui.QLabel('Arbo')
        mainLayout.addWidget(lbl)



        self.setLayout(mainLayout)

class Bibliotheque(QtGui.QWidget):
       def __init__(self,  parent=None):
        super(Bibliotheque, self).__init__(parent)

        mainLayout = QtGui.QGridLayout()
        j=0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]
        for p in pos:
            j = j+1
            img_path = 'C:/Users/GABI/PycharmProjects/frog_manager_home/logo_menu.jpg'
            pixmap = QtGui.QPixmap(img_path)
            lbl_miniature = QtGui.QLabel(self)
            lbl_miniature.setPixmap(pixmap)
            mainLayout.addWidget(lbl_miniature,p[0],p[1])


        self.setLayout(mainLayout)

class PermissionsTab(QtGui.QWidget):
    def __init__(self,  parent=None):
        super(PermissionsTab, self).__init__(parent)

        fileNameLabel = QtGui.QLabel("File Name:")
        fileNameEdit = QtGui.QLineEdit('yo')

        mainLayout = QtGui.QVBoxLayout()


        mainLayout.addWidget(fileNameEdit)
        mainLayout.addStretch(1)

        mainLayout.addWidget(fileNameLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class ApplicationsTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ApplicationsTab, self).__init__(parent)

        fileNameLabel = QtGui.QLabel("File Name:")
        fileNameEdit = QtGui.QLineEdit('yo')

        mainLayout = QtGui.QVBoxLayout()


        mainLayout.addWidget(fileNameEdit)
        mainLayout.addStretch(1)

        mainLayout.addWidget(fileNameLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class TopWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TopWindow, self).__init__(parent)


        img_path = 'C:/Users/GABI/PycharmProjects/frog_manager_home/logo_menu.jpg'
        pixmap = QtGui.QPixmap(img_path)
        lbl_logo = QtGui.QLabel()
        lbl_logo.setPixmap(pixmap)


        mainLayout = QtGui.QHBoxLayout()


        mainLayout.addWidget(lbl_logo)
        mainLayout.addStretch(1)
        top_window_user = TopWindowUser()
        mainLayout.addWidget(top_window_user)

        self.setLayout(mainLayout)

class Chat(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Chat, self).__init__(parent)

        lbl_logo = QtGui.QLabel('Chat')


        mainLayout = QtGui.QHBoxLayout()


        mainLayout.addWidget(lbl_logo)
        mainLayout.addStretch(1)



        self.setLayout(mainLayout)

class BotWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(BotWindow, self).__init__(parent)


        tabWidget = TabDialog()
        tabWidget.resize(500,500)
        chat = Chat()
        mainLayout = QtGui.QHBoxLayout()


        mainLayout.addWidget(tabWidget)
        mainLayout.addStretch(1)
        mainLayout.addWidget(chat)


        self.setLayout(mainLayout)

class TopWindowUser(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TopWindowUser, self).__init__(parent)


        lbl_logo = QtGui.QLabel("UserInfo")


        mainLayout = QtGui.QVBoxLayout()


        mainLayout.addWidget(lbl_logo)

        self.setLayout(mainLayout)


