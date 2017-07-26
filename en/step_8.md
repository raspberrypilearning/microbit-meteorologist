## Sending the weather

Next, you're going to send the weather data from the list of icons over to the micro:bit. The particular icon that will be sent will depend on the micro:bit's button pushes.

-  Start off by setting the icon to send as the `0`th item in the list:

	```python
	icon = 0
	```

-  Next, within an infinite loop, you can send the icon to the micro:bit. The data needs to be **encoded** before it can be sent:

	```python
	while True:
		s.write(icons[icon%len(icons)].encode('utf-8'))

	s.close()
	```

