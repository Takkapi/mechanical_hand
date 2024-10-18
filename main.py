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
hand = Motor(Port.A)
handClosed = False

# Set hand to the default position
# if hand.angle() < 55:
#     hand.run_target(500, 50, then=Stop.HOLD)
# else: pass



sensor = TouchSensor(Port.S1)

while(True):
    pressed = ev3.buttons.pressed()
    ev3.light.on(Color.ORANGE)
    # motorZ.stop()

    # Main hand
    if(Button.CENTER in pressed):
        if handClosed == False:
            ev3.light.on(Color.GREEN)
            hand.run_target(400, -50, then=Stop.HOLD)
            if hand.control.stalled():
                pass
            handClosed = True
            print(hand.angle())
            pass
            # break
        elif handClosed == True:
            ev3.light.on(Color.GREEN)
            hand.run_target(400, 50, then=Stop.HOLD)
            if hand.control.stalled():
                pass
            handClosed = False
            print(hand.angle())
            pass
            # break

    if(Button.LEFT in pressed):
        ev3.light.on(Color.GREEN)
        motorZ.run(-120)
        # motorZ.dc(20)
        pass
    elif True:
        pass
    else: motorZ.stop() pass


    if(Button.RIGHT in pressed):
        ev3.light.on(Color.GREEN)
        motorZ.run(120)
        # motorZ.dc(-20)
        pass
    elif Button.RIGHT in pressed and sensor.pressed():
        ev3.speaker.beep(500, 100)
        ev3.light.on(Color.RED)
        pass
    else: motorZ.stop() pass

    # if Button.RIGHT in pressed and sensor.pressed():
    #     ev3.speaker.beep(500, 100)
    #     ev3.light.on(Color.RED)
    #     pass


    # if Button.LEFT in pressed:
        # elif Button.RIGHT in pressed:


# motorZ.run(-90)

# wait(5000)

ev3.light.on(Color.RED)
# motorZ.stop()


# if ev3.button.pressed(button.left):
#     pass

