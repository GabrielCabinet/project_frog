#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

This example shows
how to use QtGui.QSplitter widget.

author: Jan Bodnar
website: zetcode.com
last edited: August 2011
"""

import sys
from PySide import QtCore
from PySide import QtGui
import qdarkstyle

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

         # INITIALISE BUTTON

        okButton = QtGui.QPushButton("OK")
        user_lbl = QtGui.QLabel("User Information")
        chat_lbl = QtGui.QLabel("Chat")
        window_lbl = QtGui.QLabel("Window")
        okButton4 = QtGui.QPushButton("OK")


        img_path = 'C:/Users/GABI/PycharmProjects/frog_manager_home/logo_menu.jpg'
        pixmap = QtGui.QPixmap(img_path)
        lbl_logo = QtGui.QLabel(self)
        lbl_logo.setPixmap(pixmap)


        # MAIN LAYOUT
        main_layout = QtGui.QVBoxLayout(self)



        #TOP LAYOUT
        top_layout = QtGui.QHBoxLayout(self)
        top_layout.addWidget(lbl_logo)
        top_layout.addStretch(1)
        top_layout.addWidget(user_lbl)


        #BOT LAYOUT
        bot_layout =  QtGui.QHBoxLayout(self)
        bot_layout.addWidget(window_lbl)
        bot_layout.addWidget(chat_lbl)

        # VIEW WINDOW LAYOUT




        main_layout.addLayout(top_layout)
        main_layout.addLayout(bot_layout)





        self.setLayout(main_layout)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QtGui.QSplitter')
        self.show()

    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():

    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
