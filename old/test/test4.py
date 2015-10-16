# -*- coding: utf-8 -*-

'''
@author: Aaron Richiger
@contact: a.r...@bluewin.ch
@date: 08.02.2011
'''

from PySide.QtGui import *
from PySide.QtCore import *
import sys

class TreeItem(object):
     def __init__(self, data, parent=None):
         self.parentItem = parent
         self.itemData = data
         self.childItems = []

     def appendChild(self, item):
         self.childItems.append(item)

     def child(self, row):
         return self.childItems[row]

     def childCount(self):
         return len(self.childItems)

     def columnCount(self):
         return len(self.itemData)

     def data(self, column):
         try:
             return self.itemData[column]
         except IndexError:
             return None

     def parent(self):
         return self.parentItem

     def row(self):
         if self.parentItem:
             return self.parentItem.childItems.index(self)

         return 0


class TreeModel(QAbstractItemModel):
     def __init__(self, rootItem, parent=None):
         super(TreeModel, self).__init__(parent)

         self.rootItem = rootItem

     def columnCount(self, parent = QModelIndex()):
         if parent.isValid():
             return parent.internalPointer().columnCount()
         else:
             return self.rootItem.columnCount()

     def data(self, index, role):
         if not index.isValid():
             return None

         if role != Qt.DisplayRole:
             return None

         item = index.internalPointer()

         return item.data(index.column())

     def flags(self, index):
         if not index.isValid():
             return Qt.NoItemFlags

         return Qt.ItemIsEnabled | Qt.ItemIsSelectable

     def headerData(self, section, orientation, role):
         if orientation == Qt.Horizontal and role == Qt.DisplayRole:
             return self.rootItem.data(section)

         return None

     def index(self, row, column, parent = QModelIndex()):
         if not self.hasIndex(row, column, parent):
             return QModelIndex()

         if not parent.isValid():
             parentItem = self.rootItem
         else:
             parentItem = parent.internalPointer()

         childItem = parentItem.child(row)
         if childItem:
             return self.createIndex(row, column, childItem)
         else:
             return QModelIndex()

     def parent(self, index):
         if not index.isValid():
             return QModelIndex()

         childItem = index.internalPointer()
         parentItem = childItem.parent()

         if parentItem == self.rootItem:
             return QModelIndex()

         return self.createIndex(parentItem.row(), 0, parentItem)

     def rowCount(self, parent = QModelIndex()):
         if parent.column() > 0:
             return 0

         if not parent.isValid():
             parentItem = self.rootItem
         else:
             parentItem = parent.internalPointer()

         return parentItem.childCount()

     def addData(self, data, parent):
         lines = data.split('\n')
         parents = [parent]
         indentations = [0]

         number = 0

         while number < len(lines):
             position = 0
             while position < len(lines[number]):
                 if lines[number][position] != ' ':
                     break
                 position += 1

             lineData = lines[number][position:].strip()

             if lineData:
                 # Read the column data from the rest of the line.
                 columnData = [s.strip() for s in lineData.split(';') if s]

                 if position > indentations[-1]:
                     # The last child of the current parent is now the new
                     # parent unless the current parent has no children.

                     if parents[-1].childCount() > 0:
                         
parents.append(parents[-1].child(parents[-1].childCount() - 1))
                         indentations.append(position)

                 else:
                     while position < indentations[-1] and len(parents) > 0:
                         parents.pop()
                         indentations.pop()

                 # Append a new item to the current parent's list of 
children.
                 parents[-1].appendChild(TreeItem(columnData, parents[-1]))

             number += 1
         self.rowsInserted.emit(self, self.rowCount() - 1, 
self.rowCount() - 1)

if __name__ == '__main__':
     app = QApplication(sys.argv)
     widget = QWidget()

     data = '''
Getting Started;            How to familiarize yourself with Qt Designer
     Launching Designer;     Running the Qt Designer application
     The User Interface;     How to interact with Qt Designer

Designing a Component;      Creating a GUI for your application
     Creating a Dialog;      How to create a dialog
     Composing the Dialog;   Putting widgets into the dialog example'''

     rootItem = TreeItem(("Title", "Summary"))
     model = TreeModel(rootItem)
     model.addData(data, rootItem)

     treeView = QTreeView(widget)
     treeView.setModel(model)

     lbTitle = QLabel('Title:', widget)
     lbSummary = QLabel('Summary:', widget)
     leTitle = QLineEdit(widget)
     leSummary = QLineEdit(widget)
     pbAddItem = QPushButton('Add this item', widget)
     pbAddItem.clicked.connect(lambda: model.addData(leTitle.text() + 
';' + leSummary.text(), model.rootItem))

     grid = QGridLayout(widget)
     grid.addWidget(treeView, 0, 0, 1, 2)
     grid.addWidget(lbTitle, 1, 0, 1, 1)
     grid.addWidget(lbSummary, 2, 0, 1, 1)
     grid.addWidget(leTitle, 1, 1, 1, 1)
     grid.addWidget(leSummary, 2, 1, 1, 1)
     grid.addWidget(pbAddItem, 3, 1, 1, 1)
     widget.show()

     sys.exit(app.exec_())