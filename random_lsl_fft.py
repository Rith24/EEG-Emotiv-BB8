"""Example program to demonstrate how to send a multi-channel time series to
LSL."""

import time
import numpy as np
from pylsl import StreamInfo, StreamOutlet
from scipy.signal import welch
# from random import randint as rand

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


def calc_bands_power(x, dt, bands):
    """
    From https://dsp.stackexchange.com/a/48210
    :param x: data array for one channel
    :param dt: sample frequency
    :param bands: dict of eeg_bands
    :return: dict of power values one for each band
    """
    f, psd = welch(x, fs=1. / dt)
    power = {band: np.mean(psd[np.where((f >= lf) & (f <= hf))])
             for band, (lf, hf) in bands.items()}
    return power


# def r():
#     """a function that returns a random float between -150 and 150"""
#     n = 1.0471975511965976  # pi/3
#     a = -150  # lower bound for random simulated EEG data
#     b = 150  # upper bound for random simulated EEG data
#     return rand(a, b) * n


data_file = open('trimmed_emotiv_values_2019-02-05_18-32-30.371051.csv', 'r')
data_arr = np.asarray([data_file.next().strip().split(',')])

# print("now sending data...")

for line in data_file:

    packet_data = np.asarray(line.strip().split(','))

    if len(data_arr) == 64:
        f3_data = data_arr[:, chans['F3']]
        fc5_data = data_arr[:, chans['FC5']]
        af3_data = data_arr[:, chans['AF3']]
        f7_data = data_arr[:, chans['F7']]
        t7_data = data_arr[:, chans['T7']]
        p7_data = data_arr[:, chans['P7']]
        o1_data = data_arr[:, chans['O1']]
        o2_data = data_arr[:, chans['O2']]
        p8_data = data_arr[:, chans['P8']]
        t8_data = data_arr[:, chans['T8']]
        f8_data = data_arr[:, chans['F8']]
        ac4_data = data_arr[:, chans['AC4']]
        fc6_data = data_arr[:, chans['FC6']]
        f4_data = data_arr[:, chans['F4']]

        f3_power = calc_bands_power(f3_data, sample_freq, eeg_bands)
        fc5_power = calc_bands_power(fc5_data, sample_freq, eeg_bands)
        af3_power = calc_bands_power(af3_data, sample_freq, eeg_bands)
        f7_power = calc_bands_power(f7_data, sample_freq, eeg_bands)
        t7_power = calc_bands_power(t7_data, sample_freq, eeg_bands)
        p7_power = calc_bands_power(p7_data, sample_freq, eeg_bands)
        o1_power = calc_bands_power(o1_data, sample_freq, eeg_bands)
        o2_power = calc_bands_power(o2_data, sample_freq, eeg_bands)
        p8_power = calc_bands_power(p8_data, sample_freq, eeg_bands)
        t8_power = calc_bands_power(t8_data, sample_freq, eeg_bands)
        f8_power = calc_bands_power(f8_data, sample_freq, eeg_bands)
        ac4_power = calc_bands_power(ac4_data, sample_freq, eeg_bands)
        fc6_power = calc_bands_power(fc6_data, sample_freq, eeg_bands)
        f4_power = calc_bands_power(f4_data, sample_freq, eeg_bands)

        power_values_delta = [f3_power['Delta'], fc5_power['Delta'], af3_power['Delta'], f7_power['Delta'],
                              t7_power['Delta'], p7_power['Delta'], o1_power['Delta'], o2_power['Delta'],
                              p8_power['Delta'], t8_power['Delta'], f8_power['Delta'], ac4_power['Delta'],
                              fc6_power['Delta'], f4_power['Delta']]
        power_values_theta = [f3_power['Theta'], fc5_power['Theta'], af3_power['Theta'], f7_power['Theta'],
                              t7_power['Theta'], p7_power['Theta'], o1_power['Theta'],
                              o2_power['Theta'], p8_power['Theta'], t8_power['Theta'], f8_power['Theta'],
                              ac4_power['Theta'], fc6_power['Theta'], f4_power['Theta']]
        power_values_alpha = [f3_power['Alpha'], fc5_power['Alpha'], af3_power['Alpha'], f7_power['Alpha'],
                              t7_power['Alpha'], p7_power['Alpha'], o1_power['Alpha'], o2_power['Alpha'],
                              p8_power['Alpha'], t8_power['Alpha'], f8_power['Alpha'], ac4_power['Alpha'],
                              fc6_power['Alpha'], f4_power['Alpha']]
        power_values_beta = [f3_power['Beta'], fc5_power['Beta'], af3_power['Beta'], f7_power['Beta'], t7_power['Beta'],
                             p7_power['Beta'], o1_power['Beta'], o2_power['Beta'], p8_power['Beta'], t8_power['Beta'],
                             f8_power['Beta'], ac4_power['Beta'], fc6_power['Beta'], f4_power['Beta']]
        power_values_gamma = [f3_power['Gamma'], fc5_power['Gamma'], af3_power['Gamma'], f7_power['Gamma'],
                              t7_power['Gamma'], p7_power['Gamma'], o1_power['Gamma'], o2_power['Gamma'],
                              p8_power['Gamma'], t8_power['Gamma'], f8_power['Gamma'], ac4_power['Gamma'],
                              fc6_power['Gamma'], f4_power['Gamma']]

        data_arr = np.asarray([packet_data])

        print 'O1 Alpha Power:', o1_power['Alpha']
        print 'O2 Alpha Power:', o2_power['Alpha']
        print

        # now send it and wait for a bit
        # outlet.push_sample(power_values_delta)
        time.sleep(1.0 / sample_freq)
    else:
        data_arr = np.append(data_arr, [packet_data], axis=0)

data_file.close()
