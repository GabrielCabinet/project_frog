#!/usr/bin/env python

############################################################################
# 
#  Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
# 
#  This file is part of the example classes of the Qt Toolkit.
# 
#  This file may be used under the terms of the GNU General Public
#  License version 2.0 as published by the Free Software Foundation
#  and appearing in the file LICENSE.GPL included in the packaging of
#  this file.  Please review the following information to ensure GNU
#  General Public Licensing requirements will be met:
#  http://www.trolltech.com/products/qt/opensource.html
# 
#  If you are unsure which license is appropriate for your use, please
#  review the following information:
#  http://www.trolltech.com/products/qt/licensing.html or contact the
#  sales department at sales@trolltech.com.
# 
#  This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
#  WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
# 
############################################################################

# This is only needed for Python v2 but is harmless for Python v3.
#import sip
#sip.setapi('QString', 2)

import qdarkstyle


from app.package import *
from app.comment import *

session_config = SessionConfig()
project = Project(session_config.session_project_name)
project_root = project.project_root
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.show_mangement_window()


        self.session_config = SessionConfig()
        self.project = Project(session_config.session_project_name)
        self.project_root = self.project.project_root

        self.textEdit = QtGui.QTextEdit()

        img_path = os.path.join(script_root_dir,'img/logo.jpg')
        pixmap = QtGui.QPixmap(img_path)
        self.lbl_logo = QtGui.QLabel()
        self.lbl_logo.setPixmap(pixmap)
        self.setCentralWidget(self.lbl_logo)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()

        self.create_dock_contact_sheet()
        self.create_dock_package_info()
        self.create_dock_arborescence()

        self.setWindowTitle("Dock Widgets")


        self.setUnifiedTitleAndToolBarOnMac(True)



    def undo(self):
        document = self.textEdit.document()
        document.undo()

    def insertCustomer(self, customer):
        if not customer:
            return
        customerList = customer.split(', ')
        document = self.textEdit.document()
        cursor = document.find('NAME')
        if not cursor.isNull():
            cursor.beginEditBlock()
            cursor.insertText(customerList[0])
            oldcursor = cursor
            cursor = document.find('ADDRESS')
            if not cursor.isNull():
                for i in customerList[1:]:
                    cursor.insertBlock()
                    cursor.insertText(i)
                cursor.endEditBlock()
            else:
                oldcursor.endEditBlock()

    def addParagraph(self, paragraph):
        if not paragraph:
            return
        document = self.textEdit.document()
        cursor = document.find("Yours sincerely,")
        if cursor.isNull():
            return
        cursor.beginEditBlock()
        cursor.movePosition(QtGui.QTextCursor.PreviousBlock,
                QtGui.QTextCursor.MoveAnchor, 2)
        cursor.insertBlock()
        cursor.insertText(paragraph)
        cursor.insertBlock()
        cursor.endEditBlock()

    def about(self):
        QtGui.QMessageBox.about(self, "About Dock Widgets",
                "The <b>Dock Widgets</b> example demonstrates how to use "
                "Qt's dock widgets. You can enter your own text, click a "
                "customer to add a customer name and address, and click "
                "standard paragraphs to add them.")

    def createActions(self):




        self.quitAct = QtGui.QAction("&Quit", self, shortcut="Ctrl+Q",
                statusTip="Quit the application", triggered=self.close)

        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")


        self.fileMenu.addAction(self.quitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")


        self.viewMenu = self.menuBar().addMenu("&View")

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")



        self.editToolBar = self.addToolBar("Edit")


    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def picture_buttonClick(self):
        package_name = (self.sender().text())
        self.package = Package(package_name)
        self.create_metadata_package()
        self.create_comment_package()
        #self.create_task_package()
        self.tree_focus()

    def tree_focus(self):
        model = QtGui.QFileSystemModel()

        caca = self.tree.currentIndex().data()
        path = "D://project_viva//%s"%(caca)
        print path
        model.setRootPath(path)
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(path))




############ARBO#########################################
    def create_dock_arborescence(self):
        '''
        Init dock package information.
        Dock package information groupe:
        -The preview
        -Comments
        -Tasks
        :param package: name of the package
        :return:
        '''

        dock = QtGui.QDockWidget("Arborescence", self)


        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath("D://project_viva")
        self.model.setNameFilters(['metadata','comment'])

        self.tree = QtGui.QTreeView()
        self.tree.setModel(self.model)

        self.tree.setRootIndex(self.model.index("D://project_viva"))
        self.tree.setAnimated(True)

        self.tree.setWindowTitle("Dir View")
        self.tree.setModel(self.model)

        self.tree.clicked[QtCore.QModelIndex].connect(self.tree_focus)

     #   self.create_metadata_package()

        dock.setWidget(self.tree)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())
#############DOCK INFO####################################









    def create_dock_package_info(self, package=""):
        '''
        Init dock package information.
        Dock package information groupe:
        -The preview
        -Comments
        -Tasks
        :param package: name of the package
        :return:
        '''

        dock = QtGui.QDockWidget("Package Info", self)
        #Init widget
        self.package_info_widget = QtGui.QWidget()
        self.package_info_layout = QtGui.QVBoxLayout(self.package_info_widget)
        self.package_info_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.package_comment_widget = QtGui.QWidget()
        self.package_comment_layout = QtGui.QVBoxLayout(self.package_comment_widget)
        self.package_info_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.all_tasks_widget = QtGui.QWidget()
        self.all_tasks_layout = QtGui.QGridLayout(self.all_tasks_widget)

        # Create package preview layout
        self.package_preview_widget =QtGui.QWidget()
        self.package_preview_layout = QtGui.QHBoxLayout(self.package_preview_widget)
        self.package_mini = QtGui.QLabel("Task Miniature:")
        self.package_metadata = QtGui.QLabel("Metadata:")
        self.package_preview_layout.addWidget(self.package_mini)
        self.package_preview_layout.addWidget(self.package_metadata)

        #Add widget to main layout
        self.package_info_splitter.addWidget(self.package_preview_widget)
        self.package_info_splitter.addWidget(self.package_comment_widget)
        self.package_info_splitter.addWidget(self.all_tasks_widget)
        self.package_info_layout.addWidget(self.package_info_splitter)



     #   self.create_metadata_package()

        dock.setWidget(self.package_info_splitter)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

    def create_task_package(self):
        row = 0
        clearLayout(self.all_tasks_layout)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Task"),row,1)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Schedule"),row,2)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Asigned to"),row,3)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Statut"),row,4)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Last user"),row,5)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Last edited"),row,6)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Created by"),row,7)
        self.all_tasks_layout.addWidget(QtGui.QLabel("File"),row,8)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Open"),row,9)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Folder"),row,10)
        self.all_tasks_layout.addWidget(QtGui.QLabel("Preview"),row,11)


        list_task = get_immediate_sub_directories(self.package.package_path)

        for task in list_task:
            self.task = Task(self.package.package_name,task)
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

            row = row+1

            self.all_tasks_layout.addWidget(task_name_label,row,1)
            self.all_tasks_layout.addWidget(task_schedule_label,row,2)
            self.all_tasks_layout.addWidget(task_asigned_to_label,row,3)
            self.all_tasks_layout.addWidget(task_statut_label,row,4)
            self.all_tasks_layout.addWidget(task_last_user_label,row,5)
            self.all_tasks_layout.addWidget(task_last_edited_time,row,6)
            self.all_tasks_layout.addWidget(task_created_by_label,row,7)
            self.all_tasks_layout.addWidget(task_file_name_with_ex_label,row,8)
            self.all_tasks_layout.addWidget(self.open_task_button,row,9)
            self.all_tasks_layout.addWidget(self.fodler_task_button,row,10)
            self.all_tasks_layout.addWidget(prev_task_button,row,11)

    def create_comment_package(self):
        '''
        Create a layout for the package comment
        :return:
        '''
        clearLayout(self.package_comment_layout)
        #Button Comment
        self.comment_edit_button = QtGui.QPushButton("Edit")
        self.comment_edit_button.clicked.connect(lambda: open_file_to_bloc_note(all_com.comment_file_path))

        self.comment_add_button = QtGui.QPushButton("Add")
        self.comment_add_text = QtGui.QTextEdit("New comment")
        self.comment_add_button.clicked.connect(lambda: self.add_new_comment())

        self.comment_button_layout = QtGui.QHBoxLayout()
        self.comment_button_layout.addWidget(self.comment_edit_button)
        self.comment_button_layout.addWidget(self.comment_add_button)


        #Scroll on comment
        self.scroll_comment = QtGui.QScrollArea()
        self.scroll_comment.setWidgetResizable(True)
        self.scroll_comment.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.com_grid_widget = QtGui.QWidget()
        self.com_grid_layout = QtGui.QGridLayout(self.com_grid_widget)

        all_com = Comment(self.package.package_name)
        row = 0
        colum = 0

        for com in sorted(all_com.comment_dictionary.keys(), reverse=True):
            comment_text = all_com.comment_dictionary[com].get('comment','unknown')
            comment_text_label = QtGui.QLabel(str(comment_text))
            comment_date_label = QtGui.QLabel(all_com.comment_dictionary[com].get('date','unknown'))
            comment_file_label = QtGui.QLabel(all_com.comment_dictionary[com].get('file','unkown'))
            comment_user_label = QtGui.QLabel(all_com.comment_dictionary[com].get('user','unkown'))
            self.com_grid_layout.addWidget(comment_date_label,row,0)
            self.com_grid_layout.addWidget(comment_text_label,row,1)
            self.com_grid_layout.addWidget(comment_file_label,row,2)
            self.com_grid_layout.addWidget(comment_user_label,row,3)
            row = row + 1



        self.scroll_comment.setWidget(self.com_grid_widget)
        self.package_comment_layout.addWidget(self.scroll_comment)
        self.package_comment_layout.addLayout(self.comment_button_layout)
        self.package_comment_layout.addWidget(self.comment_add_text)

    def add_new_comment(self):
        comment_txt = str(self.comment_add_text.toPlainText())
        new_com = Comment(self.package.package_name, True, comment_txt)
        self.create_comment_package()

    def create_metadata_package(self):
        '''
        Get information package.
        :param package: package class
        :type package: class
        :return:
        '''

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


###########DOCK CONTACT SHEET###################################
    def create_dock_contact_sheet(self):
        '''
        Create a contact sheet of all package
        :return:
        '''


        self.contact_sheet_widget = QtGui.QWidget()
        self.contact_sheet_layout = QtGui.QGridLayout(self.contact_sheet_widget)


        row = 0
        colum = -1
        #Create Dock
        dock = QtGui.QDockWidget("Contact Sheet", self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)

        #Create defaut pixmap
        self.defaut_pixmap = QtGui.QPixmap(os.path.join(script_root_dir,'img','defaut_package_icon.jpg'))
        self.defaut_package_ico = QtGui.QIcon(self.defaut_pixmap)

        #List package and create miniature
        self.list_packages = list_packages(project_root)

        for package in self.list_packages:

            # Create layout for package img and metadata

            self.package = package
            #Create miniature and comment.
            mini_filename = "%s_mini.jpg"%(package)

            self.mini_file_path = os.path.join(project_root,package,mini_filename)


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

            self.contact_sheet_layout.addWidget(self.picture_button,row,colum)

        self.scroll = QtGui.QScrollArea()

        self.scroll.setWidgetResizable(True)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scroll.setWidget(self.contact_sheet_widget)




        dock.setWidget(self.scroll)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())



    def show_mangement_window(self):
        p=ManagementWindow(self)
        p.show()


class ManagementWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle('PRC Editor')
        self.resize(100,100)

        self.create_dock_management_package()


    def create_dock_management_package(self):

        self.management_main_widget = QtGui.QWidget()
        self.management_main_layout = QtGui.QVBoxLayout(self.management_main_widget)

        row = 0
        colum = -1

        self.info_package_layout = QtGui.QHBoxLayout()
        self.layout_cut_in_cut_out= QtGui.QHBoxLayout()
        self.all_tasks_layout = QtGui.QVBoxLayout()
        self.all_tasks_layout_groupbox = QtGui.QGroupBox("Tasks")
        self.all_tasks_layout_groupbox.setLayout(self.all_tasks_layout)

        #Create Widget
        self.package_name_edit = QtGui.QLineEdit('Nom_du_package_001')   #Layout name edit
        self.package_kind_combo = QtGui.QComboBox(self)   #Layout combopackge
        self.package_kind_combo.addItem("Prop")
        self.package_kind_combo.addItem("Back")
        self.package_kind_combo.addItem("Char")
        self.package_kind_combo.addItem("Shot")

        self.sequence_combo = QtGui.QComboBox(self)   #Layout combopackge
        sequence_list =  ast.literal_eval(read_text_file(os.path.join(script_root_dir,'data\sequence')))
        for sequence in sequence_list:
            self.sequence_combo.addItem(sequence)

        self.create_new_task_button = QtGui.QPushButton('+ Task ')
        #Create Widget User
        self.user_asigned_to_combo = QtGui.QComboBox(self)
        self.user = User()
        for user in self.user.all_user_dictionary.keys():
            self.user_asigned_to_combo.addItem(user)

        self.create_new_package_button = QtGui.QPushButton('Create')

        #Add widget/layoyut to main
        self.info_package_layout.addWidget(self.package_name_edit)
        self.info_package_layout.addWidget(QtGui.QLabel('Type'))
        self.info_package_layout.addWidget(self.package_kind_combo)
        self.info_package_layout.addWidget(QtGui.QLabel('AssignTo'))
        self.info_package_layout.addWidget(self.user_asigned_to_combo)
        self.info_package_layout.addLayout(self.layout_cut_in_cut_out)
        self.info_package_layout.addWidget(self.sequence_combo)
        self.info_package_layout.addWidget(self.create_new_package_button)
        self.management_main_layout.addLayout(self.info_package_layout)
        self.management_main_layout.addWidget(self.create_new_task_button)


        self.management_main_layout.addWidget( self.all_tasks_layout_groupbox)
        self.uptdate_task_list ('Back')

        #Connect
        self.package_kind_combo.activated[str].connect(self.on_combo_box_Activated)   #Connect combobox
        self.create_new_package_button.clicked.connect(self.on_create_new_package_cliked)
        self.create_new_task_button.clicked.connect(self.add_new_task_gui)


        self.scroll = QtGui.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.management_main_widget)


        self.holder_scroll_layout = QtGui.QHBoxLayout()
        self.holder_scroll_layout.addWidget(self.scroll)
        self.setLayout(self.holder_scroll_layout)


    def uptdate_task_list(self, kind):
        '''
        Create all the task of a template. (modelling,shading...)
        :param kind:
        :return:
        '''
        script_root_dir = os.path.abspath(__file__ + "/../../")

        project_database_file_path = os.path.join(script_root_dir,'data\project_database')
        template_all_task = read_dictionary_from_file(os.path.join(script_root_dir,'data\\template'))
        print template_all_task
        clearLayout(self.all_tasks_layout)
        self.tasks_list_template = template_all_task.get(kind,'unknown')
        self.user.all_user_dictionary = read_dictionary_from_file(os.path.join(script_root_dir,'data/user_database.txt'))
        for task in self.tasks_list_template:
            self.add_new_task_gui(task,self.user.all_user_dictionary)

    def add_new_task_gui(self,task="", all_user_dic={}):
        '''
        Create one task
        :param task: task name
        :param all_user_dic: combo box of users
        :return:
        '''
        if all_user_dic is {}:
            self.user.all_user_dictionary = read_dictionary_from_file(os.path.join(script_root_dir,'data/user_database.txt'))
        task_layout = QtGui.QHBoxLayout()
        self.task_name = QtGui.QLineEdit(task)
        self.label_task_name= QtGui.QLabel('Task name:')
        self.label_asigned = QtGui.QLabel('Asigned To:')
        self.label_schedule= QtGui.QLabel('Schedule:')
        self.user_asigned_to_combo = QtGui.QComboBox(self)
        self.user_asigned_to_combo.addItem('All')
        self.schedule_date_time = QtGui.QDateEdit()
        self.schedule_date_time.setDateTime(QtCore.QDateTime.currentDateTime())
        self.file_type_combo_box = QtGui.QComboBox(self)
        self.file_type_combo_box.addItems(["Maya.mb","Nuke.nk","3dsmax.max","ZBrush.zpr"])


        for user in self.user.all_user_dictionary.keys():
            self.user_asigned_to_combo.addItem(user)


        task_layout.addWidget(self.label_task_name)
        task_layout.addWidget(self.task_name)
        task_layout.addWidget(self.label_asigned)
        task_layout.addWidget(self.user_asigned_to_combo)
        task_layout.addWidget(self.label_schedule)
        task_layout.addWidget(self.schedule_date_time)
        task_layout.addWidget(self.file_type_combo_box)
        self.all_tasks_layout.addLayout(task_layout)


    def on_create_new_package_cliked(self):
        self.package = Package(str(self.package_kind_combo.currentText())+"_"+str(self.package_name_edit.text()),
                          True ,
                          str(self.package_kind_combo.currentText()),
                          'Un chouette test de package',
                          str(self.user_asigned_to_combo.currentText()),
                          str(self.sequence_combo.currentText())
                         )

        item_task = (self.all_tasks_layout.layout().itemAt(i) for i in range(self.all_tasks_layout.layout().count()))
        for task_layout in item_task:
            self.task_name = task_layout.layout().itemAt(1).widget().text()  # Get the task name QtGui.all_task_layout.QtGui.taskLayout.QtGui.QLineEdit
            self.assigned = str(task_layout.layout().itemAt(3).widget().currentText())
            self.schedule = task_layout.layout().itemAt(5).widget().dateTime().toString("yyyy.MM.dd")
            self.file_type = str(task_layout.layout().itemAt(6).widget().currentText())
            # TASK CREATION (folder, subfolder,metadata)
            self.task = Task(self.package.package_name,self.task_name,True,'new',self.schedule,self.assigned,self.file_type)



    def on_combo_box_Activated(self, text):
        clearLayout(self.layout_cut_in_cut_out)
        self.uptdate_task_list(text)
        if text == "Shot":
            self.cut_in = QtGui.QSpinBox()
            self.cut_in.setSingleStep(1)

            self.cut_out = QtGui.QSpinBox()
            self.cut_out.setSingleStep(1)
            self.cut_in.setMaximum(666666)
            self.cut_out.setMaximum(666666)
            self.layout_cut_in_cut_out.addWidget(QtGui.QLabel('cutIn'))
            self.layout_cut_in_cut_out.addWidget(self.cut_in)
            self.layout_cut_in_cut_out.addWidget(QtGui.QLabel('cutOut'))
            self.layout_cut_in_cut_out.addWidget(self.cut_out)

        else:
            clearLayout(self.layout_cut_in_cut_out)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
