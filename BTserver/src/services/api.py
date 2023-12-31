from ast import literal_eval
import requests
from exceptions.exceptions import InvalidIDException, InactiveApiException

class RequestAPI:

    def __init__(self, airID):
        self.setID(airID)
        
    def isActiveAir(self):
        try:
            r = requests.get(f"http://localhost:8000/api/isActive?id={self.getID()}")

            if(r.text == "true"):
                return True
            return False
        
        except Exception:
            raise InactiveApiException("A api está inativa, verifique o servidor ou os endpoints")
    

    def getInfoAir(self):
        try:
            r = requests.get(f"http://localhost:8000/api/search?id={self.getID()}")
            infoAir = literal_eval( r.content.decode() ) 
            return infoAir
        except Exception:
            raise InactiveApiException("A api está inativa, verifique o servidor ou os endpoints")


    def __active(self, temp=18):
        try:
            r = requests.put("http://localhost:8000/api/active?id={}&temp={}".format(self.getID(), temp))
            return r.text
        except Exception:
            raise InactiveApiException("A api está inativa, verifique o servidor ou os endpoints")
    
    def __disable(self):
        try:
            r = requests.put("http://localhost:8000/api/disable?id={}".format(self.getID()))
            return r.text
        except Exception:
            raise InactiveApiException("A api está inativa, verifique o servidor ou os endpoints")
    
    

    def apiIsActive(self):
        try:
            r = requests.get("http://localhost:8000/api/ping")

            # print(r.text)

            if(r.status_code == 200):
                return True
            return False
        
        except Exception:
            raise InactiveApiException("A api está inativa, verifique o servidor ou os endpoints")


    def getID(self):
        return self.__ID

    def setID(self, id):
        if( RequestAPI.isValidID(id) ):
            self.__ID = id
        else:
            raise InvalidIDException("O ID do arcondicionado não é valido")

    @staticmethod
    def isValidID(id):
        try:
            r = requests.get("http://localhost:8000/api/isActive?id={}".format(id))

            # print(r.text)

            if(r.status_code != 404 or r.text == "true"):
                return True
            return False
        
        except Exception:
            raise InactiveApiException("A api está inativa, verifique o servidor ou os endpoints")
