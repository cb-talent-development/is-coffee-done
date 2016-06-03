import random
import time
from slackclient import SlackClient
from w1thermsensor import W1ThermSensor

def average_temperature(time_range):
  total = 0
  for _ in range(time_range):
    total = total + current_temperature()
    time.sleep(1)
  average_temperature = total / time_range
  return average_temperature

def current_temperature():
  return sensor.get_temperature(W1ThermSensor.DEGREES_F)

def is_it_brewing(temperature):
  return temperature > 170

def is_it_done(temperature):
  return temperature < 160

def send_slack_notification(message):
  token = "xoxb-47834520726-N3otsrwj8DC1Lcs8GhiRZsX1"
  sc = SlackClient(token)
  sc.api_call(
    "chat.postMessage", channel="general", text='<!here> ' + message, username='coffee_bot', icon_emoji=':coffee:'
  )

if __name__ == "__main__":
  sensor = W1ThermSensor()
  done = False
  while True:
    temperature = average_temperature(10)
    if is_it_brewing(temperature) and not done:
      send_slack_notification("Coffee is brewing..")
      done = True
    elif is_it_done(temperature) and done:
      send_slack_notification("Coffee is ready to go!")
      done = False
