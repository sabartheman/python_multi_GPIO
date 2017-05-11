import RPi.GPIO as GPIO
from time import sleep


#pin 23 has a pull down resistor
#pin 24 has a pull up   resistor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)

def toggle_a_single_pin_1hz():
    GPIO.output(10, GPIO.HIGH)
    sleep(.5)
    GPIO.output(10, GPIO.LOW)
    sleep(.5)

def main():
    while(True):
        toggle_a_single_pin_1hz()

if __name__ == '__main__':
    main()
