#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

# Declaring motors
motorZ = Motor(Port.C)
motorX = Motor(Port.B)
hand = Motor(Port.A)

# Declaring sensors
light_sensor = ColorSensor(Port.S3)
touch_sensor = TouchSensor(Port.S1)

# This bool is for checking the hand it it closed or not
# Here the bool is False. Before running the program on the EV3 robot
# place make sure that the hand's claws are opened, else the motor
# will stall and the program will not continue.
# If the hand gets stuck, stop the program to release the motor and
# position the claw correctly
handClosed = False

while(True):
    pressed = ev3.buttons.pressed()
    ev3.light.on(Color.GREEN)

    # Easter egg
    # When the touch sensor is pressed it draws a image on the screen
    # The image must be a .png file and have 128x128 pixels resolution
    # to fit well on the EV3 screen
    if touch_sensor.pressed():
        ev3.screen.load_image("./rickroll_4k")
        pass

    # Main hand
    if Button.CENTER in pressed:
        if handClosed == False:
            ev3.light.on(Color.ORANGE)
            hand.run_target(400, -50, then=Stop.HOLD)
            if hand.control.stalled():
                hand.hold()
                pass
            handClosed = True
            pass
        elif handClosed == True:
            ev3.light.on(Color.ORANGE)
            hand.run_target(400, 50, then=Stop.HOLD)
            if hand.control.stalled():
                hand.hold()
                pass
            handClosed = False
            pass
        pass

    # Hand Z rotation
    # This if statement is used to stop the hand so it is not rotating infinitely
    if not Button.LEFT in pressed and not Button.RIGHT in pressed:
        motorZ.hold()
        pass

    if Button.LEFT in pressed:
        ev3.light.on(Color.ORANGE)
        motorZ.run(-240)
        pass

    if Button.RIGHT in pressed and not touch_sensor.pressed():
        ev3.light.on(Color.ORANGE)
        motorZ.run(240)
        pass
    elif Button.RIGHT in pressed and touch_sensor.pressed():
        ev3.speaker.beep(500, 100)
        ev3.light.on(Color.RED)
        motorZ.stop()
        pass

    # Hand X rotation
    # Same thing as for Z hand rotation
    if not Button.UP in pressed and not Button.DOWN in pressed:
        motorX.hold()
        pass

    if Button.UP in pressed and not light_sensor.color() == Color.WHITE:
        ev3.light.on(Color.ORANGE)
        motorX.run(-240)
        pass
    
    if Button.DOWN in pressed:
        ev3.light.on(Color.ORANGE)
        motorX.run(240)
        pass

ev3.light.on(Color.RED)

