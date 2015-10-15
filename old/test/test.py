from PySide import QtGui
import sys
import fnmatch
import os
app = QtGui.QApplication(sys.argv)

treeWidget = QtGui.QTreeWidget()
treeWidget.setColumnCount(2)
treeWidget.setHeaderLabels(['Title', 'Summary']);


matches = []

for dir in os.listdir("D:/project_viva"):
    print dir

    item0 = QtGui.QTreeWidgetItem(treeWidget, ['Title 0', 'Summary 0'])


    print "yooooo"

    for filename in fnmatch.filter(filenames, '*.c'):
        matches.append(os.path.join(root, filename))


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