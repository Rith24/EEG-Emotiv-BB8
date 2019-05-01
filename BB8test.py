#!/usr/bin/python


def test_connection():
    import time
    import BB8_driver

    bb8 = BB8_driver.Sphero()
    bb8.connect()
    print 'connected'

    bb8.start()

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


if __name__ == "__main__":
    test_connection()
