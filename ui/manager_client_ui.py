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
from app.package import *
from app.comment import *
from pprint import pprint


'''
package = Package('Char_TEST38',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST39',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST40',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST45',True ,'Char','Un chouette test de package' )
package = Package('Char_TEST50',True ,'Char','Un chouette test de package' )
'''

script_root_dir = os.path.abspath(__file__ + "/../../")

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



class AssetLib(QtGui.QWidget):


    def __init__(self, parent=None):
        super(AssetLib, self).__init__(parent)

        #Get config
        #http://stackoverflow.com/questions/10184941/how-to-detect-mouse-click-on-images-displayed-in-gui-created-using-pyside
        session_config = SessionConfig()
        project = Project(session_config.session_project_name)
        self.project_root = project.project_root


        # Top layout
        self.layout  = QtGui.QHBoxLayout(self)

        # Sub Layout
        self.asset_viewer_layout = QtGui.QVBoxLayout()

        #Miniature Layout
        self.miniature_layout = QtGui.QGridLayout()


        #Comment Layout
        self.comment_layout = QtGui.QVBoxLayout()
        self.comment_label = QtGui.QLabel("Some Com")

        self.comment_layout.addWidget(self.comment_label)

        #Current asset layout
        self.current_asset_layout = QtGui.QHBoxLayout()
        self.package_mini = QtGui.QLabel("Task Miniature:")               #INIT LABEL FOR MAX MINIATURE
        self.package_metadata = QtGui.QLabel("Metadata:")                 #LABEL POUR METADATA
        self.current_asset_layout.addWidget(self.package_metadata)
        self.layout.addStretch(1)
        self.current_asset_layout.addWidget(self.package_mini)

        #Task layout
        self.all_tasks_layout = QtGui.QVBoxLayout()

        #Add layout to sublayout
        self.asset_viewer_layout.addLayout(self.current_asset_layout)
        self.asset_viewer_layout.addLayout(self.comment_layout)
        self.asset_viewer_layout.addLayout(self.all_tasks_layout)
        self.layout.addLayout(self.asset_viewer_layout)

        self.layout.addLayout(self.miniature_layout)
        # LIST LES PACKAGES
        list_package = list_packages()

        self.create_packages_contact_sheet(list_package)
        self.create_package_info('Back_TEST03')

    def picture_buttonClick(self):
        self.update_all(self.sender().text())


    def update_all(self,package_name):

        self.create_package_info(package_name)
        self.create_package_comment(package_name)
        self.create_package_task(package_name)


        return

    def create_package_comment(self,package_name):
        '''
        Crate les commentaires du package
        :param package_name:
        :return:
        '''
        clearLayout(self.comment_layout)
        self.comment_edit_button = QtGui.QPushButton("Edit")
        self.comment_add_button = QtGui.QPushButton("Add")
        self.comment_button_layout = QtGui.QHBoxLayout()
        self.comment_button_layout.addWidget(self.comment_edit_button)
        self.comment_button_layout.addWidget(self.comment_add_button)
        self.comment_layout.addLayout(self.comment_button_layout)
        self.comment_tab_name_layout = QtGui.QHBoxLayout()
        self.comment_tab_name_layout.addWidget(QtGui.QLabel('User'))
        self.comment_tab_name_layout.addWidget(QtGui.QLabel('Commentaire'))
        self.comment_tab_name_layout.addStretch(1)
        self.comment_tab_name_layout.addWidget(QtGui.QLabel('Date'))
        self.comment_tab_name_layout.addWidget(QtGui.QLabel('File'))
        self.comment_layout.addLayout(self.comment_tab_name_layout)


        comment = Comment(package_name,write=False)

        self.comment_edit_button.clicked.connect(lambda: open_file_to_bloc_note(comment.comment_file_path))
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


        return

    def create_packages_contact_sheet(self,list_package):
        # Grid Layout for package miniature
        clearLayout(self.miniature_layout)
        row = 0
        colum = -1

        self.defaut_pixmap = QtGui.QPixmap(os.path.join(script_root_dir,'img','defaut_package_icon.jpg'))
        self.defaut_package_ico = QtGui.QIcon(self.defaut_pixmap)
        for package in list_package:

            # Create layout for package img and metadata

            self.package = package
            #Create miniature and comment.
            mini_filename = "%s_mini.jpg"%(package)

            self.mini_file_path = os.path.join(self.project_root,package,mini_filename)


            #Create pushbutton
            self.picture_button = QtGui.QToolButton()
            self.picture_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            self.picture_button.setText(package)
            if os.path.isfile(self.mini_file_path):
                self.pixmap = QtGui.QPixmap(self.mini_file_path)

            else:
                self.pixmap = self.defaut_pixmap
            self.ico = QtGui.QIcon(self.pixmap)
            self.picture_button.setIcon(self.ico)
            self.picture_button.setIconSize(QtCore.QSize(50,50))

            #Connect Button
            self.picture_button.clicked.connect(self.picture_buttonClick)


            if colum >= 5:
                colum = 0
                row = row +1
            else:
                colum = colum+1
            self.miniature_layout.addWidget(self.picture_button,row,colum)

        self.setLayout(self.layout)

    def create_package_info(self, package):
        self.package = Package(package,False)
        # SET METADATA
        if os.path.isfile(self.package.package_metadata_path) :
            self.metadata = read_dictionary_from_file(self.package.package_metadata_path)
            self.metadata_str = ""
            for key, value in self.metadata.iteritems():
                self.metadata_str = "%s<P><b>%s</b>: %s </P>"%(self.metadata_str, underscore_to_camelcase(key), value)
            self.package_metadata.setText(self.metadata_str)
        #SET PIXMAP
        if os.path.isfile(self.package.package_mini_path):

            pixmap = QtGui.QPixmap(self.package.package_mini_path)
        else:
            pixmap = QtGui.QPixmap(os.path.join(script_root_dir,'img','defaut_package_icon.jpg'))
        self.package_mini.setPixmap(pixmap)

        return

    def create_package_task(self,package_name):
        self.package = Package(package_name)
        clearLayout(self.all_tasks_layout)
        list_task = get_immediate_sub_directories(self.package.package_path)
        for task in list_task:
            self.task = Task(package_name,task)
            task_layout = QtGui.QHBoxLayout()
            task_name_label = QtGui.QLabel(task)
            task_schedule_label= QtGui.QLabel(self.task.schedule)
            task_asigned_to_label= QtGui.QLabel( self.task.asigned_to)
            task_statut_label =  QtGui.QLabel(self.task.statut )
            task_last_user_label = QtGui.QLabel(self.task.last_user)
            task_last_edited_time = QtGui.QLabel( self.task.last_edited_time)
            task_created_by_label = QtGui.QLabel(self.task.created_by )
            self.file_name_without_extention = "%s_%s"%(self.package.package_name,task)
            self.task_file_name_with_ex = get_file_without_extention(self.task.task_path, self.file_name_without_extention)
            task_file_name_with_ex_label = QtGui.QLabel(self.task_file_name_with_ex)
            #Button
            self.open_task_button = QtGui.QPushButton("Open",self)
            self.fodler_task_button = QtGui.QPushButton("Folder",self)
            prev_task_button = QtGui.QPushButton("Prev",self)
            #Connect button
            path = os.path.join(self.task.task_path,"Wip")

            self.open_task_button.clicked.connect(lambda path=self.task.task_path, fname_no_ext=self.file_name_without_extention:open_file_without_extention(path,fname_no_ext))
            self.fodler_task_button.clicked.connect(lambda path=path: open_folder_location(path))
            task_layout.addWidget(task_name_label)
            task_layout.addWidget(task_schedule_label)
            task_layout.addWidget(task_asigned_to_label)
            task_layout.addWidget(task_statut_label)
            task_layout.addWidget(task_last_user_label)
            task_layout.addWidget(task_last_edited_time)
            task_layout.addWidget(task_created_by_label)
            task_layout.addWidget(task_file_name_with_ex_label)
            task_layout.addWidget(self.open_task_button)
            task_layout.addWidget(self.fodler_task_button)
            task_layout.addWidget(prev_task_button)

            self.all_tasks_layout.addLayout(task_layout)






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


