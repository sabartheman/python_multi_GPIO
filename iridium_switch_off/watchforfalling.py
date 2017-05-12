import RPI.GPIO as GPIO
from time import sleep



#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)


#these pins are off limits 
#21, 20, 26, 19, 13, 6 ,5, 18
########## Constants #############
AUTOSHUTDOWN = 1
SWITCHGPIO   = 8
##################################


GPIO.setup(SWITCHGPIO, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


def switchCallback():
    global AUTOSHUTDOWN

    if AUTOSHUTDOWN == 1:
        print "Now going to shutdown"
        os.system('/sbin/shutdown -h now')
    sys.exit(0)

def main():
    global SWITCHGPIO
    global AUTOSHUTDOWN

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SWITCHGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(SWITCHGPIO, GPIO.FALLING, callback=switchCallback,bouncetime=200)




if '__name__' == '__main__':
    main()



