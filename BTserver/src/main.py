from time import sleep

from exceptions.exceptions import *

from services.microcontroller import MicroController
from services.api import RequestAPI

from utils.system import System

api = None
arduino = None

def definations():
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
        definations()

def main():

    # TODO: implementar logica para o ar nao fique sendo ligado(quando ja estiver ligado)

    # TODO: corrigir o bug dessa logica
    definations()
    lastStateAir = True
    
    while(True):
        stateAir = api.isActiveAir()
        if( stateAir == True and lastStateAir == False ):
            # arduino.send("ligar")
            print("ligar")
            lastStateAir = True
        
        elif( stateAir == False and lastStateAir == True):
            # arduino.send("desligar")
            print("desligar")
            lastStateAir = False
        sleep(10)
        
if __name__ == "__main__":
    main()

