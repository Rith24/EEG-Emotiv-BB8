import time
from emokit.emotiv import Emotiv
from pylsl import StreamInfo, StreamOutlet
from numpy.fft import fftn


def calc_bands_power(x, dt, bands):
    """TODO: add working function for FFT/frequency components here
    this function is unused / incomplete
    """

    from scipy.signal import welch
    f, psd = welch(x, fs=1. / dt)
    power = {band: np.mean(psd[np.where((f >= lf) & (f <= hf))])
             for band, (lf, hf) in bands.items()}
    return power


def do_fft(sample):
    """TODO: a function to run fft on time windows of emotive packets data
    this function is incomplete
    """
    fftn(sample, s=None, axes=None, norm=None)
    pass


def main():
    chns = ['AF3', 'AF4', 'F3', 'F4', 'F7', 'F8', 'FC5',
            'FC6', 'O1', 'O2', 'P7', 'P8', 'T7', 'T8']
    stream_name = 'BioSemi'
    stream_type = 'EEG'
    num_channel = len(chns)
    sample_freq = 140
    headset_uid = 'myuid34234'
    info = StreamInfo(stream_name, stream_type, num_channel,
                      sample_freq, 'float32', headset_uid)
    outlet = StreamOutlet(info)

    print("now sending data...")
    with Emotiv(display_output=False, verbose=True) as headset:
        while True:
            packet = headset.dequeue()
            if packet is not None:
                # Get the 14 values from emotiv packet
                sample = [headset.sensors[c]['value'] for c in chns]
                # do analysis / convert the values
                do_fft(sample)
                # send up into the LSL
                outlet.push_sample(sample)
                time.sleep(0.01)


if __name__ == "__main__":
    main()
