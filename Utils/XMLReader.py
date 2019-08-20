from xml.etree.ElementTree import Element
import xml.etree.cElementTree as ET

class XMLFile():
    def __init__(self):
        self.drawStructure={}
        pass

    def ReadFromPath(self,path):
        """
        Read XML file and parse into data structure
        :param path:
        :return:
        """
        f=ET.parse(path)

        airportX=f.getroot()
        description=airportX.find("Description")
        drawing=airportX.find("Drawing")

        generalInfo=drawing.find("GeneralInfo")
        self.drawStructure['center_x']=generalInfo.find("center_x").text
        self.drawStructure['center_y'] = generalInfo.find("center_y").text

        detailInfo=drawing.find("DetailInfo")
        runways=detailInfo.find('runways')
        # apron=detailInfo.find('apron')
        # apron_sub=apron.getchildren()
        # for i in range(len(apron_sub)):
        #     if(apron_sub[i].tag=="Polygons"):
        #
        #         polygonList=apron_sub.findall("Polygons")
        #         for i in range(len(polygonList)):
        #             polygon=polygonList[i].findall('Polygon')
        #             for j in range(len(polygonList)):
        #                 pass
        #             pass
        #         pass
        #     elif(apron_sub[i].tag=="Circles"):
        #         pass
        #     elif (apron_sub[i].tag == "Lines"):
        #         pass
        #     elif (apron_sub[i].tag == "Arcs"):
        #         pass
        #     elif (apron_sub[i].tag == "Texts"):
        #         pass
