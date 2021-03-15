import curses
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

##SERVO PINS
GPIO.setup(22,GPIO.OUT)
# GPIO.setup(22,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
# GPIO.setup(22,GPIO.OUT)

# servo1 = GPIO.PWM(22,50)
servo2 = GPIO.PWM(18,50)
servo3 = GPIO.PWM(16,50)
servo4 = GPIO.PWM(22,50)
# servo5 = GPIO.PWM(22,50)

# servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)
# servo5.start(0)

time.sleep(2)

# duty=0



screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('Q'):
            break
        if char == ord('S'):
            os.system('sudo shutdown now')
        elif char== curses.KEY_UP:
            GPIO.output(7,True)
            GPIO.output(11,False)
            GPIO.output(15,True)
            GPIO.output(13,False)         
        elif char== curses.KEY_DOWN:
            GPIO.output(11,True)
            GPIO.output(7,False)
            GPIO.output(13,True)
            GPIO.output(15,False)
        elif char== curses.KEY_RIGHT:
            GPIO.output(7,False)
            GPIO.output(11,True)
            GPIO.output(15,True)
            GPIO.output(13,False)
        elif char== curses.KEY_LEFT:
            GPIO.output(7,True)
            GPIO.output(11,False)
            GPIO.output(13,True)
            GPIO.output(15,False)
        elif char== 10:
            GPIO.output(11,False)
            GPIO.output(7,False)
            GPIO.output(13,False)
            GPIO.output(15,False)
           
           
##servo control
        elif char == ord('q'):
            servo1.ChangeDutyCycle(0)
            time.sleep(0.5)
            servo1.ChangeDutyCycle(2)
            time.sleep(0.5)
            servo1.ChangeDutyCycle(5)
            time.sleep(0.5)
            servo1.ChangeDutyCycle(7)
            time.sleep(0.5)
            
#         elif char == ord('e'):
#             servo1.ChangeDutyCycle(7)
#             time.sleep(0.5)
#             servo1.ChangeDutyCycle(5)
#             time.sleep(0.5)
#             servo1.ChangeDutyCycle(2)
#             time.sleep(0.5)
#             servo1.ChangeDutyCycle(0)
#         
#         elif char == ord('w'):
#             servo1.ChangeDutyCycle(0)
#         
        elif char == ord('a'):
            servo2.ChangeDutyCycle(0)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(2)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(5)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(7)
            time.sleep(0.5)
            
        elif char == ord('d'):
            servo2.ChangeDutyCycle(7)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(5)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(2)
            time.sleep(0.5)
            servo2.ChangeDutyCycle(0)
        
        elif char == ord('s'):
             servo2.ChangeDutyCycle(0)
        
        elif char == ord('z'):
              servo3.ChangeDutyCycle(2)
#             time.sleep(0.5)
#             servo3.ChangeDutyCycle(3)
#             time.sleep(0.5)
#             servo3.ChangeDutyCycle(5)
            
            
        elif char == ord('c'):
              servo3.ChangeDutyCycle(12)
#             time.sleep(0.5)
#             servo3.ChangeDutyCycle(12)
#             time.sleep(0.5)
#             servo3.ChangeDutyCycle(10)
            
            
        elif char == ord('x'):
              servo3.ChangeDutyCycle(0)
        
        elif char == ord('r'):
              servo4.ChangeDutyCycle(5)
#             time.sleep(0.5)
#             servo4.ChangeDutyCycle(3)
#             time.sleep(0.5)
#             servo4.ChangeDutyCycle(5)
            
            
        elif char == ord('y'):
              servo4.ChangeDutyCycle(12)
#             time.sleep(0.5)
#             servo4.ChangeDutyCycle(12)
#             time.sleep(0.5)
#             servo4.ChangeDutyCycle(10)
            
            
        elif char == ord('t'):
              servo4.ChangeDutyCycle(0)
        
#         elif char == ord('f'):
#             servo5.ChangeDutyCycle(0)
#             time.sleep(0.5)
#             servo5.ChangeDutyCycle(2)
#             time.sleep(0.5)
#             servo5.ChangeDutyCycle(5)
#             time.sleep(0.5)
#             servo5.ChangeDutyCycle(7)
#             time.sleep(0.5)
#             
#         elif char == ord('h'):
#             servo5.ChangeDutyCycle(7)
#             time.sleep(0.5)
#             servo5.ChangeDutyCycle(5)
#             time.sleep(0.5)
#             servo5.ChangeDutyCycle(2)
#             time.sleep(0.5)
#             servo5.ChangeDutyCycle(0)
#             
#         elif char == ord('g'):
#             servo5.ChangeDutyCycle(0)
finally:
    curses.nocbreak();screen.keypad(0);curses.echo()
    curses.endwin()
      #servo1.stop()
    servo2.stop()
    servo3.stop()
    servo4.stop()
#     servo5.stop()
    GPIO.cleanup()
        
            
       
            

