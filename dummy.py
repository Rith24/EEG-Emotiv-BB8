# this file exists to circumvent the problem of double importing to change global variables from another file.
# so this "Dummy" file serves as an intermediary storage file; values from training_GUI.py are stored here and accessed
# from emotiv_lsl_fft.py

global use_abt_trained
global abt_trained
