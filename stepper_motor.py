from time import sleep
# sudo apt-get install rpi.gpio
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
revolutions = 2
speed = 1
delay = .0026 / speed

for i in range(2):
    GPIO.output(DIR, CW)
    print("Clockwise")
    for x in range(step_count * revolutions):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

    sleep(0.5)

    GPIO.output(DIR, CCW)
    print("Counter-clockwise")
    for x in range(step_count * revolutions):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

    sleep(0.5)

GPIO.cleanup()

# ---------------------------------------------------
# # control stepper motor with keyboard 

# # pip install sshkeyboard
# from sshkeyboard import listen_keyboard

# import threading

# import sys

# DIR = 20   # Direction GPIO Pin
# STEP = 21  # Step GPIO Pin
# CW = 1     # Clockwise Rotation
# CCW = 0    # Counterclockwise Rotation

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR, GPIO.OUT)
# GPIO.setup(STEP, GPIO.OUT)
# GPIO.output(DIR, CW)

# speed = 4
# delay = .0026 / speed

# def rotate_cw():
#     global moving_cw
#     while moving_cw:
#         GPIO.output(DIR, CW)
#         GPIO.output(STEP, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP, GPIO.LOW)
#         sleep(delay)
    
# def rotate_ccw():  
#     global moving_ccw 
#     while moving_ccw:
#         GPIO.output(DIR, CCW)
#         GPIO.output(STEP, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(STEP, GPIO.LOW)
#         sleep(delay)       

# def press(key):
#     global moving_cw
#     global moving_ccw
#     if key == 'left':
#         moving_ccw = True
#         threading.Thread(target=rotate_ccw).start()  
#     elif key == 'right':
#         moving_cw = True
#         threading.Thread(target=rotate_cw).start() 
#     elif key == 'esc':
#         GPIO.cleanup()
#         sys.exit()

# def release(key):
#     global moving_ccw
#     global moving_cw

#     if key == 'left':
#         moving_ccw = False
#     elif key == 'right':
#         moving_cw = False

# listen_keyboard(
#     on_press=press,
#     on_release=release
# )

