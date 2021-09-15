from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub() 

legs = MotorPair('C','D')

def set_speed(value):
    legs.set_default_speed(value)

def turn_right(sec):
    legs.move(sec,'seconds',steering = 90)
    wait_for_seconds(3)

set_speed(40)

loop = 0
while loop < 5:
    turn_right(3)
    loop += 1
