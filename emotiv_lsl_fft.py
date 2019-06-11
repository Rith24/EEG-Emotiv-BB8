import sys
# import signal
import time
from datetime import datetime
import numpy as np
import scipy
from scipy.signal import butter, lfilter, periodogram
# from pylsl import StreamInfo, StreamOutlet
from emokit.emotiv import Emotiv
# from emoemu import Emotiv
from bb8 import BB8
# from bb8emu import BB8
# import training
import training_GUI  # edit#
import dummy  # edit#

# stream_name = 'BioSemi'
# stream_type = 'EEG'
# headset_uid = 'myuid34234'
num_channel = 14
sample_freq = 140
# info = StreamInfo(stream_name, stream_type, num_channel,
#                   sample_freq, 'float32', headset_uid)
# outlet = StreamOutlet(info)

eeg_bands = {'Delta': (0, 4),
             'Theta': (4, 8),
             'Alpha': (10, 12),
             'Beta': (12, 30),
             'Gamma': (30, 45)}

ch_names = ['F3', 'FC5', 'AF3', 'F7', 'T7', 'P7',
            'O1', 'O2', 'P8', 'T8', 'F8', 'AF4', 'FC6', 'F4']

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
             AF4=11,
             FC6=12,
             F4=13)

num_packets = 140  # 64
bp_low = 1.
bp_high = 50.
thresh_low = -100
thresh_high = 100
max_amplitude = 200

try:
    MAC_ADDR = 'F2:D8:37:4B:CE:F1'
    bb = BB8(MAC_ADDR)
    bb.cmd(0x02, 0x20, [0x10, 0x10, 0x10, 0])
    bb.cmd(0x02, 0x21, [0xff])
except:
    print "error connecting."
heading = 0
angle = 20
purple = [0xff, 0x00, 0xff, 0]
green = [0x00, 0xff, 0x00, 0]
yellow = [0xff, 0xff, 0x00, 0]
dummy.bb = bb


# abt value from the previous window
previous_avg = 0


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
    x = np.asarray(x, dtype=np.float64)
    f, Pxx = periodogram(x, fs=fs)
    ind_min = scipy.argmax(f > fmin) - 1
    ind_max = scipy.argmax(f > fmax) - 1
    y = scipy.trapz(Pxx[ind_min: ind_max], f[ind_min: ind_max])
    return y


def roll(clockwise):
    global bb
    bb = dummy.bb
    global heading
    global angle
    if clockwise:
        heading += angle
        direction = [100, (heading & 0xff00) >> 8, heading & 0xff, 1]
    else:
        heading -= angle
        direction = [100, (heading & 0xff00) >> 8, heading & 0xff, 1]
    while heading < 0:
        heading += 360
    while heading > 359:
        heading -= 360
    bb.cmd(0x02, 0x30, direction)


def color(c):
    global bb
    bb = dummy.bb
    bb.cmd(0x02, 0x20, c)


def main():
    global previous_avg
    """
    avg_o1_alpha_eyesopen = 0.
    avg_o1_theta_eyesopen = 0.
    avg_o1_alpha_eyesclosed = 0.
    avg_o1_theta_eyesclosed = 0.

    avg_o1_alpha_eyesopen =22.8203556961
    avg_o1_alpha_eyesclosed =21.3627777428
    avg_o1_theta_eyesopen =136.277341318
    avg_o1_theta_eyesclosed =171.116188896

    avg_o1_alpha_eyesopen 26.6371945105
    avg_o1_alpha_eyesclosed 51.7758978465
    avg_o1_theta_eyesopen 222.906163651
    avg_o1_theta_eyesclosed 285.299625622

    avg_o1_alpha_eyesopen = 3.56621148132
    avg_o1_alpha_eyesclosed = 4.28481369505
    avg_o1_theta_eyesopen = 1 #22.5621196167
    avg_o1_theta_eyesclosed = 1 #24.6003135031
    """

    # training.train(eyesopen=True)
    # training.train(eyesopen=False)

    training_GUI.vp_start_gui()

    use_abt_trained = dummy.use_abt_trained
    abt_trained = dummy.abt_trained

    # print(use_abt_trained)
    # print(abt_trained)
    # abt_trained = ((avg_o1_alpha_eyesopen/avg_o1_theta_eyesopen) + (avg_o1_alpha_eyesclosed/avg_o1_theta_eyesclosed))/2
    # abt_trained = training.get_average_abt()

    print 'Training Complete.'

    for t in range(6):
        if t % 2 == 0:
            print 'Record Eyes Open'
        else:
            print 'Record Eyes Closed'
        raw_input('Press Enter to continue...')
        start_time = time.time()
        end_time = time.time()

        data_arr = []
        inst_color = None
        inst_direction = None
        with Emotiv(display_output=False, write=True, verbose=True) as headset:
            # while True:
            while end_time - start_time < 60:
                try:
                    packet = headset.dequeue()
                    if packet is not None:
                        # Get the 14 values from emotiv packet
                        sample = [headset.sensors[c]['value'] for c in ch_names]

                        data_arr.append(sample)

                        if len(data_arr) == num_packets:

                            # Get Data for O1 and O2 channel
                            o1_data = [col[chans['O1']] for col in data_arr]
                            o2_data = [col[chans['O2']] for col in data_arr]

                            if len(o1_data) == len(o2_data):
                                for i in range(len(o1_data)):
                                    o1_data[i] = o1_data[i] - 4300
                                    o2_data[i] = o2_data[i] - 4300

                            # Filtering
                            o1_data_filt = butter_bandpass_filter(
                                o1_data, bp_low, bp_high, sample_freq, order=5)
                            o2_data_filt = butter_bandpass_filter(
                                o2_data, bp_low, bp_high, sample_freq, order=5)

                            # Thresholding
                            o1_amplitude = max(o1_data) - min(o1_data)
                            o2_amplitude = max(o2_data) - min(o2_data)

                            # Calculate Alpha Band Power
                            fmin, fmax = eeg_bands['Alpha']
                            ap_o1 = calc(o1_data_filt, fmin, fmax)
                            ap_o2 = calc(o2_data_filt, fmin, fmax)

                            # Calculate Theta Band Power
                            fmin, fmax = eeg_bands['Theta']
                            tp_o1 = calc(o1_data_filt, fmin, fmax)
                            tp_o2 = calc(o2_data_filt, fmin, fmax)

                            # Calculate Alpha / Theta
                            abt_o1 = ap_o1 / tp_o1
                            abt_o2 = ap_o2 / tp_o2
                            abt_avg = (abt_o1 + abt_o2) / 2

                            print '#' * 80
                            print 'O1 Alpha:', ap_o1, '|', 'O1 Theta:', tp_o1
                            print 'O1 Alpha/Theta:', abt_o1
                            print 'O2 Alpha:', ap_o2, '|', 'O2 Theta:', tp_o2
                            print 'O2 Alpha/Theta:', abt_o2
                            print 'Avg Alpha/Theta:', abt_avg, '|', 'Trained Avg Alpha/Theta:', abt_trained

                            if not use_abt_trained:
                                # or abs(o2_amplitude > max_amplitude):
                                if abs(o1_amplitude) > max_amplitude:
                                    print '-*- o1_amp:', o1_amplitude, '|', 'o2_amp:', o2_amplitude
                                    print 'color(yellow)'
                                    # color(yellow)
                                    inst_color = yellow
                                    inst_direction = None
                                # might change to < if value decreases in each successive window (meditative state)
                                elif abt_avg > previous_avg:
                                    print 'color(purple)'
                                    # color(purple)
                                    inst_color = purple
                                    print 'roll(False)'
                                    # roll(False)
                                    inst_direction = False
                                else:
                                    print 'color(green)'
                                    # color(green)
                                    inst_color = green
                                    print 'roll(True)'
                                    # roll(True)
                                    inst_direction = True

                                previous_avg = abt_avg

                            else:
                                # or abs(o2_amplitude > max_amplitude):
                                if abs(o1_amplitude) > max_amplitude:
                                    print '-*- o1_amp:', o1_amplitude, '|', 'o2_amp:', o2_amplitude
                                    print 'color(yellow)'
                                    # color(yellow)
                                    inst_color = yellow
                                    inst_direction = None
                                elif abt_avg > abt_trained:
                                    print 'color(purple)'
                                    # color(purple)
                                    inst_color = purple
                                    print 'roll(False)'
                                    # roll(False)
                                    inst_direction = False
                                else:
                                    print 'color(green)'
                                    # color(green)
                                    inst_color = green
                                    print 'roll(True)'
                                    # roll(True)
                                    inst_direction = True

                            data_arr = []
                            # now send it and wait for a bit
                            # outlet.push_sample(power_values_delta)
                            time.sleep(1.0 / sample_freq)

                        # constant rolling, only updated when new packet group is calculated
                        # every 16th packet, to give time for rolling
                        if (len(data_arr) + 1) % 16 == 0:
                            if inst_color is not None:
                                print "color(%s)" % inst_color
                                color(inst_color)
                            if inst_direction is not None:
                                print "roll(%s)" % inst_direction
                                roll(inst_direction)
                    # else:
                        # break
                    end_time = time.time()
                except KeyboardInterrupt:
                    break

    bb.disconnect()
    print "Done."
    sys.exit(0)


if __name__ == "__main__":
    main()
