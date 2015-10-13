from PySide import QtGui, QtCore
import sys
import os
class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.img_fold = r"C:\Users\GABI\Pictures\WallPaper"

        self.widget_layout = QtGui.QVBoxLayout(self)
        self.scrollarea = QtGui.QScrollArea()
        self.scrollarea.setWidgetResizable(True)
        self.widget_layout.addWidget(self.scrollarea)
        self.widget = QtGui.QWidget()
        self.layout = QtGui.QVBoxLayout(self.widget)
        self.scrollarea.setWidget(self.widget)

        self.layout.setAlignment(QtCore.Qt.AlignHCenter)

        for img in os.listdir(self.img_fold):
            img_path = os.path.join(self.img_fold, img)

            pixmap = QtGui.QPixmap(img_path)
            lbl = QtGui.QLabel(self)
            lbl.setPixmap(pixmap)

            self.layout.addWidget(lbl)


        self.setGeometry(300, 300, 280, 170)  #s
        self.setWindowTitle('Image viewer')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()