import time
import RPi.GPIO as GPIO
import core.send_email as email


def init ():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)


def activate(channel):
    GPIO.output(channel, GPIO.LOW)


def deactivate(channel):
    GPIO.output(channel, GPIO.HIGH)


def scheduler():
    try:
        # make sure all relays are turn off
        deactivate(12)
        deactivate(16)
        deactivate(18)
        deactivate(22)

        # sprinkler 1
        print("Activate back flower sprinkler for 5 minutes")
        activate(12)
        time.sleep(300)
        deactivate(12)

        # sprinkler 2
        print("Activate back sprinklers for 20 minutes")
        activate(16)
        time.sleep(1200)
        deactivate(16)

        # sprinkler 3
        print("Activate side sprinkler for 10 minutes")
        activate(18)
        time.sleep(600)
        deactivate(18)

        #sprinkler 4
        print("Activate from flowers sprinkler for 5 minutes")
        activate(22)
        time.sleep(300)
        deactivate(22)

        #cleanup
        print("deactivate 12")
        deactivate(12)
        print("deactivate 16")
        deactivate(16)
        print("deactivate 18")
        deactivate(18)
        print("deactivate 22")
        deactivate(22)
        print("Cleanup")
        GPIO.cleanup()
        print("Exit")

        email.send_email_with_subject(recipient='breazuadrian@gmail.com', subject='Sprinklers job finished',
                                      body="Sprinklers 1,2,3 and 4 finished their job successfully")
    except KeyboardInterrupt:
        print("deactivate 12")
        deactivate(12)
        print("deactivate 16")
        deactivate(16)
        print("deactivate 18")
        deactivate(18)
        print("deactivate 22")
        deactivate(22)
        print("Cleanup")
        GPIO.cleanup()
        print("Exit")
        email.send_email_with_subject(recipient='breazuadrian@gmail.com', subject='Sprinklers job failed',
                                      body="Sprinklers 1,2,3 and 4 did not start")
