import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(18,gpio.OUT)

s1 = gpio.PWM(18,50)
s1.start(0)

try:
    while True:
        angle = int(input("Enter the value of angle: ")) 
        duty = 2+(angle/18)
        s1.ChangeDutyCycle(duty)
        time.sleep(1)
        s1.ChangeDutyCycle(0)
        time.sleep(1)
except:
    s1.stop()
    gpio.cleanup()