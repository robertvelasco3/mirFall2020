from mirConnection import mirConnection
from motorControl import motorControl

# State Machine
# 7 States: 'IDLE', 'READY_DOCK', 'DOCK', 'UNLOAD', 'STOP', 'LOAD', 'UNDOCK'
# Output occurs at the transitions between states
class StateMachine:
    def __init__(self, mir, motor, initialState=0, begin=True):
        self.currentState = initialState
        self.mir = mir
        self.motor = motor
        self.finished = False

    def set_State(self, toState):
        self.action(self.currentState)
        self.currentState = toState

    def checkTransitions(self, command):
        pass

    def action(self, state_run):
        if state_run == 1:
            self.move()
        elif state_run == 2:
            self.dock()
        elif state_run == 3:
            self.unload()
        elif state_run == 4:
            self.stop()
        elif state_run == 5:
            self.load()
        elif state_run == 6:
            # How to go back to idle position
            self.finished = True

    def move(self):
        print('MiR100 on route to position A')
        self.mir.goToA()

    def dock(self):
        print('MiR100 is preparing to dock')
        self.mir.endMission(54)

    def unload(self):
        print('Currently unloading the MiR100')
        self.motor.moveForward(5)

    def stop(self):
        print('Currently stop unloading the MiR100')
        self.motor.stop()

    def load(self):
        print('Currently loading the MiR100')
        self.motor.moveBackward(2)

    def undock(self):
        print('Currently undocking the MiR100')

if __name__ == "__main__":
    mir = mirConnection()
    motor = motorControl()

    machine = StateMachine(mir, motor, 0)

    run = True
    while run:
        command = input()
        machine.checkTransitions(command)

        # End program
        if machine.finished:
            run = False





