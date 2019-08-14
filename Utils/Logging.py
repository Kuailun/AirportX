import logging
from Utils import PublicData as PD
from Utils import FileDirectory as FD

# 检查文件夹结构
FD.FileSystem_Initialization()

'''Logging设置'''
with open(PD.path_Log+"/Log.txt","w") as f:
    f.close()
logger=logging.getLogger("AirportX")
logger.setLevel(level=logging.INFO)
handler=logging.FileHandler(PD.path_Log+"/Log.txt")
handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console=logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(handler)

def Get_Logger(name):
    """
    Get the logger for each module
    :param name: sub module name
    :return: A logger
    """
    return logging.getLogger("AirportX."+name)