#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
# buttons = Button()
motorZ = Motor(Port.C)
motorX = Motor(Port.B)
hand = Motor(Port.A)

light_sensor = ColorSensor(Port.S3)
sensor = TouchSensor(Port.S1)

handClosed = False

while(True):

    if sensor.pressed():
        # ev3.speaker.play_file("./rickroll.mp3")
        ev3.screen.load_image("./rickroll_4k")
        # wait(10000)
        pass

    pressed = ev3.buttons.pressed()
    ev3.light.on(Color.GREEN)

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
    if not Button.LEFT in pressed and not Button.RIGHT in pressed:
        motorZ.hold()
        pass

    if Button.LEFT in pressed:
        ev3.light.on(Color.ORANGE)
        motorZ.run(-240)
        pass

    if Button.RIGHT in pressed and not sensor.pressed():
        ev3.light.on(Color.ORANGE)
        motorZ.run(240)
        pass
    elif Button.RIGHT in pressed and sensor.pressed():
        ev3.speaker.beep(500, 100)
        ev3.light.on(Color.RED)
        motorZ.stop()
        pass

    # Hand X rotation
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

