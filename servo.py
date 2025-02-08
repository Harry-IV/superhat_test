import pigpio
from time import sleep

# connect to the 
pi = pigpio.pi()

SERVOGPIO = 13
# loop forever
while True:

    pi.set_servo_pulsewidth(SERVOGPIO, 0)    # off
    sleep(1)
    pi.set_servo_pulsewidth(SERVOGPIO, 1000) # position anti-clockwise
    sleep(1)
    pi.set_servo_pulsewidth(SERVOGPIO, 1500) # middle
    sleep(1)
    pi.set_servo_pulsewidth(SERVOGPIO, 2000) # position clockwise
    sleep(1)