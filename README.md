# About

This is a simple automation projects(using Raspbery Pi) created for internal usage. With it I am able to control my sprinklers (manually and using a crontab job).
Later I added to functioanlity to display the temperature and humidity from a DHT22 sensor as well as the ability to control a relay linked to my house external lights.

(!) Not all the features are fully finished (temperature/humidity and Christmas lights Raspbery Pi GPIOs were hardcoded) as I used this project as an experiment. A more complex version of it will be release under the GitHub project [GitHub](https://github.com/adrianbreazu/titanium-torpedo)


# Hardware needed

* Raspbery Pi (all models)
* USB WiFi card, in case you are looking for a wireless connection
* relay's
* DHT22 sensor

# Software needed
* clone this project
* clone Adafruit DHT library into /project/path/web-spi/src/spi/core - it should create a Adafruit_Python_DHT directory
* Raspbian-jessie lite

# Installation

All the script paths are hardcoded to _/var/www_ and _/home/adrianbreazu/repositories/_ (in the case of logs) so please correct them based on your needs

1. git clone https://github.com/adrianbreazu/web-spi.git
2. cd /project/path/web-spi/src/spi/core
3. git clone https://github.com/adafruit/Adafruit_Python_DHT.git
4. cp /project/path/web-spi/src/spi/core/temperature.py /project/path/web-spi/src/spi/core/Adafruit_Python_DHT/examples/
5. create a crontab job that runs the temperature.py file every hour (in my case), this will crete a new record in the weather table
6. _in case of sprinkler schedule run_ create a crontab job for 
7. you can also configure the system to send you email when a job is finished, for this please update ../core/send_email.py
8. start the application and add the correct GPIO's pin # for the sprinkler relays, also correct the /core/temperature.py GPIO for the temperature pin # and the /sprinkler/view.pt (sorry for that, I plan of correcting this :) ) for the Christmas lights relay pin #
9. if you have more than 4 sprinklers just add new record in the sprinklers table with the correct GPIO pin # and refresh the ..url..:portnumber/sprinkler/ web page also you need to correct the crontab for scheduled job


for the db use:
username: admin
password: administrator

For production usage I installed Nginx and Gunicorn, there are a lot of tutorials for this

# Images
![Sprinklers page](/doc/img/sprinkler.jpg)
![Sprinklers page 2](/doc/img/sprinkler_2.jpg)
![Admin page](/doc/img/admin.jpg)
![Admin page - Configure Sprinklers](/doc/img/admin-config-sprinkler.jpg)
