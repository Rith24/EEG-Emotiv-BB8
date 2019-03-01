import sys, signal, time
import numpy as np
import scipy
from scipy.signal import butter, lfilter, periodogram
# from pylsl import StreamInfo, StreamOutlet
# from emokit.emotiv import Emotiv
from emoemu import Emotiv
from bb8 import BB8
import training

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
             AF4=11,
             FC6=12,
             F4=13)

num_packets = 64
bp_low = 1.
bp_high = 50.
thresh_low = -100
thresh_high = 100

MAC_ADDR = 'F2:D8:37:4B:CE:F1'
bb = BB8(MAC_ADDR)
bb.cmd(0x02, 0x21, [0xff])
heading = 0
angle = 15
red = [0xff, 0x00, 0x00, 0]
green = [0x00, 0xff, 0x00, 0]
terminate = False


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
    bb.cmd(0x02, 0x20, c)


def signal_handling(signum, frame):
    global terminate
    terminate = True


def main():

    training.train(eyesopen=True)
    training.train(eyesopen=False)

    data_arr = []
    i = 0
    with Emotiv(display_output=False, verbose=True) as headset:
        while True:
            packet = headset.dequeue()
            if packet is not None:
                # Get the 14 values from emotiv packet
                sample = [headset.sensors[c]['value'] for c in chans]

                data_arr.append(sample)

                if len(data_arr) != 0 and len(data_arr) % num_packets == 0:

                    # Get Data for O1 and O2 channel
                    o1_data = [col[chans['O1']] for col in data_arr]
                    # o2_data = [col[chans['O2']] for col in data_arr]

                    # Filtering
                    # o1_data_filt = butter_bandpass_filter(o1_data, bp_low, bp_high, sample_freq, order=5)
                    # o2_data_filt = butter_bandpass_filter(o2_data, bp_low, bp_high, sample_freq, order=5)

                    # Thresholding
                    # o1_amplitude = max(o1_data[i-num_packets+1:i]) - min(o1_data[i-num_packets+1:i])
                    # o2_amplitude = max(o2_data[i-num_packets+1:i]) - min(o2_data[i-num_packets+1:i])

                    # Calculate Alpha Band Power
                    fmin, fmax = eeg_bands['Alpha']
                    a_o1 = calc(o1_data, fmin, fmax)
                    # a_o2 = calc(o2_data, fmin, fmax)

                    # Calculate Theta Band Power
                    fmin, fmax = eeg_bands['Theta']
                    t_o1 = calc(o1_data, fmin, fmax)
                    # t_o2 = calc(o2_data, fmin, fmax)

                    # Calculate Alpha / Theta
                    abt_o1 = a_o1 / t_o1
                    # abt_o2 = a_o2 / t_o2

                    average_abt = training.get_average_abt()

                    print 'O1 Alpha/Theta:', abt_o1, '|', 'Average Alpha/Theta:', average_abt

                    if abt_o1 > average_abt:
                        print 'color(red)'
                        color(red)
                        print 'roll(False)'
                        roll(False)
                    else:
                        print 'color(green)'
                        color(green)
                        print 'roll(True)'
                        roll(True)

                    # now send it and wait for a bit
                    # outlet.push_sample(power_values_delta)
                    time.sleep(1.0 / sample_freq)
                i += 1

                # Graceful shutdown on ^C
                if terminate:
                    print "\nDisconnecting..."
                    break

        bb.disconnect()
        print "Done."
        sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handling)
    main()
