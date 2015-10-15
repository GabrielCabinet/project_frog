from PySide import QtGui
import sys

app = QtGui.QApplication(sys.argv)
model = QtGui.QStandardItemModel()
model.setHorizontalHeaderLabels(['Title', 'Summary'])
rootItem = model.invisibleRootItem()

#First top-level row and children 
item0 = [QtGui.QStandardItem('Title0'), QtGui.QStandardItem('Summary0')]
item00 = [QtGui.QStandardItem('Title00'), QtGui.QStandardItem('Summary00')]
item01 = [QtGui.QStandardItem('Title01'), QtGui.QStandardItem('Summary01')]
rootItem.appendRow(item0)
item0[0].appendRow(item00)
item0[0].appendRow(item01)

#Second top-level item and its children
item1 = [QtGui.QStandardItem('Title1'), QtGui.QStandardItem('Summary1')]
item10 = [QtGui.QStandardItem('Title10'), QtGui.QStandardItem('Summary10')]
item11 = [QtGui.QStandardItem('Title11'), QtGui.QStandardItem('Summary11')]
item12 = [QtGui.QStandardItem('Title12'), QtGui.QStandardItem('Summary12')]
rootItem.appendRow(item1)
item1[0].appendRow(item10)
item1[0].appendRow(item11)
item1[0].appendRow(item12)

#Children of item11 (third level items)
item110 = [QtGui.QStandardItem('Title110'), QtGui.QStandardItem('Summary110')]
item111 = [QtGui.QStandardItem('Title111'), QtGui.QStandardItem('Summary111')]
item11[0].appendRow(item110)
item11[0].appendRow(item111)

treeView= QtGui.QTreeView()
treeView.setModel(model)
treeView.show()
sys.exit(app.exec_())