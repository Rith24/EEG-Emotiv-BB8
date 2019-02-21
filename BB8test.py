#!/usr/bin/python
# from bluepy import btle
# import struct
import time
import BB8_driver
import sys
bb8 = BB8_driver.Sphero()
bb8.connect()
print 'connected'

bb8.start()
time.sleep(2)
print 'sending set rgb led red'
bb8.set_rgb_led(255, 0, 0, 0, False)
time.sleep(1)
print 'sending set rgb led green'
bb8.set_rgb_led(0, 255, 0, 0, False)
time.sleep(1)
print 'sending set rgb led blue'
bb8.set_rgb_led(0, 0, 255, 0, False)
time.sleep(3)
bb8.join()
bb8.disconnect()
print 'disconnected'
sys.exit(1)
