__author__ = 'Vivarium'
import os
import maya.cmds as cmds
import mtoa.utils as mutils
from maya import OpenMayaUI as omui
from PySide.QtCore import *
from PySide.QtGui import *
from shiboken import wrapInstance

if cmds.objExists("Studio"):
    print 'Studio already created'
else:
    cmds.group(n="Studio", em=True)


mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)

class CreatePolygonUI(QWidget):
    def __init__(self, *args, **kwargs):
        super(CreatePolygonUI, self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Window)
        self.setObjectName('CreatePolygonUI_uniqueId')
        self.setWindowTitle('Create polygon')
        self.setGeometry(50, 50, 250, 150)
        self.initUI()
        self.cmd = 'polyCone'

    def initUI(self):
        self.mainlayout = QVBoxLayout()

        self.combo = QComboBox(self)

        listHdri= self.listHdri()
        self.combo.addItems(listHdri)
        self.combo.setCurrentIndex(0)

        self.combo.activated[str].connect(self.combo_onActivated)

        self.button = QPushButton('Create dome', self)
        self.buttoncyclo = QPushButton ('Create Cyclo', self)
        self.button_sun = QPushButton ("Create Sun", self)
        self.button_camera = QPushButton("Create  DofCamera", self)

        

        self.button.clicked.connect(self.button_onClicked)
        self.buttoncyclo.clicked.connect(self.buttoncyclo_onClicked)
        self.button_sun.clicked.connect(self.button_sun_onClicked)
        self.button_camera.clicked.connect(self.button_cam_onClicked)
        self.mainlayout.addWidget(self.combo)
        self.mainlayout.addWidget(self.button)

        self.mainlayout.addWidget(self.button_sun)
        self.mainlayout.addWidget(self.button_camera)
        self.mainlayout.addWidget(self.buttoncyclo)

        self.setLayout(self.mainlayout)

    def button_cam_onClicked(self):

        cmds.file('Y:/Ressources/CameraRigDof.mb', r=True, namespace='DofCame' )

    def buttoncyclo_onClicked(self):
        #CREATE CURTAIN
        if not cmds.objExists('Cyclo'):
            cmds.polyCube(n="Cyclo", d=20,h=20,w=20)
            cmds.xform("Cyclo", t=[0,10,0])
            deletableFaces = cmds.ls("Cyclo.f[0]","Cyclo.f[1]","Cyclo.f[4]","Cyclo.f[5]")
            cmds.delete(deletableFaces)
            cmds.select("Cyclo.e[5:7]")
            cmds.polySplitRing(sma=30, wt=0.4)
            cmds.select("Cyclo.e[3:5]")
            cmds.polySplitRing(sma=30, wt=0.4)
            cmds.displaySmoothness("Cyclo", po=3)
            cmds.delete("Cyclo", ch=True)
            cmds.parent("Cyclo", "Studio")
        
            #CREATE CURTAIN MATERIAL
            shader = cmds.shadingNode("aiStandard",n="aiStandard#",asShader=True)
            shaderGroup = cmds.sets(renderable=True,n="%sSG"%shader, noSurfaceShader=True,empty=True)
            cmds.connectAttr("%s.outColor"%shader, "%s.surfaceShader"%shaderGroup)
            cmds.setAttr ("%s.diffuseRoughness"%shader, 1);
            cmds.select("Cyclo")
            cmds.hyperShade(assign=shader)
        else:
            print "Cyclo already exist"
  
    def createDomLight(self):
        if cmds.objExists('aiSkyDomeLight1'):
           print "Un dome exist deja"
        else:  
            Dommy = mutils.createLocator("aiSkyDomeLight", asLight=True)
            cmds.setAttr("%s.aiSamples"%Dommy[0], 3)
            cmds.parent(Dommy[1], "Studio")
            
        if cmds.objExists('hdri_file_script'):
            cmds.connectAttr('hdri_file_script.outColor' , 'aiSkyDomeLightShape1.color')
        else:
            self.file_node= cmds.shadingNode("file",asTexture=True, name = "hdri_file_script")
            cmds.connectAttr('%s.outColor' %self.file_node, 'aiSkyDomeLightShape1.color')

        cmds.parent('aiSkyDomeLight1','Studio')

    def listHdri(self):

        listHdri = [os.path.join(root, name)
             for root, dirs, files in os.walk("Y:/Ressources/Hdri")
             for name in files
             if name.endswith((".hdr", ".exr"))]

        return listHdri

    def combo_onActivated(self, text):
        sel = cmds.ls("hdri_file_script")
        print sel
        cmds.setAttr(sel[0] + ".fileTextureName", text, type="string")
        
    def button_sun_onClicked(self):
        if cmds.objExists('sun'):
            print 'Sun already exist'
        else:
            cmds.directionalLight(name='sun')
            cmds.parent('sun','Studio')

    def button_onClicked(self):
        self.createDomLight()

def main():
    ui = CreatePolygonUI()
    ui.show()
    return ui

if __name__ == '__main__':
    main()