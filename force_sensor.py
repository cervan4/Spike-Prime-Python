from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub() 

legs = MotorPair('C','D')
force = ForceSensor('E')

while True:
    value = force.is_pressed()
    if value == True:
        legs.move(3, 'seconds')

    if force.is_pressed() == True:
        legs.move(3,'seconds')

    force.wait_until_pressed()
    legs.move(3,'seconds')

    force.wait_until_released()
    legs.move(3,'seconds')
