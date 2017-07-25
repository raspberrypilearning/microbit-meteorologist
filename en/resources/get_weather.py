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
