import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)

print("hello")
GPIO.output(11, GPIO.HIGH)
sleep(2)
GPIO.output(11, GPIO.LOW)