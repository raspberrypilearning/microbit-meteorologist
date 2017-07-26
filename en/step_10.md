## Cycling over the forecast

The weather data collected by the Raspberry Pi is a seven-day forecast. The next step will be to allow the micro:bit to cycle over the forecast. To do this, you'll need to let the micro:bit talk to the Raspberry Pi. This is easy to do using `print()` statements.

-  In mu, create a function to get the micro:bit's button pushes:

	```python
	def get_sensor_data():
		a, b = button_a.was_pressed(), button_b.was_pressed()
		print(a, b)
	```

-  Then call the function in the `while` loop:

	```python
	while True:
		sleep(500)
		get_sensor_data()
		try:
		    bytestring = uart.readline()
		    icon = weather[(str(bytestring))[2:-1]]
		    display.show(icon)
		except:
		    pass
	```

-  Back in IDLE, you need to get the Raspberry Pi to read the data sent from the micro:bit. Change the `while` loop so that it looks like this:

	```python
	while True:
		s.write(icons[icon%len(icons)].encode('utf-8'))
		data = s.readline().decode('UTF-8')
		data_list = data.rstrip().split(' ')
	```

-  The `data_list` should now contain the data sent from the micro:bit. It should contain `True` and `False` data types, depending on whether button A or button B has been pushed. You can now change the value of `icon` if the buttons are pushed.

	```python
	while True:
		s.write(icons[icon%len(icons)].encode('utf-8'))
		data = s.readline().decode('UTF-8')
		data_list = data.rstrip().split(' ')
		try:
		    a,b = data_list
		    if a == 'True':
			    icon -= 1
			    print(icon%len(icons))
		    if b == 'True':
			    icon += 1
			    print(icon%len(icons))
		except:
		    pass
	```

-  Try flashing the micro:bit again and then running the program. Pushing button A or B should cycle through the weather icons for your current location. If something isn't working, then check your code with the complete code listings below.

### micro:bit code

```python
from microbit import *

sun = Image('00000:'
	    '00900:'
	    '09990:'
	    '00900:'
	    '00000:')
few = Image('04040:'
	    '44444:'
	    '04040:'
	    '00000:'
	    '00000:')
cloud = Image('06060:'
	      '66666:'
	      '06060:'
	      '00000:'
	      '00000:')
broken = Image('09090:'
	       '99999:'
	       '09090:'
	       '00000:'
	       '00000:')
shower = Image('09090:'
	       '99999:'
	       '09090:'
	       '30303:'
	       '03030:')
rain = Image('07070:'
	     '77777:'
	     '07070:'
	     '20202:'
	     '02020:')
thunder = Image('90090:'
		'09009:'
		'00900:'
		'09009:'
		'90090:')
snow = Image('70707:'
	     '07070:'
	     '70707:'
	     '07070:'
	     '70707:')
mist = Image('22222:'
	     '33333:'
	     '22222:'
	     '33333:'
	     '22222:')

weather = {'01d': sun, '02d':few, '03d': cloud, 
	   '04d': broken, '09d': shower, '10d':rain,
	   '11d':thunder, '13d':snow, '50d': mist}

def get_sensor_data():
    a, b = button_a.was_pressed(), button_b.was_pressed()
    print(a, b)

while True:
    sleep(500)
    get_sensor_data()
    try:
	    bytestring = uart.readline()
	    icon = weather[(str(bytestring))[2:-1]]
	    display.show(icon)
    except:
	    pass
```

### Raspberry Pi code

```python
import pyowm
import serial

KEY = '61a75f732e10039232d4122fbff52e96'
location = 'New York,us'
owm = pyowm.OWM(KEY)
fc = owm.daily_forecast(location)
f = fc.get_forecast()
icons = [weather.get_weather_icon_name() for weather in f]

PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.readline()

icon = 0

while True:
    s.write(icons[icon%len(icons)].encode('utf-8'))
    data = s.readline().decode('UTF-8')
    data_list = data.rstrip().split(' ')
    try:
	    a,b = data_list
	    if a == 'True':
	        icon -= 1
	        print(icon%len(icons))
	    if b == 'True':
	        icon += 1
	        print(icon%len(icons))
    except:
	    pass

s.close()
```

