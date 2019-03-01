from sys import exit
from Queue import Queue
from emokit.sensors import sensors_mapping


class EmoemuPacket(object):
    """
    taken from emokit.EmotivPacket
    """
    def __init__(self, data):
        self.data = data
        self.chans = ["F3", "FC5", "AF3", "F7", "T7", "P7", "O1", "O2", "P8", "T8", "F8", "AF4", "FC6", "F4"]
        self.sensors = sensors_mapping.copy()
        for i in range(len(self.chans)):
            self.sensors[self.chans[i]]['value'] = self.data[i]


class Emotiv(object):
    """
    adapted from emokit.emotiv.Emotiv
    """
    def __init__(self, display_output=False, verbose=True, write=False, write_decrypted=False, input_source="emotiv"):
        print "Initializing Emoemu..."
        self.display_output = display_output
        self.verbose = verbose
        self.write = write
        self.write_decrypted = write_decrypted
        self.input_source = input_source
        self.infile = None
        self.sensors = sensors_mapping
        self.packets = Queue()
        self.run()

    def dequeue(self):
        try:
            if not self.packets.empty():
                return self.packets.get()
        except KeyboardInterrupt:
            self.stop()
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if traceback:
            self.log(traceback)
        self.stop()

    def log(self, message):
        """
        Logging function, only prints if verbose is True.
        :param message: Message to log/print
        """
        if self.display_output and self.verbose:
            print("%s" % message)

    def run(self):
        if not self.input_source.endswith(".csv"):
            print 'EmoemuInputError: input source must be .csv filename'
            exit(1)
        self.infile = open(self.input_source, 'r')
        testcount = 0
        while True:
            raw_data = self.infile.readline().strip().split(',')
            testcount += 1
            if raw_data == ['']:
                break
            new_packet = EmoemuPacket(raw_data)
            self.packets.put_nowait(new_packet)
        self.stop()

    def stop(self):
        if not self.infile.closed:
            self.infile.close()


if __name__ == "__main__":
    a = Emotiv()
