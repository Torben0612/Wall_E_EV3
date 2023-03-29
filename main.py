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


# Threading: use global variable running and declare your thread code in thread_function.
running = False

def thread_function1(sound, loudness):
    """Add code between running = True and running = False. This function sets loudness and plays sound."""
    global ev3, running
    running = True
    # Set speaker loudness and play sound.
    ev3.speaker.set_volume(loudness)
    ev3.speaker.play_file(sound)
    running = False

def thread_function2(sound, loudness):
    """Add code between running = True and running = False. This function sets loudness and plays sound."""
    global ev3, running
    running = True
    # Set speaker loudness and play sound.
    ev3.speaker.set_volume(loudness)
    ev3.speaker.play_file(sound)
    running = False

# Create Thread thread and its parameters filename and volume.
file1 = './wwwaaallleee.wav'  # walle
file2 = './woah.wav
volume = 100
thread1 = threading.Thread(target=thread_function2, args=(file1, volume, ))
thread2 = threading.Thread(target=thread_function2, args=(file2, volume, ))

ev3.speaker.beep()
thread1.start()

while True:
    distance = eyes.distance()
    distance = int(distance)
    while distance >= 200:
        motor2.run_time(1000, 50, wait=False)
        motor1.run_time(1000, 50, wait=False)
    if ultrasonic.distance() <= 50:
        thread2.start()
        motor1.stop()
        motor2.stop()