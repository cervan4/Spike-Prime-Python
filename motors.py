from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub() 


legs = MotorPair('C','D')

legs.move(3,'seconds')

wait_for_seconds(4)

legs.move(180,'degrees')
legs.move(3,'seconds',steering = 90)
