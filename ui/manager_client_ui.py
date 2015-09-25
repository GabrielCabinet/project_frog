__author__ = 'GABI'


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created: Tue Jun 23 21:43:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from app.core import *
from app.package import  *
from app.comment import *
from pprint import pprint
def list_packages(name_filter="", task_filter=""):
    '''
    List package using optional filter
    :param name_filter: use '*' as a wild card before or after the name
    :type name_filter: str
    :param task_filter: Array of task package MUST have.
    :type task_filter: list
    '''
    session_config = SessionConfig()
    project = Project(session_config.session_project_name)
    project_root = project.project_root                 #W:/Vivarium
    list_packages = os.listdir(project_root)             # List all package in root directory

    #Filter by name
    if name_filter:
    # Filter list of packages
        list_packages = [package for package in list_packages if
        re.findall("^%s$" % name_filter.lower().replace("*", ".+"), package.lower())]
        # Return List of Package matching Name Filter

        #Filter by task_filter
        if task_filter:
            remove_list = []
            for package in list_packages:
                list_package_task = list_package_tasks_directory(os.path.join(project_root,package))
                print "%s,%s"%(package , list_package_task)
                for task in task_filter:
                    if task not in list_package_task:
                            remove_list.append(package)
            list_packages = [package for package in self.list_package if package not in remove_list ]

    return list_packages



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

class TaskList(QtGui.QWidget):
    self.task_list_layout = QtGui.QVBoxLayout(self)


class AssetLib(QtGui.QWidget):
#http://stackoverflow.com/questions/10184941/how-to-detect-mouse-click-on-images-displayed-in-gui-created-using-pyside

    def __init__(self, parent=None):
        super(AssetLib, self).__init__(parent)

        layout  = QtGui.QHBoxLayout(self)

        # CURRENT ASSET
        self.asset_viewer_layout = QtGui.QVBoxLayout()
        self.comment_layout = QtGui.QVBoxLayout()
        self.comment_label = QtGui.QLabel("Some Com")
        self.comment_edit_button = QtGui.QPushButton("Edit")
        self.comment_add_button = QtGui.QPushButton("Add")
        self.comment_layout.addWidget(self.comment_label)
        self.comment_layout.addWidget(self.comment_edit_button)
        self.comment_layout.addWidget(self.comment_add_button)
        self.current_asset_layout = QtGui.QHBoxLayout()
        self.package_mini = QtGui.QLabel("Task Miniature:")               #INIT LABEL FOR MAX MINIATURE
        self.package_metadata = QtGui.QLabel("Metadata:")                 #LABEL POUR METADATA
        self.current_asset_layout.addWidget(self.package_metadata)
        layout.addStretch(1)
        self.current_asset_layout.addWidget(self.package_mini)
        self.asset_viewer_layout.addLayout(self.current_asset_layout)
        self.asset_viewer_layout.addLayout(self.comment_layout)
        list_package = list_packages()

        layout.addLayout(self.asset_viewer_layout)
        miniature_layout = QtGui.QGridLayout()
        row = 0
        colum = -1
        for package in list_package:
            package_layout = QtGui.QVBoxLayout()
            picture = PictureLabel(package, self)
            picture.pictureClicked.connect(self.update_label)
            package_info_label = QtGui.QLabel(package)

            package_layout.addWidget(picture)
            package_layout.addWidget(package_info_label)
            if colum >= 5:
                colum = 0
                row = row +1
            else:
                colum = colum+1
            miniature_layout.addLayout(package_layout,row,colum)
        layout.addLayout(miniature_layout)


        self.setLayout(layout)

    def update_label(self, metadata,package,mini_file_path,comment_file_path):

        clearLayout(self.comment_layout)

        self.metadata_str = ""
        for key, value in metadata.iteritems() :
            # data_txt =
            #data_labal = QtQui.QLabel()
            self.metadata_str = "%s<P><b>%s</b>: %s </P>"%(self.metadata_str, underscore_to_camelcase(key), value)
        self.package_metadata.setText(self.metadata_str)
        pixmap = QtGui.QPixmap(mini_file_path)
        self.package_mini.setPixmap(pixmap)
        comment = Comment(comment_file_path)
        for com in comment.comment_dictionary.keys():
            self.com_layout  = QtGui.QHBoxLayout()
            comment_text = comment.comment_dictionary[com].get('comment','unknown')
            comment_text_label = QtGui.QLabel(str(comment_text))
            comment_date_label = QtGui.QLabel(comment.comment_dictionary[com].get('date','unknown'))
            comment_file_label = QtGui.QLabel(comment.comment_dictionary[com].get('file','unkown'))
            comment_user_label = QtGui.QLabel(comment.comment_dictionary[com].get('user','unkown'))
            self.com_layout.addWidget(comment_user_label)
            self.com_layout.addWidget(comment_text_label)
            self.com_layout.addStretch(1)
            self.com_layout.addWidget(comment_date_label)
            self.com_layout.addWidget(comment_file_label)


            self.comment_layout.addLayout(self.com_layout)

    def update_task_layout(self, package_name):
        return


class PictureLabel(QtGui.QLabel):
    '''
    Create a clickable label
    '''

    pictureClicked = QtCore.Signal(dict,str,str,str) # can be other types (list, dict, object...)

    def __init__(self, package, parent=None):

        super(PictureLabel, self).__init__(parent)
        # GET CONFIG
        session_config = SessionConfig()
        project = Project(session_config.session_project_name)
        project_root = project.project_root

        #GET MINIATURE FROM PACKAGE DIR
        mini_filename = "mini_%s.jpg"%(package)
        comment_filename = "%s_comment.txt"%(package)
        self.package = package
        self.mini_file_path = os.path.join(project_root,package,mini_filename)
        self.comment_file_path = os.path.join(project_root,package,comment_filename)
        metadata_filename = "%s_metadata.txt"%(package)
        metadata_file_path = os.path.join(project_root,package,metadata_filename )
        if os.path.isfile(self.mini_file_path) :
            self.setPixmap(QtGui.QPixmap(self.mini_file_path).scaled(90,90, QtCore.Qt.KeepAspectRatio))
        else:
            self.setPixmap(os.path.join(script_root_dir,'img/logo_menu.jpg'))

        if os.path.isfile(metadata_file_path) :
            self.metadata = read_dictionary_from_file(metadata_file_path)
        else:
            self.metadata = {}

    def mousePressEvent(self, event):

        print "from PictureLabel.mousePressEvent"

        self.pictureClicked.emit(self.metadata,self.package,self.mini_file_path, self.comment_file_path)

class Browser(QtGui.QWidget):
    def __init__(self,  parent=None):
        super(Browser, self).__init__(parent)

        arborescence = Arborescence()
        test =  AssetLib()
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addStretch(1)


        mainLayout.addWidget(test)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        mainLayout.addWidget(arborescence)

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


        img_path = os.path.join(script_root_dir,'img/logo.jpg')
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


