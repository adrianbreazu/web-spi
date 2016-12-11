#import RPi.GPIO as GPIO
import core.GPIO as GPIO
import logging

logger = logging.getLogger(__name__)


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
        logger.debug("beginning of __init__")
        try:
            GPIO.setmode(GPIO.BCM)
            self.pinout_list = []
        except Exception as e:
            logger.error("__init__ exception {0}".format(e))
        finally:
            logger.debug("end of __init__")

    def init_GPIO(self, pinout, gpio_type):
        logger.debug("beginning of init_GPIO, for pin: {0} and gpio_type: {1}".format(pinout, gpio_type))
        try:
            if not(pinout in self.pinout_list):
                GPIO.setup(pinout, gpio_type)
                self.pinout_list.append(pinout)
                logger.debug("set pin {0}".format(int(pinout)))
            else:
                logger.debug("pin: {0} already exists".format(int(pinout)))
        except Exception as e:
            logger.error("init_GPIO exception {0}".format(e))
        finally:
            logger.debug("end of init_GPIO, for pin: {0} and gpio_type: {1}".format(pinout, gpio_type))

    def get_gpio_input_value(self, pinout):
        logger.debug("beginning of get_gpio_input_value, for pin: {0}".format(pinout))
        try:
            return GPIO.input(pinout)
        except Exception as e:
            logger.error("get_gpio_input_value exception {0}".format(e))
        finally:
            logger.debug("end get_gpio_input_value for pin {0}".format(pinout))

    def activate(self, pinout):
        self.change_state(int(pinout), self.GPIO_STATE.get("high"))

    def deactivate(self, pinout):
        self.change_state(int(pinout), self.GPIO_STATE.get("low"))

    def change_state(self, pinout, gpio_state):
        logger.debug("beginning of change_state for pin {0} state to {1}".format(pinout, gpio_state))
        try:
            GPIO.output(int(pinout), gpio_state)
        except Exception as e:
            logger.error("change state exception {0}".format(e))
        finally:
            logger.debug("end of change_state for pin {0} state to {1}".format(pinout, gpio_state))

    def deactivate_all(self):
        print("beginning cleanup, pinout_list array = {0}".format(self.pinout_list))
        if len(self.pinout_list):
            for pin in self.pinout_list:
                print("deactivate pin: {0}".format(pin))
                self.deactivate(pinout=int(pin))

    def __del__(self):
        GPIO.cleanup
        print("finish RPI cleanup")
