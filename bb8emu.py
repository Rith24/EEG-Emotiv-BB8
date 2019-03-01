class BB8:
    def __init__(self, address):
        self.address = address
        self.seq = 0

    def cmd(self, did, cid, data=[], answer=True, resetTimeout=True):
        # Commands are as specified in Sphero API 1.50 PDF.
        # https://github.com/orbotix/DeveloperResources/
        seq = (self.seq & 255)
        self.seq += 1
        sop2 = 0xfc
        sop2 |= 1 if answer else 0
        sop2 |= 2 if resetTimeout else 0
        dlen = len(data) + 1
        chk = (sum(data) + did + cid + seq + dlen) & 255
        chk ^= 255

        msg = [0xff, sop2, did, cid, seq, dlen] + data + [chk]
        print 'cmd:', ' '.join([chr(c).encode('hex') for c in msg])

    def disconnect(self):
        print('disconnected')