import sys
import time
import signal
import RPi.GPIO as GPIO

IN1 = 13
IN2 = 11
IN3 = 7
IN4 = 15


def signal_handler(sig, freme):
    GPIO.cleanup()
    sys.exit()
    
def button_BOTH_pressed_callback(channel):
    print('button_BOTH_pressed_callback channel:',channel)

def button_FALLING_pressed_callback(channel):
    print('button_FALLING_pressed_callback channel:',channel)
    
def button_RISING_pressed_callback(channel):
    print('button_RISING_pressed_callback channel:',channel)
    
if __name__ == '__main__':
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(IN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(IN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	GPIO.add_event_detect(IN1, GPIO.BOTH, callback=button_BOTH_pressed_callback, bouncetime=100)
	GPIO.add_event_detect(IN2, GPIO.FALLING, callback=button_FALLING_pressed_callback, bouncetime=100)
	GPIO.add_event_detect(IN3, GPIO.RISING, callback=button_RISING_pressed_callback, bouncetime=100)

	signal.signal(signal.SIGINT, signal_handler)
	signal.pause()
