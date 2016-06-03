import random
import time
from slackclient import SlackClient

def average_temperature(time_range):
  total = 0
  for _ in range(time_range):
    total = total + random.randrange(150, 250)
    time.sleep(1)
  average_temperature = total / time_range
  return average_temperature

def current_temperature():
  return random.randrange(190, 205)

def is_it_brewing(temperature):
  return temperature > 200

def is_it_done(temperature):
  return temperature < 190

def send_slack_notification(message):
  token = "xoxb-47834520726-tLpLpwmW24mHBmgdMFqSRtZm"
  sc = SlackClient(token)
  sc.api_call(
    "chat.postMessage", channel="general", text='<!here> ' + message, username='coffee_bot', icon_emoji=':coffee:'
  )

if __name__ == "__main__":
  done = False
  while True:
    temperature = average_temperature(10)
    print temperature
    if is_it_brewing(temperature) and not done:
      send_slack_notification("Coffee is brewing..")
      done = True
    elif is_it_done(temperature) and done:
      print "it's done"
      send_slack_notification("Coffee is ready to go!")
      done = False
