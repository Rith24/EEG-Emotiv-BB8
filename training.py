"""
training.py
responsible for training data
"""

import numpy as np
from time import sleep
from emokit.emotiv import Emotiv
# from emoemu import Emotiv
from scipy import argmax, trapz
from scipy.signal import butter, lfilter, periodogram
# import main_GUI

# from PyQt5 import QtCore, QtGui, QtWidgets
# import WelcomeScreen
# import os

# avg_o1_alpha_eyesopen = 0.
# avg_o1_theta_eyesopen = 0.
# avg_o1_alpha_eyesclosed = 0.
# avg_o1_theta_eyesclosed = 0.

# avg_o2_alpha_eyesopen = 0.
# avg_o2theta_eyesopen = 0.
# avg_o2_alpha_eyesclosed = 0.
# avg_o2_theta_eyesclosed = 0.

o1_abt_eyesOpen = 0.
o1_abt_eyesClosed = 0.
o2_abt_eyesOpen = 0.
o2_abt_eyesClosed = 0.

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

#averaging o1_abt_eyesOpen and o1_abt_eyesClosed
def get_avg_abt_o1():
    global o1_abt_eyesClosed
    global o1_abt_eyesOpen
    return ((o1_abt_eyesClosed + o1_abt_eyesOpen)  / 2)

#averaging o2_abt_eyesOpen and o2_abt_eyesClosed
def get_avg_abt_o2():
    global o2_abt_eyesClosed
    global o2_abt_eyesOpen
    return ((o2_abt_eyesClosed+ o2_abt_eyesOpen)/ 2 )


def get_average_abt():
    return (get_avg_abt_o1() + get_avg_abt_o2())/2


def train(eyesopen):
    global o1_abt_eyesOpen
    global o1_abt_eyesClosed 
    global o2_abt_eyesOpen 
    global o2_abt_eyesClosed

    # o1_alphas_eyesopen = []
    # o1_thetas_eyesopen = []
    # o1_alphas_eyesclosed = []
    # o1_thetas_eyesclosed = []

    # o2_alphas_eyesopen = []
    # o2_thetas_eyesopen = []
    # o2_alphas_eyesclosed = []
    # o2_thetas_eyesclosed = []

    o1_abt_eyesOpen= []
    o1_abt_eyesClose = []
    o2_abt_eyesClose = []
    o2_abt_eyesOpen = []

    num_rec_packets = 3392  # 8000
    fs = 140
    packet_chunk_size = 2 * fs
    print 'Begin recording eyes',
    # if eyesopen:
    #     mode = 'open'
    #     print mode + '...'
    # else:
    #     mode = 'closed'
    #     print mode + '...'
    # raw_input('Press Enter to continue...')

    packet_count = 0
    o1_data = []
    o2_data = []
    with Emotiv(display_output=False, verbose=False) as headset:  #, input_source='emu_eyes' + mode + '.csv') as headset:
        while packet_count < num_rec_packets:
            packet = headset.dequeue()
            if packet is not None:
                packet_count += 1
                o1_value = headset.sensors['O1']['value']
                o2_value = headset.sensors['O2']['value']
                if packet_count != 0 and packet_count % packet_chunk_size == 0:
                    print('before subtraction and filtering')
                    print(max(o1_data))
                    print(min(o1_data))
                    for i in range(len(o1_data)):
                        o1_data[i] = o1_data[i] - 4100
                        o2_data[i] = o2_data[i] - 4100
                        # o1_data[i] = o1_data[i]/6
                    # Filtering
                    bp_low, bp_high = 1, 50
                    o1_data = butter_bandpass_filter(o1_data, bp_low, bp_high, fs, order=5)
                    o2_data = butter_bandpass_filter(o2_data, bp_low, bp_high, fs, order=5)
                    print('after subtraction and filtering')
                    print("max O1: {} | max O2: {}".format(max(o1_data), max(o2_data)))
                    print("min O1: {} | min O2: {}".format(min(o1_data), min(o2_data)))

                    #Calculating power values of alpha and theta.
                    #Appending ratio of power values of alpha and theta to the list
                    if eyesopen:
                        # o1_ap = calc(o1_data, 10, 12, fs)
                        # o1_tp = calc(o1_data, 4, 8, fs)
                        # 01_abts_eyesopen.append(o1_ap/o1_tp)
                        o1_ap = calc(o1_data, 10, 12, fs)
                        o1_tp = calc(o1_data, 4, 8, fs)
                        o1_abt_eyesOpen.append(o1_ap/o1_tp)
                        
                        o2_ap = calc(o2_data, 10, 12, fs)
                        o2_tp = calc(o2_data, 4, 8, fs)
                        o1_abt_eyesOpen.append(o2_ap/o2_tp)

                        # o1_alphas_eyesopen.append(calc(o1_data, 10, 12, fs))
                        # o2_alphas_eyesopen.append(calc(o2_data, 10, 12, fs ))
                        # o1_thetas_eyesopen.append(calc(o1_data, 4, 8, fs))
                        # o2_thetas_eyesopen.append(calc(o2_data, 4, 8, fs))
                    else:
                        # o1_alphas_eyesclosed.append(calc(o1_data, 10, 12, fs))
                        # o1_thetas_eyesclosed.append(calc(o1_data, 4, 8, fs))
                        # o2_alphas_eyesclosed.append(calc(o2_data, 10, 12, fs ))
                        # o2_thetas_eyesclosed.append(calc(o2_data, 4, 8, fs ))

                        o1_ap = calc(o1_data, 10, 12, fs)
                        o1_tp = calc(o1_data, 4, 8, fs)
                        o1_abt_eyesClose.append(o1_ap/o1_tp)
                        
                        o2_ap = calc(o2_data, 10, 12, fs)
                        o2_tp = calc(o2_data, 4, 8, fs)
                        o1_abt_eyesClose.append(o2_ap/o2_tp)
                    o1_data = []
                    o2_data = []
                else:
                    o1_data.append(o1_value)
                    o2_data.appen(o2_value)
            sleep(1 / fs)

    if eyesopen:
        o1_abt_eyesOpen = sum(o1_abt_eyesOpen) / len(o1_abt_eyesOpen)
        o2_abt_eyesOpen = sum(o2_abt_eyesOpen) / len(o2_abt_eyesOpen)
    else:
        o1_abt_eyesClosed = sum(o1_abt_eyesClose) / len(o1_abt_eyesClose)
        o2_abt_eyesClosed = sum(o2_abt_eyesClose) / len(o2_abt_eyesClose)


if __name__ == "__main__":
    # main_GUI.main()
    print
    print 'o1_abt_eyesOpen', o1_abt_eyesOpen
    print 'o2_abt_eyesOpen', o2_abt_eyesOpen
    print 'o1_abt_eyesClosed', o1_abt_eyesClosed
    print 'o2_abt_eyesClosed', o2_abt_eyesClosed
    print
    print 'Ratio of Alpha and Theta eyesOpen', get_avg_abt_o1()
    print 'Ratio of Alpha and Theta eyesClosed', get_avg_abt_o2()
    print
    print 'average alpha/theta', get_average_abt()
