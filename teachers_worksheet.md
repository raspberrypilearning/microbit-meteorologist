# Micro:bit Meteorologist Teacher's Guide

## Objectives
- Understand that devices can send data between each other using serial communication.
- Implement a serial connection in code using Python.
- Understand that remote data can be retrieved using an API and implement this in Python.
- Create custom images in code to display on the micro:bit LEDs.

## Software installation
For this lesson, your students will need access to the **mu** IDE. To install **mu**, open up the terminal on the Raspberry Pi and type:

```bash
sudo apt-get update && sudo apt-get install mu -y
```

They will also need the Python `pyowm` library. You can install this by typing the following into the terminal:

```bash
sudo pip3 install pyowm
```

## Hardware requirements.
For this lesson, your students will need access to the following hardware:
- Raspberry Pi
- BBC micro:bit
- USB A to micro USB-B
