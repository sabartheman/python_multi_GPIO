import RPi.GPIO as GPIO
import time.sleep as sleep


#pin 23 has a pull down resistor
#pin 24 has a pull up   resistor
GPIO.setmode(BCM)
GPIO.setwarnings(False)

def toggle_a_single_pin_1hz():
    GPIO.output(27, HIGH)
    sleep(.5)
    GPIO.output(27, LOW)
    sleep(.5)

def main():
    while(True):
        toggle_a_single_pin_1hz()

if __name__ == '__main__':
    main()
