import requests

class MicroController:
    pass

class RequestAPI:

    def __init__(self, airID):
        self.ID = airID


    def isActive(self):

        r = requests.get("http://localhost:8000/api/isActive?id={}".format(self.ID))

        # print(r.text)

        if(r.status_code == 200):
            return True
        return False

    def active(self):
        r = requests.put("http://localhost:8000/api/active", data={'id':self.ID})
        print(r.text)

    def disable(self):
        pass


    def apiIsActive():

        r = requests.get("http://localhost:8000/api/ping")

        # print(r.text)

        if(r.status_code == 200):
            return True
        return False


req = RequestAPI("INFO22")

print(req.isActive())
# print(req.active())