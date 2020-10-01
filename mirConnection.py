import json
import urllib3

GoToA = "cfbc2ff2-0363-11eb-99a6-000129922c9e"
GoToStart = "94601816-0363-11eb-99a6-000129922c9e"

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

    def goToA(self):
        #GoToA mission id: 74
        missionID = "54"
        missionBody = json.dumps({"mission_id" : GoToA})

        http = urllib3.PoolManager()
        req = http.request('POST', 'http://mir.com:8080/v2.0.0/mission_queue', 
            headers={'Content-Type': 'application/json', 'authorization': ' Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
    
    def goToStart(self):
        #GoToA mission id: 74
        missionID = "54"
        missionBody = json.dumps({"mission_id" : GoToStart})

        http = urllib3.PoolManager()
        req = http.request('POST', 'http://mir.com:8080/v2.0.0/mission_queue', 
            headers={'Content-Type': 'application/json', 'authorization': ' Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
    
    def getMission():
        http = urllib3.PoolManager()
        req = http.request('GET', 'http://mir.com:8080/v2.0.0/mission_queue', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
    
    def endMission(missionID):
        http = urllib3.PoolManager()
        req = http.request('DELETE', 'http://mir.com:8080/v2.0.0/mission_queue/' + missionID, 
            headers={'Content-Type': 'application/json', 'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        print(req)
    
    def httpReq(self, method, url):
        http = urllib3.PoolManager()
        req = http.request(method, url, headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        return req
    
    def test(self):
        r = self.httpReq('GET', 'https://google.com')
        #j = json.loads(r.data.decode('utf-8'))
        print(r.data)
        print(r.decode('utf-8'))

