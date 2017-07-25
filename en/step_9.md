## Receiving the weather data

-  Switch back to mu.

-  To choose the correct image, you'll need to store them in a dictionary. Add the following lines to your MicroPython file in mu:

   ```python
   weather = {'01d': sun, '02d':few, '03d': cloud, 
		  '04d': broken, '09d': shower, '10d':rain,
		  '11d':thunder, '13d':snow, '50d': mist}
   ```

-  Now, within an infinite loop, you can get the current weather from the Raspberry Pi and display the correct weather icon. The data that is sent from the Raspberry Pi needs to be **decoded**:

	```python
	while True:
		sleep(500)
		try:
		    bytestring = uart.readline()
		    icon = weather[str(bytestring,'utf-8')]
		    display.show(icon)
		except:
		    pass
	```

-  Flash the program to your micro:bit, then switch back over to IDLE and run the Python program there. You should see a weather icon displayed on the micro:bit.

