
from wireless_networks import WirelessNetworks

class Application:
    listSensors=[]
    neighboursensors=[]
    onlysensors=[]
    list2dict={}
    path=[]



    def start(self):
        WirelessNetworks.greetMessage()
        print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
        print("_________________________________")
        self.createSensors()

    def createSensors(self):
        no_of_sens= int(input("Enter the number of sensors: "))
        sensorcount=0
        for sensor in range(1,no_of_sens+1):
                sensor=WirelessNetworks()
                if sensorcount>0:
                    print("For next sensor: ")
                sensid=input("Enter the ID for the sensor: ")
                while sensid.isalpha()!=True:
                     print("Please enter a valid ID!")
                     sensid=input("Enter the ID for the sensor: ")
                self.onlysensors.append(sensid)
                self.listSensors.append(sensid)
                
                sensorcount+=1
                sensor.setsensorID(sensid)
                no_of_ns= int(input("Enter the number of neighbours: "))
                
                
                if no_of_ns>=1:
                    try: 
                     for neighbour in range(1,no_of_ns+1):
                         print("For neighbour"+str(neighbour))
                      
                         nid=str(input("Enter the ID for the neighbour: "))
                         while nid.isalpha()!=True:
                              print("Please enter a valid input!!")
                              nid=str(input("Enter the ID for the neighbour: "))
                         self.onlysensors.append(nid)
                         ndist=str(input("Enter the distance from"+str(sensid)+":-"))  #ndist refers to the distance of the neighbour from the main sensor
                         while ndist.isdigit()!=True:
                             print("Invalid input given!! Please enter a valid input!!")
                             ndist=str(input("Enter the distance from"+str(sensid)+":-")) 
                         member=nid,ndist
                         sensor.setneighbour(member)
                        
                         
                         passs=True
                    except Exception:
                        break
                else:
                    print("Invalid input was entered")
                    passs=False
                if passs!=False:
                   
                   oxylevel=int(input("Enter the oxygen level for the sensor (in %): "))
                   while type(oxylevel)!=int:
                       print("This is invalid entry for oxygen level!!")
                       oxylevel=int(input("Enter the oxygen level for the sensor (in %): "))

                   temp=int(input("Enter temperature measurement: "))
                   while type(temp)!=int:
                       print("Invalid entry for temperature!")
                       temp=int(input("Enter temperature measurement: "))
                   sensor.setoxygenlevel(oxylevel)
                   sensor.settemperature(temp)
                   #self.neighbourlist= sensor.getneighbourlst()
                   self.neighboursensors.append(sensor.getneighbourlst())
                   #print(self.neighboursensors)
                   #print(self.listSensors)
        self.convrtToDictionary()           
                #print(sensor)
                #print(f"Sensors ID is{sensor.getsensorID()}")
                


     # the oxygen level is {self.oxygenLevel}, the temperature is {self.temperature}, and the neighbour list is: {self.neighbourlist}")
                #print(sensor)
            #except Exception:
             # break


    def convrtToDictionary(self):
        dict={}
        lsta= self.listSensors
        lstb= self.neighboursensors
        for x in range(0,len(lsta)):
            a= lsta[x]
            b= lstb[x]
            dict[a]=b
        self.list2dict=dict
        print(self.list2dict)
        source=str(input("Enter source sensor: "))
        dest= str(input("Enter destination sensor: "))
        path=[]
        dict=self.list2dict
        self.findPath(dict,source,dest,path)

    def findPath(self,dict,source,dest,path):
        self.path=[]
        
        
        for x in dict:
    
            if source==dest:
                 print("Destination reached!")
                 break

            if dest not in self.onlysensors:
                print("Destination not found!!")
                print("Terminating program")
                break

            for source in dict:
                 self.path.append(source)
                 for i in range(0,len(dict[source])):
                        max= dict[source][0][1]
                        if dict[source][i][1]>max:
                            max= dict[source][i][1]
                            #print(max+"is the longest route")
                            term=dict[source][i][0]
                            self.path.append(term)
                            self.path.remove(term)
                            source=term
                            if source==dest:
                                print("Destination reached")
                                break
                        else:
                            continue
                        if source==dest:
                           print("Destination reached")
                           break
            else:
              self.path.append(dest)
              print("Destination reached")
              break
        
        print("PATH: ",self.path)




        


   

        







