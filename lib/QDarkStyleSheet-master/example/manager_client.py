__author__ = 'GABI'
#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) <2013-2014> <Colin Duquesnoy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""
A simple example of use.

Load an ui made in QtDesigner and apply the DarkStyleSheet.


Requirements:
    - Python 2 or Python 3
    - PySide

.. note.. :: qdarkstyle does not have to be installed to run
    the example

"""
import logging
import sys
from PySide import QtGui, QtCore
# make the example runnable without the need to install
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))
import sys
import qdarkstyle
from manager_client_ui import *
import manager_client_ui


def main():
    """
    Application entry point
    """



    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))




    if len(sys.argv) >= 2:
        fileName = sys.argv[1]
    else:
        fileName = "."

    tabdialog = Ui_MainWindow()
    tabdialog.resize(500,200)

    sys.exit(tabdialog.exec_())

    # setup stylesheet


    # run
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
