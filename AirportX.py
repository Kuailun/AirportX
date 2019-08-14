from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QPixmap, QCursor, QBrush, QCloseEvent
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMenu
from Utils import PublicData as PD
from Utils.Logging import Get_Logger


class AirportX(QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables:
        self.is_debug = False
        self.initUI()

    def initUI(self):
        """
        Initialize the UI
        :return:
        """
        # self.move(PD.data_Config.InstrumentX_X, PD.data_Config.InstrumentX_Y)
        # self.resize(PD.data_Config.InstrumentX_Width, PD.data_Config.InstrumentX_Height)

        # Set the window name
        self.setWindowTitle('AirportX')
        # self.actionTitlebar_Change(PD.data_Config.InstrumentX_Titlebar)

        # Set the right click menu
        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.rightMenuShow)

        self.update()
        self.show()
        pass

    # def rightMenuShow(self):
    #     """
    #     Handle the right click menu
    #     :return:
    #     """
    #     try:
    #         self.contextMenu = QMenu()
    #         self.menuConfig = self.contextMenu.addAction(u'Configuration')
    #         self.menuSetupMode = self.contextMenu.addAction(u'Display Setup mode F12')
    #
    #         # Second level menu
    #         self.menuDisplays = self.contextMenu.addMenu(u'Displays')
    #         self.menuDisplay_1 = self.menuDisplays.addAction(u'Display-1')
    #         self.menuDisplay_2 = self.menuDisplays.addAction(u'Display-2')
    #
    #         self.menuFullscreen = self.contextMenu.addAction(u'Fullscreen')
    #         self.menuTitlebar = self.contextMenu.addAction(u'Titlebar')
    #         self.menuReset = self.contextMenu.addAction(u'Reset')
    #         self.menuStatus = self.contextMenu.addAction(u'Status')
    #         self.menuQuit = self.contextMenu.addAction(u'Quit')
    #         self.menuAbout = self.contextMenu.addAction(u'About')
    #
    #         self.menuConfig.triggered.connect(self.actionHandler)
    #         self.menuSetupMode.triggered.connect(self.actionSetupMode)
    #         self.menuTitlebar.triggered.connect(self.actionTitlebar)
    #         self.menuQuit.triggered.connect(self.actionQuit)
    #
    #         self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
    #
    #         self.contextMenu.show()
    #     except Exception as e:
    #         print(e)
    #
    # def actionHandler(self):
    #     print('action')
    #
    # def actionSetupMode(self):
    #     """
    #     The function for right click menu for Setup Mode
    #     :return:
    #     """
    #     self.is_debug = not self.is_debug
    #     logger = Get_Logger("actionSetupMode")
    #     logger.info("Setup Mode Pressed")
    #     self.repaint()
    #     pass
    #
    # def actionTitlebar(self):
    #     """
    #     The function for right click menu for titlebar
    #     :return:
    #     """
    #     PD.data_Config.InstrumentX_Titlebar = not PD.data_Config.InstrumentX_Titlebar
    #     self.actionTitlebar_Change(PD.data_Config.InstrumentX_Titlebar)
    #     pass
    #
    # def actionTitlebar_Change(self, status):
    #     """
    #     Change window from frameless to having frame and vice versa
    #     :param status:
    #     :return:
    #     """
    #     logger = Get_Logger("Titlebar_Change")
    #     logger.info("Titlebar Pressed" + str(status))
    #     if (status):
    #         self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
    #         self.show()
    #         pass
    #     else:
    #         self.setWindowFlags(Qt.FramelessWindowHint)
    #         self.show()
    #         pass
    #
    #     self.update()
    #     pass
    #
    # def actionQuit(self):
    #     """
    #     Quit the InstrumentX
    #     :return:
    #     """
    #     JP.Json_SaveFile()
    #     self.hide()
    #     self.close()

    def resizeEvent(self, event):
        """
        Handle the change of window size
        :param event:
        :return:
        """
        # logger = Get_Logger("InstrumentX-resizeEvent")
        # PD.data_Config.InstrumentX_Height = event.size().height()
        # PD.data_Config.InstrumentX_Width = event.size().width()
        pass

    def moveEvent(self, event):
        """
        Handle the change of window move
        :param event:
        :return:
        """
        # logger = Get_Logger("InstrumentX-moveEvent")
        # PD.data_Config.InstrumentX_X = event.pos().x()
        # PD.data_Config.InstrumentX_Y = event.pos().y()
        pass

    def closeEvent(self, event):
        """
        Handle the event of closing
        :param event:
        :return:
        """
        # JP.Json_SaveFile()
        pass

    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        qp.fillRect(QRect(0, 0, self.size().width(), self.size().height()), QBrush(Qt.black))

        qp.setPen(QColor(166,66,250))
        qp.drawPie(100,100,200,200,0*16,120*16)
        qp.drawText(120, 120, "文字")
        qp.end()
        pass

