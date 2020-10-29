import json
import urllib3

class mirConnection:
    def __init__(self):
        self.mirurl = "http://192.168.1.8:8080"
    
    def updateURL(self, newurl):
        self.mirurl = newurl

    def getStatusText(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        status = json.loads(req.data.decode('utf-8'))
        return req, status

    def getStatus(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        status = json.loads(req.data.decode('utf-8'))
        print("Status: ", status)
        
    def getMissions(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/missions', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Missions: ", missions)
        
    #Use this method to add a mission to MiR's mission queue, give it the mission's mission_id (constants given in testCode)
    def performMission(self, missionID):
        missionBody = json.dumps({"mission_id" : missionID})
        http = urllib3.PoolManager()
        req = http.request('POST', self.mirurl + '/v2.0.0/mission_queue', 
            headers={'Content-Type': 'application/json', 'authorization': ' Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        missions = json.loads(req.data.decode('utf-8'))
        print("Req: ", req)
        print("Status: ", missions)
        if(req.status == 200):
            print("Mission Successfully Queued: ", missionID)
        else:
            print("Error while queueing mission: ", req.status)
    
    #GET status, then grab the 'distance to next target' value (in meters) and any current errors
    def getDistFromTarget(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        status = json.loads(req.data.decode('utf-8'))
        print("Status:", status)
        distance = status['distance_to_next_target']
        errors = status['errors']
        print("Distance To Target: ", distance)
        print("Errors:", errors)
        return (distance, errors)
    
    # Clears the error flag from the MiR after an error has occured. In this way, the code can 
    # keep running even after an error occurs.
    def clearError(self):
        statusBody = json.dumps({"clear_error" : True})
        http = urllib3.PoolManager()
        req = http.request('PUT', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='},
                           body=statusBody)
        status = json.loads(req.data.decode('utf-8'))
        if(req.status == 200):
            print("Error cleard.")
        else:
            print("Error while clearing error: ", req.status)
    
    # Sets the state of the MiR's mission queue to 'Ready' - It will automatically change to pause 
    # after an error occurs, so it needs to be changed back to ready after an error occurs
    def makeReady(self):
        statusBody = json.dumps({"state_id" : 3})
        http = urllib3.PoolManager()
        req = http.request('PUT', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='},
                           body=statusBody)
        status = json.loads(req.data.decode('utf-8'))
        if(req.status == 200):
            print("MiR is Ready.")
        else:
            print("Error while setting MiR state: ", req.status)
    
    # Deletes the current missions in the MiR queue
    def deleteMissions(self):
        http = urllib3.PoolManager()
        req = http.request('DELETE', self.mirurl + '/v2.0.0/mission_queue/', 
            headers={'Content-Type': 'application/json', 'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        #response = json.loads(req.data.decode('utf-8'))
        if(req.status == 200):
            print("Misisons Deleted.")
        else:
            print("Error while deleting missions: ", req.status)