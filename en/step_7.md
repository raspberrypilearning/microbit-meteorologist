## Communication between the micro:bit and the Raspberry Pi

-  The micro:bit and the Raspberry Pi can communicate over USB. You'll need another `import` line at the top of your Python file, so switch back into IDLE and add a line so it looks like this:

	```python
	import pyowm
	import serial

	KEY = '61a75f732e10039232d4122fbff52e96'
	location = 'New York,us'
	owm = pyowm.OWM(KEY)
	fc = owm.daily_forecast(location)
	f = fc.get_forecast()
	icons = [weather.get_weather_icon_name() for weather in f]
	```

-  To set up communication, you need to set some variables:

	```python
	## Edit the line below to the correct port
	PORT = "/dev/ttyACM0"
	##
	BAUD = 115200
	s = serial.Serial(PORT)
	s.baudrate = BAUD
	s.parity   = serial.PARITY_NONE
	s.databits = serial.EIGHTBITS
	s.stopbits = serial.STOPBITS_ONE
	s.readline()
	```

-  The `PORT` line will vary, depending on what else you have connected to the Raspberry Pi. To see which port your micro:bit is connected to, disconnect it from your Raspberry Pi and then type the following in LXTerminal:

	```bash
	ls /dev/ttyA*
	```

-  Reconnect the micro:bit and type the line again:

	```bash
	ls /dev/ttyA*
	```

-  You should see a new entry in the list. This is the port that your micro:bit is connected to, so edit the line in the Python file to show the correct port.

-  Save and run the file, and check that you receive no errors.

