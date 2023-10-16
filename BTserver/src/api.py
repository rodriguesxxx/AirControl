import requests

class RequestAPI:

    def __init__(self, airID):
        self.ID = airID


    def isActive(self):

        r = requests.get("http://localhost:8000/api/isActive?id={}".format(self.ID))

        # print(r.text)

        if(r.status_code == 200):
            return True
        return False

    def active(self, temp=18):
        r = requests.put("http://localhost:8000/api/active?id={}&temp={}".format(self.ID, temp))
        return r.text
    
    def disable(self):
        r = requests.put("http://localhost:8000/api/disable?id={}".format(self.ID))
        return r.text


    def apiIsActive():

        r = requests.get("http://localhost:8000/api/ping")

        # print(r.text)

        if(r.status_code == 200):
            return True
        return False
