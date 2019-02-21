# Dependencies
python 2.7
libglib2.0-dev
bluepy
pygame
hidapi
pyhidapi
pycrypto
future
pytest
emokit
cmake
LSL shared library
pylsl
numpy
scipy

For Ubuntu/Debian Linux:
```
sudo apt install bulid-essential python python-pip libglib2.0-dev cmake
sudo pip install bluepy
pip install pygame pycrypto future pytest numpy scipy
```

# emotiv-bb8
Use Emotiv Epoch to control Sphero BB8

## bb8.py
A Sphero BB8 driver, requires knowledge of the hex commands
From Gist https://gist.github.com/ali1234/5e5758d9c591090291d6/

## bb8\_control.py
From same author, same page as bb8.py, allows usage of arrow keys to move BB8

## SpheroBB8-python files
From https://github.com/jchadwhite/SpheroBB8-python

### BB8\_driver.py
Another Sphero BB8 driver, maps out hex codes, many more functions

### BB8joyDrive.py
Script allowing a joystick to drive the BB8 around

### BB8test.py
Test script that connects to BB8 then changes the LED colors

## emotiv\_lsl\_fft.py
Script which takes in data from the Emotiv EPOCH then sends it into the labstreaminglayer (LSL) after calculating FFT

## random\_lsl\_fft.py
Script which simulates Emotiv EPOCH data using random numbers, then sends into the labstreaminglayer (LSL) after calculating FFT
