import json

class JsonFile():
    def __init__(self):
        self.drawStructure={}
        pass

    def ReadFromPath(self,path):
        """
        Read Json file and parse into data structure
        :param path:
        :return:
        """
        with open(path,'r') as f:
            js=json.load(f)

        return js