import curses
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
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
finally:
    curses.nocbreak();screen.keypad(0);curses.echo()
    curses.endwin()
    GPIO.cleanup()
        
            
       
            
