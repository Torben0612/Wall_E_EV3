#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
backmotor = Motor(Port.C)
frontmotor = Motor(Port.D)
drill = Motor(Port.B)
eyes = UltrasonicSensor(Port.S1)

# Write your program here.

# Create Thread thread and its parameters filename and volume.

running = False

def thread_function(sound, loudness):
    """Add code between running = True and running = False. This function sets loudness and plays sound."""
    global ev3, running
    running = True
    # Set speaker loudness and play sound.
    ev3.speaker.set_volume(loudness)
    ev3.speaker.play_file(sound)
    running = False

# Create Thread thread and its parameters filename and volume.
filename = './wwwaaallleee.wav'  # https://freesound.org/people/Hatayde/sounds/580283/
volume = 25
thread = threading.Thread(target=thread_function, args=(filename, volume, ))



ev3.speaker.beep()
thread.start()

while True:
    distance = eyes.distance()
    distance = int(distance)
    print(distance)
    if distance >= 101:
        backmotor.run_time(-500, 1050, wait=False)
        frontmotor.run_time(500, 1050, wait=True)
    if eyes.distance() <= 1000:
        backmotor.stop()
        frontmotor.stop()
        drill.run(500)