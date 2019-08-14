from PyQt5.QtWidgets import QApplication
import sys
from Utils.Logging import Get_Logger
from Utils import FileDirectory as FD
from AirportX import AirportX

if __name__ == "__main__":
    # 检查文件夹结构
    FD.FileSystem_Initialization()

    # 初始化日志系统
    Logger=Get_Logger("Main")
    Logger.info("Log Initialization Done!")

    # 检查Json文件是否存在，存在则读取，不存在创建默认并读取
    # JP.Json_Initialization()

    # 初始化InstrumentX
        # TODO：初始化网络连接
    app=QApplication(sys.argv)
    instrumentX=AirportX()
    Logger.info("InstrumentX is running")
    instrumentX.show()

    app.exec()
    Logger.info("InstrumentX has exited")