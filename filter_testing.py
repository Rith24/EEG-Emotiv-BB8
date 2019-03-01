import scipy
from scipy import signal
from scipy.signal import butter, lfilter

num_packets = 64
stream_name = 'BioSemi'
stream_type = 'EEG'
num_channel = 14
sample_freq = 128
headset_uid = 'myuid34234'
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
             AC4=11,
             FC6=12,
             F4=13)


bp_low = 1.
bp_high = 50.


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


data_file = open('trimmed_emotiv_values_2019-02-05_18-32-30.371051.csv', 'r')
data_arr = []
i = 0
for line in data_file:

    data_arr.append(map(float, line.strip().split(',')))

    if len(data_arr) !=0 and len(data_arr) % num_packets == 0:

        # Get Data for O1 and O2 channel
        o1_data = [col[chans['O1']] for col in data_arr]
        o2_data = [col[chans['O2']] for col in data_arr]

      #  o1_data = o1_data 4100
      #  o2_data = 4100

        for i in range(len(o1_data)):
            o1_data[i] = o1_data[i] - 4100
            if len(o1_data) == len(o2_data):
                o2_data[i] = o2_data[i] - 4100

        # Filtering
        o1_data_filt = butter_bandpass_filter(o1_data, bp_low, bp_high, sample_freq, order=5)
        o2_data_filt = butter_bandpass_filter(o2_data, bp_low, bp_high, sample_freq, order=5)

        # Thresholding
        # o1_amplitude = max(o1_data[i-num_packets+1:i]) - min(o1_data[i-num_packets+1:i])
        # o2_amplitude = max(o2_data[i-num_packets+1:i]) - min(o2_data[i-num_packets+1:i])

        # Calculate Alpha Band Power for O1 and O2
        fmin, fmax = eeg_bands['Theta']
        p_o1 = calc(o1_data_filt, fmin, fmax)
        p_o2 = calc(o2_data_filt, fmin, fmax)

        # print 'O1 Alpha Power:', p_o1, '|', 'O2 Alpha Power:', p_o2

        # now send it and wait for a bit
        # outlet.push_sample(power_values_delta)
        # time.sleep(1.0 / sample_freq)

    i += 1

data_file.close()