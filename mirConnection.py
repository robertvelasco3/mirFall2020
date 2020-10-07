import json
import urllib3

class mirConnection:
    def getStatus(self):
        http = urllib3.PoolManager()
        req = http.request('GET', 'http://192.168.1.8:8080/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
        
    def getMissions(self):
        http = urllib3.PoolManager()
        req = http.request('GET', 'http://192.168.1.8:8080/v2.0.0/mission_queue', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
        
    #Use this method to add a mission to MiR's mission queue, give it the mission's mission_id (constants given in testCode)
    def performMission(self, missionID):
        missionBody = json.dumps({"mission_id" : missionID})
        http = urllib3.PoolManager()
        req = http.request('POST', 'http://192.168.1.8:8080/v2.0.0/mission_queue', 
            headers={'Content-Type': 'application/json', 'authorization': ' Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
    
    def deleteMissions(self):
        http = urllib3.PoolManager()
        req = http.request('DELETE', 'http://192.168.1.8:8080/v2.0.0/mission_queue/', 
            headers={'Content-Type': 'application/json', 'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        print(req)

    #Still need to test
    def endMission(self, missionID):
        http = urllib3.PoolManager()
        req = http.request('DELETE', 'http://192.168.1.8:8080/v2.0.0/mission_queue/' + missionID, 
            headers={'Content-Type': 'application/json', 'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
