from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QPixmap, QCursor, QBrush, QCloseEvent, QPalette
from PyQt5.QtCore import Qt, QRect,QPoint
from PyQt5.QtWidgets import QMenu
from Utils import PublicData as PD
from Utils.Logging import Get_Logger

def Manipulate(x1,y1_center,direction,qp):
    '''
    Move an object from rotating center to origin, rotate and then move back
    :param x1:
    :param y1_center:
    :param direction:
    :param qp:
    :return:
    '''
    qp.translate(x1, y1_center)
    qp.rotate(direction - 90)
    qp.translate(-x1, -y1_center)
def Get_Runway_Position(x1,y_center,length,width):
    '''
    From start point defination to rectangle defination
    :param start_x:
    :param start_y:
    :param length:
    :param width:
    :return:
    '''
    return x1,y_center-1/2*width,length,width

def Draw_Runway(Runway,qp,colors):
    '''
    Draw a single runway
    :param Runway:
    :param qp:
    :param colors:
    :return:
    '''
    qp.setRenderHint(QPainter.Antialiasing)
    qp.setBrush(colors['runway'])

    # Drawing runway itself
    x1,y1,length,width = Get_Runway_Position(Runway['Position'][0],Runway['Position'][1],Runway['Position'][3],Runway['Position'][4])

    qp.save()
    Manipulate(x1,y1+width/2,Runway['Position'][2],qp)
    qp.drawRect(x1, y1, length, width)

    # Drawing runway name
    text, distance, direction = Runway['Name'][0], Runway['Name'][1], Runway['Name'][2]

    qp.save()
    Manipulate(50, 0, 0, qp)
    # s = QRect(-10, 0, 20, 10)
    qp.setPen(QColor(168, 34, 3))
    qp.setFont(QFont("Decorative", 10))
    qp.drawText(0,0, text)
    qp.restore()
    qp.restore()








def Draw_Runways(Runways,qp,colors):
    """
    Draw runways from the data structure
    :param Runways:
    :param qp:
    :param colors:
    :return:
    """
    for i in range(len(Runways)):
        runway = Runways[i]
        Draw_Runway(runway,qp,colors)
        pass
    pass