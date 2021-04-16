import sys
import time
import signal
import RPi.GPIO as GPIO
from datetime import datetime
IN1 = 7
IN2 = 11
IN3 = 13
IN4 = 15

def getDate():
       return datetime.now().strftime('%d-%m-%Y %H:%M:%S:%f')


def signal_handler(sig, freme):
    GPIO.cleanup()
    print('External interrupting application stopped')
    sys.exit()
    
def button_BOTH_pressed_callback(channel):
    if GPIO.input(IN1):
        print('button_BOTH_pressed_callback channel:' + str(channel) + ' HIGH\tdate:' + getDate())
    else:
        print('button_BOTH_pressed_callback channel:' + str(channel) + ' LOW\tdate:' + getDate())

def button_FALLING_pressed_callback(channel):
    print('button_FALLING_pressed_callback channel:' + str(channel) + ' \tdate:' + getDate())
    
def button_RISING_pressed_callback(channel):
    print('button_RISING_pressed_callback channel:' + str(channel) + ' \tdate:' + getDate())
    
if __name__ == '__main__':
    print('Raspberry pi 4 external interrupt application')
    print('External interrupting application started')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(IN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(IN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(IN1, GPIO.BOTH, callback=button_BOTH_pressed_callback, bouncetime=100)
    GPIO.add_event_detect(IN2, GPIO.FALLING, callback=button_FALLING_pressed_callback, bouncetime=100)
    GPIO.add_event_detect(IN3, GPIO.RISING, callback=button_RISING_pressed_callback, bouncetime=100)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
