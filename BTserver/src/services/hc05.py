import serial
import os
import time

from exceptions.exceptions import NullControllerException

class MicroController:

    def __init__(self):
        self.controller = self.btConnect()
        pass

    


    """ 
        CONECTE O MODULO BT AO NOTEBOOK DE FORMA MANUAL,
        LOGO APOS A CONECXAO, RODE O SEGUINTE COMANDO: <hcitool dev>
        ISSO MOSTRARA A PORTA BT.
    """

    def btConnect(self):
        
        bt_address = "98:D3:41:F6:A9:2C"
        rfcomm_port = 2
        bt_port = f"/dev/rfcomm{rfcomm_port}"
        os.system(f"nohup sudo rfcomm connect {rfcomm_port} {bt_address} &")
        time.sleep(5)

        try:
            return serial.Serial(bt_port, 9600)
        except Exception:
            raise NullControllerException("Erro ao se conectar o modulo BT, cheque se o modulo esta pariado e tente novamente...")

    
    def send(self, msg):
        self.controller.write(msg.encode())

    def receive(self):
        return self.controller.readline().encode().strip()
    
    
    
