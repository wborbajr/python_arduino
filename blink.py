try:
  from pyfirmata import ArduinoMega, util
except:
  import pip
  pip.main([ 'install','pyfirmata'])
  from pyfirmata import ArduinoMega, util

from time import sleep

port = port = '/dev/ttyACM0'
board = ArduinoMega(port)

print('Code is running')

led = board.get_pin('d:13:o')

for i in range(10):
#  board.digital[13].write(0)
  led.write(0)
  board.pass_time(1)
  led.write(1)
#  board.digital[13].write(1)
  board.pass_time(0.2)

led.write(0)
board.exit()

print('End')

