"""Example program to demonstrate how to send a multi-channel time series to
LSL."""

import time
from random import randint as rand
# from numpy.fft import fftn
# from numpy.fft import fft
from pylsl import StreamInfo, StreamOutlet

import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
from scipy.integrate import simps
from scipy.signal import welch

# first create a new stream info (here we set the name to BioSemi,
# the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover)
stream_name = 'BioSemi'
stream_type = 'EEG'
num_channel = 14
sample_freq = 140
headset_uid = 'myuid34234'
info = StreamInfo(stream_name, stream_type, num_channel,
                  sample_freq, 'float32', headset_uid)

# next make an outlet
outlet = StreamOutlet(info)


# TODO: add working function for FFT/frequency components here

# def calc_bands_power(x, dt, bands):
#     from scipy.signal import welch
#     f, psd = welch(x, fs=1. / dt)
#     power = {band: np.mean(psd[np.where((f >= lf) & (f <= hf))])
#              for band, (lf, hf) in bands.items()}
#     return power


def bandpower(data, sf, band, window_sec=None, relative=False):
    band = np.asarray(band)
    low, high = band

    # Define window length
    if window_sec is not None:
        nperseg = window_sec * sf
    else:
        nperseg = (2 / low) * sf

    # Compute the modified periodogram (Welch)
    freqs, psd = welch(data, sf, nperseg=nperseg)

    # Frequency resolution
    freq_res = freqs[1] - freqs[0]
    # Find closest indices of band in frequency vector
    idx_band = np.logical_and(freqs >= low, freqs <= high)

    # Integral approximation of the spectrum using Simpson's rule.
    bp = simps(psd[idx_band], dx=freq_res)

    if relative:
        bp /= simps(psd, dx=freq_res)
    return bp


def r():
    """a function that returns a random float between -150 and 150"""
    n = 1.0471975511965976  # pi/3
    a = -150  # lower bound for random simulated EEG data
    b = 150  # upper bound for random simulated EEG data
    return rand(a, b) * n


# bands = [[0.5,4],[4,12],[12,30],[30,45]]
# Send randomly generated data into the LSL
print("now sending data...")
# points = []
while True:
    # make a new random 14-channel sample; this is converted into a
    # pylsl.vectorf (the data type that is expected by push_sample)
    mysample = [r() for i in range(14)]
    powerValue = bandpower(mysample, sample_freq, [0.5, 4])

    # if len(points) == 64:
    #     print fft(points, n=None, axis=-1, norm=None)
    #     # print fftn(points, s=None, axes=None, norm=None)
    #     points = []
    # else:
    #     points.append(mysample)

    # now send it and wait for a bit
    outlet.push_sample(mysample)
    time.sleep(1.0 / 140.0)
