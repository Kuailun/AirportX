from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QPixmap, QCursor, QBrush, QCloseEvent, QPalette
from PyQt5.QtCore import Qt, QRect,QPoint
from PyQt5.QtWidgets import QMenu
from Utils import PublicData as PD
from Utils.Logging import Get_Logger



class AirportX(QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables:
        self.mode = {"Fixed":0,"Drag":1,"Airplane":2}
        self.currentMode=self.mode['Fixed']
        self.mapdata={}
        self.viewdata={}
        self.colors = {}

        self.dragging=False             # Whether is being dragged
        self.viewOffset=[0,0]           # Current drag offset
        self.viewOffsetFixed=[0,0]      # Dragging offset in total

        self.initUI()


    def initUI(self):
        """
        Initialize the UI
        :return:
        """
        self.move(100, 100)
        self.resize(1000,1000)

        # Set the window name
        self.setWindowTitle('AirportX')
        # self.actionTitlebar_Change(PD.data_Config.InstrumentX_Titlebar)

        # Set the right click menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)

        # Set background black
        palette=QPalette()
        palette.setColor(palette.Background,QColor(0,0,0))
        self.setPalette(palette)

        self.SetColors()

        self.update()
        self.show()
        pass

    def SetColors(self):
        """
        Set QColors in to data structure
        :return:
        """
        self.colors['Background']=QColor(0,0,0)
        self.colors['runway']=QColor(220,220,220)

    def SetData(self,js):
        """
        Set the data structure in mainwindow
        :param js:
        :return:
        """
        logger=Get_Logger("SetData")
        logger.info("Set data into data structure")
        self.mapdata=js

        self.viewdata["view_x"] = self.mapdata["Drawing"]["GeneralInfo"][0]
        self.viewdata["view_y"] = self.mapdata["Drawing"]["GeneralInfo"][1]
        pass

    def rightMenuShow(self):
        """
        Handle the right click menu
        :return:
        """
        try:
            self.contextMenu = QMenu()

            # Second level menu
            self.menuMode = self.contextMenu.addMenu(u'Display Mode')
            self.menuDisplay_0 = self.menuMode.addAction(u'Mode-Fixed')
            self.menuDisplay_1 = self.menuMode.addAction(u'Mode-Drag')
            self.menuDisplay_2 = self.menuMode.addAction(u'Mode-Airplane')

            self.menuFullscreen = self.contextMenu.addAction(u'Fullscreen')
            self.menuReset = self.contextMenu.addAction(u'Reset')
            self.menuQuit = self.contextMenu.addAction(u'Quit')
            self.menuAbout = self.contextMenu.addAction(u'About')

            self.menuQuit.triggered.connect(self.actionQuit)
            self.menuDisplay_0.triggered.connect(self.actionDisplay_0)
            self.menuDisplay_1.triggered.connect(self.actionDisplay_1)
            self.menuDisplay_2.triggered.connect(self.actionDisplay_2)

            self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
            self.contextMenu.show()
        except Exception as e:
            print(e)

    def actionDisplay_0(self):
        """
        Change current mode to Fixed
        :return:
        """
        logger=Get_Logger("actionDisplay_0")
        logger.info("Switch to Fixed view mode")
        self.currentMode=self.mode['Fixed']
        self.viewOffset=[0,0]
        self.viewOffsetFixed=[0,0]
        self.update()
        pass

    def actionDisplay_1(self):
        """
        Change current mode to Drag
        :return:
        """
        logger = Get_Logger("actionDisplay_1")
        logger.info("Switch to Drag view mode")
        self.currentMode=self.mode['Drag']
        self.update()
        pass

    def actionDisplay_2(self):
        """
        Change current mode to Airplane
        :return:
        """
        logger = Get_Logger("actionDisplay_2")
        logger.info("Switch to Airplane view mode")
        self.currentMode=self.mode['Airplane']
        self.update()
        pass

    def actionQuit(self):
        """
        Quit the InstrumentX
        :return:
        """
        # JP.Json_SaveFile()
        self.hide()
        self.close()

    def closeEvent(self, event):
        """
        Handle the event of closing
        :param event:
        :return:
        """
        # JP.Json_SaveFile()
        pass

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.translate(self.viewOffsetFixed[0]+self.viewOffset[0],self.viewOffsetFixed[1]+self.viewOffset[1])


        if not(self.mapdata=={}):
            Runways=self.mapdata['Drawing']['DetailInfo']['Runways']
            for i in range(len(Runways)):
                qp.setRenderHint(QPainter.Antialiasing)
                qp.setBrush(self.colors['runway'])
                runway=Runways[i]
                x=runway['Data'][0]
                y=runway['Data'][1]-runway['Data'][4]/2
                length=runway['Data'][3]
                width=runway['Data'][4]
                qp.translate(x, y + runway['Data'][4] / 2)
                qp.rotate(runway['Data'][2]-90)
                qp.translate(-x,-y-runway['Data'][4]/2)
                # qp.rotate(runway['Data'][2])
                qp.drawRect(x,y,length,width)
                # qp.end()
            # qp.begin(self)
            # qp.drawLine(100,25,10,25)
            # qp.end()
            # Apron=self.mapdata['Drawing']['DetailInfo']['Apron']
            # for i in range(len(Apron)):
            #     type=Apron[i]['Type']
            #     if(type=='Circle'):
            #         circles=Apron[i]['Data']
            #         for j in range(len(circles)):
            #             qp.drawEllipse(circles[j][0],circles[j][1],circles[j][2],circles[j][2])
            #         pass
            #     elif(type=='Lines'):
            #         lines = Apron[i]['Data']
            #         for j in range(len(lines)):
            #             qp.drawLine(lines[j][0], lines[j][1], lines[j][2], lines[j][3],)
            #         pass
            #     elif (type == 'Texts'):
            #         arcs = Apron[i]['Data']
            #         for j in range(len(arcs)):
            #             qp.drawArc(arcs[j][0], arcs[j][1], arcs[j][2], arcs[j][3], 90*16,90*16)
            #         pass
            #     pass
            qp.end()
        pass
    def mousePressEvent(self,event):
        """
        Handle the drag event
        :param event:
        :return:
        """
        if(event.button()==Qt.LeftButton and self.currentMode==self.mode["Drag"]):
            self.dragging=True
            self.dragging_pos=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            pass
        pass

    def mouseReleaseEvent(self, event):
        if (event.button() == Qt.LeftButton and self.currentMode == self.mode["Drag"]):
            self.dragging = False
            self.setCursor(QCursor(Qt.ArrowCursor))
            event.accept()
            self.viewOffsetFixed=[self.viewOffsetFixed[0]+self.viewOffset[0],self.viewOffsetFixed[1]+self.viewOffset[1]]
            pass
        pass

    def mouseMoveEvent(self, event):
        if(Qt.LeftButton and self.dragging):
            offset=event.globalPos()-self.pos()
            offset=offset-self.dragging_pos
            self.viewOffset=[offset.x(),offset.y()]
            self.update()

