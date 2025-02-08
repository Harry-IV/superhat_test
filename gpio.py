from time import sleep

# pip3 install keyboard
import keyboard

# sudo apt-get install rpi.gpio
import RPi.GPIO as GPIO

import sys

TOPLEFT = 15
TOPRIGHT = 6
BOTTOMLEFT = 14
BOTTOMRIGHT = 16

gpios = {"Top Left": 15, "Top Right": 6, "Bottom Left": 14, "Bottom Right": 16}

GPIO.setmode(GPIO.BCM)

for gpio in gpios.values():
    GPIO.setup(gpio, GPIO.OUT)

while True:
    for gpio_loc in gpios:
        GPIO.output(gpios[gpio_loc], GPIO.HIGH)
        print(gpio_loc)
        sleep(2)
        GPIO.output(gpios[gpio_loc], GPIO.LOW)
        sleep(1)
