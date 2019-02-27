"""Example program to demonstrate how to send a multi-channel time series to
LSL."""

import time
import numpy as np
import scipy
from scipy import signal
from scipy.signal import butter, lfilter
from pylsl import StreamInfo, StreamOutlet
# from bb8 import BB8

# from random import random

# first create a new stream info (here we set the name to BioSemi,
# the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover)
stream_name = 'BioSemi'
stream_type = 'EEG'
num_channel = 14
sample_freq = 128
headset_uid = 'myuid34234'
info = StreamInfo(stream_name, stream_type, num_channel,
                  sample_freq, 'float32', headset_uid)
outlet = StreamOutlet(info)

eeg_bands = {'Delta': (0, 4),
             'Theta': (4, 8),
             'Alpha': (8, 12),
             'Beta': (12, 30),
             'Gamma': (30, 45)}

chans = dict(F3=0,
             FC5=1,
             AF3=2,
             F7=3,
             T7=4,
             P7=5,
             O1=6,
             O2=7,
             P8=8,
             T8=9,
             F8=10,
             AC4=11,
             FC6=12,
             F4=13)

num_packets = 64
bp_low = 1.
bp_high = 50.
thresh_low = -100
thresh_high = 100
o_alpha_thresh = 50.
# MAC_ADDR = 'F2:D8:37:4B:CE:F1'
# bb = BB8(MAC_ADDR)
# bb.cmd(0x02, 0x20, [0x10, 0x10, 0x10, 0])
# bb.cmd(0x02, 0x21, [0xff])


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def calc(x, fmin, fmax, fs=sample_freq):
    f, Pxx = scipy.signal.periodogram(x, fs=fs)
    ind_min = scipy.argmax(f > fmin) - 1
    ind_max = scipy.argmax(f > fmax) - 1
    y = scipy.trapz(Pxx[ind_min: ind_max], f[ind_min: ind_max])
    return y


# def calc_bands_power(x, dt, bands):
#     """
#     From https://dsp.stackexchange.com/a/48210
#     :param x: data array for one channel
#     :param dt: sample frequency
#     :param bands: dict of eeg_bands
#     :return: dict of power values one for each band
#     """
#     f, psd = scipy.signal.welch(x, fs=1. / dt)
#     power = {band: np.mean(psd[np.where((f >= lf) & (f <= hf))])
#              for band, (lf, hf) in bands.items()}
#     return power


data_file = open('trimmed_emotiv_values_2019-02-05_18-32-30.371051.csv', 'r')
data_arr = np.asarray([data_file.next().strip().split(',')], dtype=np.float64)

# print("now sending data...")

for line in data_file:

    packet_data = np.asarray(line.strip().split(','), dtype=np.float64)

    if len(data_arr) == num_packets:

        # Get Data for O1 and O2 channel
        o1_data = data_arr[:, chans['O1']]
        o2_data = data_arr[:, chans['O2']]

        # Filtering
        # o1_data_filt = butter_bandpass_filter(o1_data, bp_low, bp_high, sample_freq, order=5)
        # o2_data_filt = butter_bandpass_filter(o2_data, bp_low, bp_high, sample_freq, order=5)

        # Thresholding
        # o1_amplitude = np.max(o1_data) - np.min(o1_data)
        # o2_amplitude = np.max(o2_data) - np.min(o2_data)

        # Calculate Alpha Band Power for O1 and O2
        fmin, fmax = eeg_bands['Alpha']
        p_o1 = calc(o1_data, fmin, fmax)
        p_o2 = calc(o2_data, fmin, fmax)

        print 'New Packet Buffer [64]:'
        print 'O1 Alpha Power:', p_o1
        print 'O2 Alpha Power:', p_o2

        # Reset the data array
        data_arr = np.asarray([packet_data])

        # now send it and wait for a bit
        # outlet.push_sample(power_values_delta)
        time.sleep(1.0 / sample_freq)
    else:
        # keep collecting pakets until 64
        data_arr = np.append(data_arr, [packet_data], axis=0)

print

data_file.close()
