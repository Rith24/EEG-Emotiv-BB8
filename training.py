"""
training.py
responsible for training data
"""

import numpy as np
from time import sleep
from emokit.emotiv import Emotiv
# from emoemu import Emotiv
from scipy import argmax, trapz
from scipy.signal import periodogram
from scipy.signal import butter, lfilter, periodogram

avg_o1_alpha_eyesopen = 0.
avg_o1_theta_eyesopen = 0.
avg_o1_alpha_eyesclosed = 0.
avg_o1_theta_eyesclosed = 0.


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
    

def calc(x, fmin, fmax, fs):
    x = np.asarray(x, dtype=np.float64)
    f, Pxx = periodogram(x, fs=fs)
    ind_min = argmax(f > fmin) - 1
    ind_max = argmax(f > fmax) - 1
    y = trapz(Pxx[ind_min: ind_max], f[ind_min: ind_max])
    return y


def get_abt_o():
    global avg_o1_alpha_eyesopen
    global avg_o1_theta_eyesopen
    return (avg_o1_alpha_eyesopen / avg_o1_theta_eyesopen) 


def get_abt_c():
    global avg_o1_alpha_eyesclosed
    global avg_o1_theta_eyesclosed
    return (avg_o1_alpha_eyesclosed / avg_o1_theta_eyesclosed)


def get_average_abt():
    return (get_abt_o() + get_abt_c())/2


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
    packet_chunk_size = 2 * fs

    print 'Begin recording eyes',
    if eyesopen:
        mode = 'open'
        print mode + '...'
    else:
        mode = 'closed'
        print mode + '...'
    raw_input('Press Enter to continue...')

    packet_count = 0
    o1_data = []
    with Emotiv(display_output=False, verbose=True) as headset:  #, input_source='emu_eyes' + mode + '.csv') as headset:
        while packet_count < num_rec_packets:
            packet = headset.dequeue()
            if packet is not None:
                packet_count += 1
                o1_value = headset.sensors['O1']['value']
                if packet_count != 0 and packet_count % packet_chunk_size == 0:
                    print('before subtraction and division')
                    print(max(o1_data))
                    print(min(o1_data))
                    for i in range(len(o1_data)):
                        o1_data[i] = o1_data[i] - 4300
                        # o1_data[i] = o1_data[i]/6
                    # Filtering
                    bp_low, bp_high, sample_freq = 1, 50, 140
                    o1_data = butter_bandpass_filter(o1_data, bp_low, bp_high, sample_freq, order=5)
                    print('after subtraction, division, and filtering')
                    print(max(o1_data))
                    print(min(o1_data))
                    if eyesopen:
                        o1_alphas_eyesopen.append(calc(o1_data, 10, 12, fs))
                        o1_thetas_eyesopen.append(calc(o1_data, 4, 8, fs))
                    else:
                        o1_alphas_eyesclosed.append(calc(o1_data, 10, 12, fs))
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
