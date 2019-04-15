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


