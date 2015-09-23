









import os
import sys
from PySide import QtGui, QtCore

class FrogManager(QtGui.QWidget):

    def __init__(self):
        super(FrogManager, self).__init__()
        self.initUI()

    def initUI(self):
        self.img_fold = r"C:\Users\GABI\PycharmProjects\frog_manager_home\project_frog\Shot_002"

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


        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Image viewer')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = FrogManager()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()