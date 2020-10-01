import json
import urllib3

class mirConnection:
    def getStatus(self):
        http = urllib3.PoolManager()
        req = http.request('GET', 'http://mir.com:8080/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
        
    def getMissions(self):
        http = urllib3.PoolManager()
        req = http.request('GET', 'http://mir.com:8080/v2.0.0/missions', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
        
    #Use this method to add a mission to MiR's mission queue, give it the mission's mission_id (constants given in testCode)
    def performMission(self, missionID):
        missionBody = json.dumps({"mission_id" : missionID})
        http = urllib3.PoolManager()
        req = http.request('POST', 'http://mir.com:8080/v2.0.0/mission_queue', 
            headers={'Content-Type': 'application/json', 'authorization': ' Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)

    #Still need to test
    def endMission(missionID):
        http = urllib3.PoolManager()
        req = http.request('DELETE', 'http://mir.com:8080/v2.0.0/mission_queue/' + missionID, 
            headers={'Content-Type': 'application/json', 'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        print(req)
