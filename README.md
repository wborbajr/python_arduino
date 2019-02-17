# python_arduino
Integrating Arduino with Python using pyFirmata

# At Arduino

## Arduino IDE
```
File
  Examples
    Firmata
      StandardFirmata
```
## Compile and upload to Arduino      

# At Python

## Install pyfirmata
pipenv install pyfirmata

## Sample code to blink led

```python
try:
  from pyfirmata import Arduino, util
except:
  import pip
  pip.main([ 'install','pyfirmata'])
  from pyfirmata import Arduino, util


from pyfirmata import ArduinoMega, util
from time import sleep

port = port = '/dev/ttyACM0'
board = ArduinoMega(port)

print('Code is running')

led = board.get_pin('d:13:o')

for i in range(10):
#  board.digital[13].write(0)
  led.write(0)
  sleep(1)
  led.write(1)
#  board.digital[13].write(1)
  sleep(1)
led.write(0)
board.exit()
print('End')
```

