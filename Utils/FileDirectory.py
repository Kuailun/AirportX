import os
from Utils import PublicData as PD

def FileSystem_Initialization():
    """
    Check the directory system. If not existing then create
    :return:
    """
    if not os.path.exists(PD.path_Data):
        os.mkdir(PD.path_Data)

    if not os.path.exists(PD.path_Log):
        os.mkdir(PD.path_Log)
    pass

