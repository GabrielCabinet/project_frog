import sys
from PySide.QtCore import *
from PySide.QtGui import *
from app.core import *
class Widget(QWidget):
     
    def __init__(self, parent= None):
        super(Widget, self).__init__()
         
        layout = QVBoxLayout(self)
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(False)
        #QToolButton
        textButton = QToolButton()
        textButton.setCheckable(True)
        textButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        textButton.setText("test \n yo")
        textButton.setIcon(QIcon(QPixmap(os.path.join(script_root_dir,'img/logo_menu.jpg'))
                            .scaled(80, 80)))
        textButton.setIconSize(QSize(100, 100))

         
        layout.addWidget(textButton)
         
        self.setLayout(layout)
         
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
     
    dialog = Widget()
    dialog.show()
 
    app.exec_()


