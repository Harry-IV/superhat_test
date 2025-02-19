import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.LOW)

GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.LOW)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(6, GPIO.LOW)

sleep(3)