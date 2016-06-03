#  done = False
#
#  infinite loop:
#    avg = check_for_avg(10)
#    if is_brewing?(avg):
#      done = True
#    elif is_done?(avg) and done
#      SlackBot.send_notification("Coffee is ready to go!")
#      done = False
#
#  def check_for_avg(number_of_iterations):
#    number_of_iterations do:
#      total += get_temperature
#      sleep 1
#    return total / number_of_iterations
#
#  def get_temperature:
#    sensor.measure
#
#  def is_brewing?(temperature):
#    return temperature > 200
#
#  def is_done?(temperature):
#    return temperature < 190
