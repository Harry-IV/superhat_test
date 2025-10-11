from time import sleep

# sudo apt-get install rpi.gpio
import RPi.GPIO as GPIO

TOPLEFT = 17
TOPRIGHT = 11
BOTTOMLEFT = 18
BOTTOMRIGHT = 16

gpios = {"Top Left": 17, "Top Right": 11, "Bottom Left": 18, "Bottom Right": 16}

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
