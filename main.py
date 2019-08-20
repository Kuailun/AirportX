from PyQt5.QtWidgets import QApplication
import sys
from Utils.Logging import Get_Logger
from Utils import FileDirectory as FD
from Utils import XMLReader as xml
from Utils import JsonReader as js
from AirportX import AirportX

if __name__ == "__main__":
    # 检查文件夹结构
    FD.FileSystem_Initialization()

    # 初始化日志系统
    Logger=Get_Logger("Main")
    Logger.info("Log Initialization Done!")

    # 初始化xml解析器
    mXML=xml.XMLFile()
    # data=mXML.ReadFromPath('Data/ZBAA.xml')

    # 初始化xml解析器
    mJson=js.JsonFile()
    data=mJson.ReadFromPath('Data/ZBAA.json')

    # 检查Json文件是否存在，存在则读取，不存在创建默认并读取
    # JP.Json_Initialization()

    # 初始化InstrumentX
        # TODO：初始化网络连接
    app=QApplication(sys.argv)
    airportX=AirportX()
    airportX.SetData(data)
    Logger.info("AirportX is running")
    airportX.show()

    app.exec()
    Logger.info("AirportX has exited")