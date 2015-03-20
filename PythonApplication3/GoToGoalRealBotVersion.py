print('Hello World')
import math
import PID as Pid
import Receiver as receiver
import Sender as sendToActuator

class GoToGoalBehaviour:
    def __init__(goalState):
# goalState is a state variable comprising of <x,y,velocity,heading direction> as its properties it is an instance of the state class

        self.goalState = goalStat
        self.currentState = None
        startBehaviour()
        abort = False

    

# Initialize the GoToGoal behavior class.
# Get the goal state of the boat.
# Do following untill abort or goal achieved.
# Get the current state of the bot.
# Calculate errors.
# Compute actuations.
# Send actuations. 
    
    def goal():
        abort = receiver.doAbort()
        if(abort):
            return abort
        else:
            if(currentState == goalState):
                return True
            else:
                return False


    def startBehaviour():
        while(not goal()):
            currentState = receiver.getCurrentState()
# The currentState is an instance of class State which stores the current state of the bot. Note that the function 
# getCurrentState will be a part of the interface module which is used to communicate between the program that stores 
# the global updations of the program.
# Both omega and acceleration will be calculated on the basis of current state of the bot.
            omega = Pid.PIDAngle()
            acceleration = Pid.PIDSpeed()
            sendToActuator.sendActuation(omega)
            sendToActuator.sendActuation(acceleration)
