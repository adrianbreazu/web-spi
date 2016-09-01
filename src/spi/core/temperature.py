import Adafruit_DHT as dht_sensor
import logging

logger = logging.getLogger(__name__)
SENSORTYPE = 22 dht_sensor.DHT22
GPIO_PIN = 17


def get_readings():
    logger.debug("beginning of get_readings")
    temperature = 0;
    humidity = 0;

    try:
        humidity, temperature = dht_sensor.read_retry(SENSORTYPE, GPIO_PIN)

        reads = {}
        reads['temperature'] = str(temperature)
        reads['humidity'] = str(humidity)
        logger.debug("set temperature and humidity of get_readings: {0:0.1f} *C | {1:0.1f} %".format(temperature, humidity))
    except Exception as e:
        logger.error("get_readings exception {0}".format(e))
        reads['temperature'] = 0
        reads['humidity'] = 0
    finally:
        logger.debug("end of get_readings: {0:0.1f} *C | {1:0.1f} %".format(temperature, humidity))
        return reads

