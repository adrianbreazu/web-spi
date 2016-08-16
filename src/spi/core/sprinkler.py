#import RPi.GPIO as GPIO
import core.GPIO as GPIO


class Sprinkler:
    GPIO_TYPE = {
        "output": GPIO.OUT,
        "input": GPIO.IN
    }

    GPIO_STATE = {
        "high": GPIO.HIGH,
        "low": GPIO.LOW
    }

    def __init__(self):
        try:
            GPIO.setmode(GPIO.BOARD)
            self.pinout_list = []
            print("init")
        except Exception as e:
            print("__init__ exception %s" % e)

    def init_GPIO(self, pinout, gpio_type):
        try:
            if not(pinout in self.pinout_list):
                GPIO.setup(pinout, gpio_type)
                self.pinout_list.append(pinout)
            else:
                print("pin already setup")
            print("setup GPIO %s for type %s" % pinout % gpio_type)
        except Exception as e:
            print("init_GPIO exception %s" % e)

    def activate(self, pinout):
        self.change_state(pinout, self.GPIO_STATE.get("low"))

    def deactivate(self, pinout):
        self.change_state(pinout, self.GPIO_STATE.get("high"))

    def change_state(self, pinout, gpio_state):
        try:
            GPIO.output(pinout, gpio_state)
        except Exception as e:
            print("change state exception %s" % e)

    def __del__(self):
        try:
            for pin in self.pinout_list:
                self.deactivate(pin)
            GPIO.cleanup()
            print("finish clean")
        except Exception as e:
            print("__del__ exception %s" % e)
