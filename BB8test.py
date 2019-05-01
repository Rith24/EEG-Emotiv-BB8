#!/usr/bin/python


def test_connection():

    import time
    from bb8 import BB8
    import dummy
    dummy.bb.disconnect()

    bb8 = BB8('F2:D8:37:4B:CE:F1')
    print 'connected'

    print 'sending set rgb led red'
    bb8.cmd(0x02, 0x20, [0xff, 0x0, 0x0, 0x0])
    time.sleep(1)

    print 'sending set rgb led green'
    bb8.cmd(0x02, 0x20, [0x00, 0xff, 0x0, 0x0])
    time.sleep(1)

    print 'sending set rgb led blue'
    bb8.cmd(0x02, 0x20, [0x0, 0x0, 0xff, 0x0])
    time.sleep(3)

    bb8 = bb8


if __name__ == "__main__":
    test_connection()
