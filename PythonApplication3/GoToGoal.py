print('Hello World')
import math
import Receiver as receiver
import Sender as sendToActuator
goal_x_cord = 0
goal_y_cord = 0
goal_angle = 0.0
bot_x = 0
bot_y = 0
bot_headDir = 0.0
Kp = 0.1

def setGoal(x_cord,y_cord,angle):
    goal_x_cord = x_cord
    goal_y_cord = y_cord
    goal_angle = angle

def setPGain(gain):
    Kp = gain

def getCurrentState():
    print 'bot_x: ',bot_x
    print 'bot_y: ',bot_y
    print 'bot_headng: ',bot_headDir

def CheckIfGoal():
    if(bot_x == goal_x_cord and bot_y == goal_y_cord):
        return True
    else:
        return False

def GoToGoal():
    while(True):
        angularSpeed = Kp * math.atan2(goal_angle - bot_headDir)
        sendToActuator.angularSpeed()
        receiver.updateBotState() 
# The Receiver and Sender are two nodes running concurrently on the ROS platform and the communication these are mainly 
#responsible to communicate the state of the system to the nodes requiring it. This can be done by exposing the information required
#in terms of Topics or as Services as per the requirements of the nodes in question. The "sendToActuator......receiver.updateBotState()" 
#only symbolizes that the actuation must be sent to the node requiring it through some communcation medium in this case another node
#handling all the communication and receive feedback also through some communication channel.''' 
        
        getCurrentState()
        if(checkIfGoal()):
            break


setGoal(100,200,30)
GoToGoal()