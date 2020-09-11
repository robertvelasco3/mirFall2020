import json
import urllib3

class mirConnection:
    def getMissions():
        http = urllib3.PoolManager()
        req = http.request('GET', 'http://mir.com:8080/v2.0.0/mission_queue', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))

    def goToA():
        #GoToA mission id: 54
        missionID = "54"
        missionBody = json.dumps({"mission_id" : missionID})

        http = urllib3.PoolManager()
        req = http.request('POST', 'http://mir.com:8080/v2.0.0/mission_queue', 
            headers={'Content-Type': 'application/json', 'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
