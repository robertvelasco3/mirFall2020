import json
import urllib3

class mirConnection:
    #Constructor
    #Sets the url we are hitting (mir url)
    def __init__(self):
        self.mirurl = "http://192.168.1.8:8080"
    
    #Inputs:  newUrl - new url to use for the mir
    #Outputs: None
    #Description: updates the url we are hitting
    def updateURL(self, newurl):
        self.mirurl = newurl

    #Inputs:  None
    #Outputs: req - a raw data object that is returned from the HTTP request; status - a JSON document of relevant live values
    #Description: Gets and returns mir status and HTTP response object
    def getStatusText(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        status = json.loads(req.data.decode('utf-8'))
        return req, status

    #Inputs:  None
    #Outputs: status - a JSON document of relevant live values
    #Description: Gets and returns mir status
    def getStatus(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        status = json.loads(req.data.decode('utf-8'))
        print("Status: ", status)
        
    #Not used
    #returns the mission ids of all created missions
    def getMissions(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/missions', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        missions = json.loads(req.data.decode('utf-8'))
        print("Missions: ", missions)
        
    #Inputs:  missionID - the ID of the mission we want to start (ids of all the missions are in mirControl.py)
    #Outputs: None
    #Description: Use this method to add a mission to MiR's mission queue. Prints error message if not successful.
    def performMission(self, missionID):
        missionBody = json.dumps({"mission_id" : missionID})
        http = urllib3.PoolManager()
        req = http.request('POST', self.mirurl + '/v2.0.0/mission_queue', 
            headers={'Content-Type': 'application/json', 'authorization': ' Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}, 
            body=missionBody)
        missions = json.loads(req.data.decode('utf-8'))
        #print("Req: ", req)
        print("Status: ", missions)
        if(req.status == 200):
            print("Mission Successfully Queued: ", missionID)
        else:
            print("Error while queueing mission: ", req.status)
    
    #Inputs:  None
    #Outputs: distance - distance to the target location; errors - any errors that have occured in the mission (the only
    #         one that should pop up is if something is blocking the target destination)
    #Description: Gets the MiR status (which is a document of relevant values), then grabs the 'distance to next target'
    #             value (in meters) and any current errors from the status document
    def getDistFromTarget(self):
        http = urllib3.PoolManager()
        req = http.request('GET', self.mirurl + '/v2.0.0/status', headers={'Content-Type': 'application/json',
                'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        status = json.loads(req.data.decode('utf-8'))
        #print("Status:", status)
        errors = status['errors']
        if(errors):
            return (0, errors)
        distance = status['distance_to_next_target']
        print("Distance To Target: ", distance)
        print("Errors:", errors)
        return (distance, errors)
    
    #Inputs:  None
    #Outputs: None
    #Description: Clears the error flag from the MiR after an error has occured. In this way, the code can 
    #             keep running even after an error occurs.  Prints error message if not successful.
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
    
    #Inputs:  None
    #Outputs: None
    #Description: Sets the state of the MiR's mission queue to 'Ready' - It will automatically change to pause 
    #             after an error occurs, so it needs to be changed back to ready after an error occurs. Prints
    #             error message if not successful.
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
    
    #Inputs:  None
    #Outputs: None
    #Description: Deletes all current missions in the MiR queue.  Prints error message if not successful.
    def deleteMissions(self):
        http = urllib3.PoolManager()
        req = http.request('DELETE', self.mirurl + '/v2.0.0/mission_queue/', 
            headers={'Content-Type': 'application/json', 'authorization': 'Basic ZGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='})
        #response = json.loads(req.data.decode('utf-8'))
        if(req.status == 200):
            print("Misisons Deleted.")
        else:
            print("Error while deleting missions: ", req.status)