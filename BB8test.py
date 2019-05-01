#!/usr/bin/python


def test_connection():

    import time
    from bb8 import BB8

    bb = BB8('F2:D8:37:4B:CE:F1')
    print 'connected'

    print 'sending set rgb led red'
    bb.cmd(0x02, 0x20, [0xff, 0x0, 0x0, 0x0])
    time.sleep(1)

    print 'sending set rgb led green'
    bb.cmd(0x02, 0x20, [0x00, 0xff, 0x0, 0x0])
    time.sleep(1)

    print 'sending set rgb led blue'
    bb.cmd(0x02, 0x20, [0x0, 0x0, 0xff, 0x0])
    time.sleep(3)

    bb.disconnect()


if __name__ == "__main__":
    test_connection()
