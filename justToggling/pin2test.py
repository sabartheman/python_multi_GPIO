import RPi.GPIO as GPIO
import time.sleep as sleep


#pin 23 has a pull down resistor
#pin 24 has a pull up   resistor
GPIO.setmode(BCM)
GPIO.setwarning(False)

def toggle_a_single_pin_2hz():
    GPIO.output(10, HIGH)
    sleep(1)
    GPIO.output(10, LOW)
    sleep(1)

def main():
    while(True):
        toggle_a_single_pin_2hz()

if __name__ == '__main__':
    main()
