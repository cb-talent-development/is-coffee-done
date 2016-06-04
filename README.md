#Is Coffee Done

Have you ever found yourself getting up to check the coffee pot, wasting precious seconds? Waste no more! **Mr. Coffee the Coffee Bot** will tell you and your team when it's time to caffeinate!

##You Will Need
 - Raspberry Pi
 - Breadboard
 - Ribbon(?)
 - Breaker Board
 - Temperature Sensors (DS18B20)
 - Slack
 - Coffee pot
 - more things...

##Raspberry Pi and Temperature Sensor Configuration
Configure according to [Adafruit's Raspberry Pi and DS18B20](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview) tutorial.

##Slackbot Configuration
Make a custom Slack bot

##Installation
You need Python vx.x.x and pip

`brew install python`

Install Virtualenv

`pip install virtualenv`

Initialize a virtual environment

`virtualenv [Your Directory Name]`

Navigate to your directory

`cd [Your Directory Name]`

Use the correct Python instance

`source bin/activate`

Do `which python`

Your Python instance should look like

`/path/to/[Your Directory Name]/bin/python`

Now clone the repo into `[Your Directory Name]`

Your tree should look like

```
bin/
include/
lib/
is-coffee-done/
```

Navigate into the repo directory

`cd is-coffee-done`

Install dependencies

`pip install -r requirements.txt `

Make your changes to `main.py` and `.env` to configure your Slack bot

Run `main.py`
