
class WirelessNetworks:
    ADHOC_Mode= "ON"
    BRAND_NAME= "Cisco"

    def __init__(self):
        self.id= ""
        self.oxygenLevel=0
        self.temperature=0
        self.neighbourlist=[]


   

    @staticmethod
    def greetMessage():
        
        print("Hello Welcome to the company's IoT-Based Health System")
        print("***********************************************")
        print("These are sensors of Cisco brand, and their Ad Hoc Mode is ON")



    def setsensorID(self,sensid):
       self.id= sensid
    def getsensorID(self):
        return self.id

    def setoxygenlevel(self,oxylvl):
        self.oxygenLevel=oxylvl
    def settemperature(self,temp):
        self.temperature=temp

    def setneighbour(self,neighbour):
        self.neighbourlist.append(neighbour)

    def getneighbourlst(self):
        return self.neighbourlist

    

   
    