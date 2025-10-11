import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep
import csv

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

ads = ADS.ADS1015(i2c)

while True:
    chan = AnalogIn(ads, ADS.P0)
    current = (chan.voltage / (0.0033 * 200))
    print(current)
    sleep(0.1)


# GPIO.output(gpios["Bottom Right"], GPIO.HIGH)
# f = open("current_sense/voltage_data/R1000_C2.2.csv", 'w')    
# writer = csv.writer(f)
# writer.writerow(["Counter","Voltage"])

# def write_data():
#     chan = AnalogIn(ads, ADS.P0)
#     print(chan.voltage)
    # writer.writerow([i, int(1000*chan.voltage)/1000])  

# # switching 
# for c in range(200):    
#     GPIO.output(gpios["Bottom Right"], GPIO.HIGH)
#     for i in range(10):
#         write_data()
#         sleep(0.001)
#     GPIO.output(gpios["Bottom Right"], GPIO.LOW)
#     for i in range(10):
#         write_data()
#         sleep(0.001)

# # constant 
# GPIO.output(gpios["Bottom Right"], GPIO.HIGH)
# for i in range(100):
#     write_data()
#     sleep(0.01)
# GPIO.output(gpios["Bottom Right"], GPIO.LOW)


# f.close()
    
# while True:
#     GPIO.output(gpios["Bottom Right"], GPIO.HIGH)
#     for i in range(100):
#         chan = AnalogIn(ads, ADS.P0)
#         # print(chan.value, chan.voltage)
#         current = (chan.voltage / (0.0033 * 200)) 
#         print(chan.voltage)
#         sleep(0.01)
#     GPIO.output(gpios["Bottom Right"], GPIO.LOW)
#     for i in range(100):
#         chan = AnalogIn(ads, ADS.P0)
#         # print(chan.value, chan.voltage)
#         # current = (chan.voltage / (0.0033 * 200)) 
#         print(chan.voltage)
#         sleep(0.01)
    
    
