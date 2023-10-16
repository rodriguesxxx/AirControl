import serial

from exceptions.exceptions import NullControllerException

class MicroController:

    def __init__(self):
        # self.controller = self.btConnect()
        pass

    


    """ 
        CONECTE O MODULO BT AO NOTEBOOK DE FORMA MANUAL,
        LOGO APOS A CONECXAO, RODE O SEGUINTE COMANDO: <hcitool dev>
        ISSO MOSTRARA A PORTA BT.
    """

    def btConnect(self):
        bt_port = "/dev/rfcomm0"  # Substitua pelo caminho do seu dispositivo Bluetooth no sistema (pode variar)
        try:
            return serial.Serial(bt_port, 9600)
        except Exception:
            raise NullControllerException("Houve um erro ao instanciar o controller, cheque a porta bt")

    
    def send(self, msg):
        self.controller.write(msg.encode())

    def receive(self):
        return self.controller.readline().encode().strip()
    
    
    
