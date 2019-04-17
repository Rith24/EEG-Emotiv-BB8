import dummy
import sys

# import training
# import emotiv_lsl_fft


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


# def num1():
#   global num1
#
# num1 += 1

# def num2():
#   global num2
#  num2 = 0

# def avg():
#   avg = (num1+num2)/2
#  return avg
abt_trained = 0
use_abt_trained = True

def set_Tk_var():
    global choice
    choice = tk.StringVar()


def processEntry():
    global abt_trained
    data = w.Entry1.get()
    abt_trained = float(data)
    print(abt_trained + 1)
    print('training_GUI_support.processEntry')
    sys.stdout.flush()


def return_to_main_program():
    global abt_trained
    global use_abt_trained
    dummy.use_abt_trained = use_abt_trained
    dummy.abt_trained = abt_trained
    # test.use_abt_trained = use_abt_trained
    # test.abt_trained = abt_trained
    # print(test.use_abt_trained)
    # print(test.abt_trained)
    # emotiv_lsl_fft.use_abt_trained = use_abt_trained
    # emotiv_lsl_fft.abt_trained = abt_trained
    print('training_GUI_support.return_to_main_program')
    destroy_window()
    sys.stdout.flush()


def setComparisonMode():
    global use_abt_trained
    if choice.get() == "1":
        use_abt_trained = True

    else:
        use_abt_trained = False

    print('training_GUI_support.setComparisonMode')
    print(use_abt_trained)
    sys.stdout.flush()


def traineyesclosed():
    training.train(eyesopen=False)
    print('training_GUI_support.traineyesclosed')
    sys.stdout.flush()


def traineyesopen():
    training.train(eyesopen=True)
    print('training_GUI_support.traineyesopen')
    sys.stdout.flush()


# def calc_abt_trained():
#     abt_trained = training.get_average_abt()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import training_GUI

    training_GUI.vp_start_gui()
