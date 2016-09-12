import core.Adafruit_Python_DHT.Adafruit_DHT as dht_sensor
import sqlite3 as sqlite
import datetime as datetime

SENSORTYPE = dht_sensor.DHT22
GPIO_PIN = 17
DB = '/var/www/web-spi/src/spi/db.sqlite3'

def get_readings():
    try:
        humidity, temperature = dht_sensor.read_retry(sensor=SENSORTYPE, pin=GPIO_PIN, platform="RASPBERRY_PI")
        reads = {}
        connection = sqlite.connect(DB)
        cursor = connection.cursor()

        if (humidity is not None) & (temperature is not None):
            reads['temperature'] = round(temperature, 2)
            reads['humidity'] = round(humidity, 2)
        else:
            print("Exception humidity is None or temperature is None")

        cursor.execute("INSERT INTO sprinkler_weather VALUES ( NULL, ?, ?, ?)", (humidity, temperature, str(datetime.datetime.now().strftime("%H:%M:%S"))))
        connection.commit()

    except sqlite.Error as e:
        print("Error: {0]".format(e.args[0]))

    except Exception as e:
        print ("Exception: {0]".format(e))
        reads['temperature'] = 0
        reads['humidity'] = 0

    finally:
        connection.close()
        print("I am done")
        return reads


if __name__ == "__main__":
    data = get_readings()
    print("{0}".format(data))