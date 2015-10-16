from PySide import QtGui
import sys
import fnmatch
import os
app = QtGui.QApplication(sys.argv)



#!/usr/bin/python

import os

# traverse root directory, and list directories as dirs and files as files
model = QtGui.QStandardItemModel()
for root, dirs, files in os.walk("D://project_viva"):
    path = root.split('/')

    print (len(path) - 1) *'---' , os.path.basename(root)
    for file in files:
        print len(path)*'---', file


treeWidget = QtGui.QTreeWidget()
treeWidget.setColumnCount(2)
treeWidget.setHeaderLabels(['Title', 'Summary']);




#First top level item and its kids
item0 = QtGui.QTreeWidgetItem(treeWidget, ['Title 0', 'Summary 0'])
item00 = QtGui.QTreeWidgetItem(item0, ['Title 00', 'Summary 00'] )
item01 = QtGui.QTreeWidgetItem(item0, ['Title 01', 'Summary 01'])

#Second top level item and its kids
item1 = QtGui.QTreeWidgetItem(treeWidget, ['Title 1', 'Summary 1'])
item10 = QtGui.QTreeWidgetItem(item1, ['Title 10', 'Summary 10'])
item11 = QtGui.QTreeWidgetItem(item1, ['Title 11', 'Summary 11'])
item12 = QtGui.QTreeWidgetItem(item1, ['Title 12', 'Summary 12'])

#Children of item11
item110 = QtGui.QTreeWidgetItem(item11, ['Title 110', 'Summary 110'])
item111 = QtGui.QTreeWidgetItem(item11, ['Title 111', 'Summary 111'])

treeWidget.show() 
sys.exit(app.exec_())