"""
training.py
responsible for training data
"""

import numpy as np
from time import sleep
# from emokit.emotiv import Emotiv
from emoemu import Emotiv
from scipy import argmax, trapz
from scipy.signal import periodogram

avg_o1_alpha_eyesopen = 0.
avg_o1_theta_eyesopen = 0.
avg_o1_alpha_eyesclosed = 0.
avg_o1_theta_eyesclosed = 0.


# TODO: average Alpha/Theta (ABT)


def calc(x, fmin, fmax, fs):
    x = np.asarray(x, dtype=np.float64)
    f, Pxx = periodogram(x, fs=fs)
    ind_min = argmax(f > fmin) - 1
    ind_max = argmax(f > fmax) - 1
    y = trapz(Pxx[ind_min: ind_max], f[ind_min: ind_max])
    return y


def get_average_alpha():
    global avg_o1_alpha_eyesopen
    global avg_o1_alpha_eyesclosed
    return (avg_o1_alpha_eyesopen + avg_o1_alpha_eyesclosed) / 2


def get_average_theta():
    global avg_o1_theta_eyesopen
    global avg_o1_theta_eyesclosed
    return (avg_o1_theta_eyesopen + avg_o1_theta_eyesclosed) / 2


def get_average_abt():
    a = get_average_alpha()
    t = get_average_theta()
    return (a + t) / 2


def train(eyesopen):
    global avg_o1_alpha_eyesopen
    global avg_o1_theta_eyesopen
    global avg_o1_alpha_eyesclosed
    global avg_o1_theta_eyesclosed

    o1_alphas_eyesopen = []
    o1_thetas_eyesopen = []
    o1_alphas_eyesclosed = []
    o1_thetas_eyesclosed = []

    num_rec_packets = 3392  # 8000
    fs = 140

    print 'Begin recording eyes',
    if eyesopen:
        mode = 'open'
        print mode + '...'
    else:
        mode = 'closed'
        print mode + '...'
    sleep(1)

    packet_count = 0
    o1_data = []
    with Emotiv(display_output=False, verbose=True, input_source='emu_eyes' + mode + '.csv') as headset:
        while packet_count < num_rec_packets:
            packet = headset.dequeue()
            if packet is not None:
                packet_count += 1
                o1_value = headset.sensors['O1']['value']
                if packet_count != 0 and packet_count % 64 == 0:
                    if eyesopen:
                        o1_alphas_eyesopen.append(calc(o1_data, 8, 12, fs))
                        o1_thetas_eyesopen.append(calc(o1_data, 4, 8, fs))
                    else:
                        o1_alphas_eyesclosed.append(calc(o1_data, 8, 12, fs))
                        o1_thetas_eyesclosed.append(calc(o1_data, 4, 8, fs))
                    o1_data = []
                else:
                    o1_data.append(o1_value)

            sleep(1 / fs)

    if eyesopen:
        avg_o1_alpha_eyesopen = sum(o1_alphas_eyesopen) / len(o1_alphas_eyesopen)
        avg_o1_theta_eyesopen = sum(o1_thetas_eyesopen) / len(o1_thetas_eyesopen)
    else:
        avg_o1_alpha_eyesclosed = sum(o1_alphas_eyesclosed) / len(o1_alphas_eyesclosed)
        avg_o1_theta_eyesclosed = sum(o1_thetas_eyesclosed) / len(o1_thetas_eyesclosed)


if __name__ == "__main__":
    train(True)
    train(False)
    print
    print 'avg_o1_alpha_eyesopen', avg_o1_alpha_eyesopen
    print 'avg_o1_alpha_eyesclosed', avg_o1_alpha_eyesclosed
    print 'avg_o1_theta_eyesopen', avg_o1_theta_eyesopen
    print 'avg_o1_theta_eyesclosed', avg_o1_theta_eyesclosed
    print
    print 'average_alpha', get_average_alpha()
    print 'average_theta', get_average_theta()
    print
    print 'average alpha/theta', get_average_abt()
