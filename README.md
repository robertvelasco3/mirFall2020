# mirFall2020 Files:
### RPi3b+Info.txt
Login and remote desktop access information for our Raspberry Pi 3b+
### mirConnection.py
This file has the class mirConnection, which uses http requests to send and receive information from the MiR100.
### motorControl.py
This file has the class motorControl, which instantiates the motor connection with the Rpis GPIO pins and contains methods that tell the motors to move forward, backward, and stop
### motorControlSampleCode.py
This is the sample code from the project that integrated the motors with the RPi 3
### testCode.py
This code tests all systems indivudally and tests the integration of all of the systems
### angularCode/
This is the enitre website code. To run the website on your computer locally, follow these steps:  
Install Node.js (npm) first.  
Then install angular using:  
`npm install -g @angular/cli`  
Then once inside the angularCode folder in a terminal, run:  
`ng serve`  
You should be able to open any browser and go to 'http://localhost:4200'  
If there are build errors, try running `npm update` and then `ng serve` again.
