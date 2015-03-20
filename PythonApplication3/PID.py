import math
def PIDAngle(goalAngle,currentAngle):
    '''Takes in the current heading direction compares it with the goal direction and outputs the angular velocity 'omega' 
    (based on the PID controller)required to reach the desired goal direction.'''
    #desiredAngle = math.atan2((goalState.y - currentState.y), (goalState.x - currentState.x))
    error = goalAngle - currentAngle
    error = math.atan2(math.sin(error), math.cos(error))
    omega = Kp * error
    return omega

def PIDSpeed(ReferenceSpeed,currentSpeed,choice = 1):
    '''Takes in the current speed compares it with the reference speed and outputs the acceleration (based on the PID comtroller)
    required to achieve the speed.''' 
    return acceleration