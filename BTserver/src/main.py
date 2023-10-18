from time import sleep

from exceptions.exceptions import *

from services.microcontroller import MicroController
from services.api import RequestAPI

from utils.system import System

api = None
arduino = None

def __DEFINATIONS():
    global api, arduino
    
    try:
        if(arduino == None):
            arduino = MicroController

        if(api == None):
            api = RequestAPI("INFO22")

        else:
            print("conexao estabelecida")
    
    except NullControllerException as error:
        print(error)

    except InactiveApiException as error:
        print(error)
        sleep(3)
        System.clear()
        print("tentando se conectar novamente...")
        sleep(2)
        System.clear()
        __DEFINATIONS()

def main():

    __DEFINATIONS()    
    lastStateAir = not api.isActiveAir()
    lastTempAir = api.getInfoAir()['temp']

    while(True):
        
        stateAir = api.isActiveAir()
        tempAir = api.getInfoAir()['temp']
        
        if( (stateAir == True and lastStateAir == False) or (tempAir != lastTempAir) ):
            
            # arduino.send(f"(func:on),(temp:{tempAir})")

            print(f"(func:on),(temp:{tempAir})")
            
            lastStateAir = True

            lastTempAir = tempAir

        elif( stateAir == False and lastStateAir == True):
            # arduino.send(f"(func:off)")
            
            print(f"(func:off)")
            
            lastStateAir = False
        sleep(10)
        
if __name__ == "__main__":
    main()

