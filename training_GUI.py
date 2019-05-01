# import sys
import training
# from functools import partial

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

import training_GUI_support

# global eyes_open_collected
# global eyes_closed_collected
eyes_open_collected = False
eyes_closed_collected = False


def hello():
    print("hello")


def hi():
    print("Hi")


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    training_GUI_support.set_Tk_var()
    top = Toplevel1(root)
    training_GUI_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    training_GUI_support.set_Tk_var()
    top = Toplevel1(w)
    training_GUI_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:

    def eyes_open(self):
        print(self.eyes_open_collected)
        if self.eyes_open_collected == False:
            self.eyes_open_collected = True
            self.Label1.configure(text='''Complete''')
        else:
            self.eyes_open_collected = True
            self.eyes_closed_collected = False
            self.Label1.configure(text='''Complete''')
            self.Label2.configure(text='''Train (Eyes Closed)''')

    def eyes_closed(self):
        print(self.eyes_closed_collected)
        if self.eyes_closed_collected == False:
            self.eyes_closed_collected = True
            self.Label2.configure(text='''Complete''')
        else:
            self.eyes_closed_collected = True
            self.eyes_open_collected = False
            self.Label2.configure(text='''Complete''')
            self.Label1.configure(text='''Train (Eyes Open)''')

    def check_training_completion(self):
        if (self.eyes_open_collected == True) and (self.eyes_closed_collected == True):
            # training_GUI.support.abt_trained = training.get_average_abt()
            training_GUI_support.abt_trained = training.get_average_abt()
            self.Entry1.insert(0, training_GUI_support.abt_trained)
            print("complete")
        else:
            print("not complete")

    def __init__(self, top=None):
        global abt_trained
        global use_abt_trained
        self.eyes_open_collected = eyes_open_collected
        self.eyes_closed_collected = eyes_closed_collected

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+695+256")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.333, rely=0.356, height=42, width=53)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        # self.Button1.configure(command=partial(training.train, eyesopen=True))
        self.Button1.configure(
            command=lambda: [training.train(eyesopen=True), self.eyes_open(), self.check_training_completion()])
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Train''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.333, rely=0.489, height=42, width=53)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        # self.Button2.configure(command=partial(training.train(eyesopen=False))
        self.Button2.configure(
            command=lambda: [training.train(eyesopen=False), self.eyes_closed(), self.check_training_completion()])
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Train''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.033, rely=0.378, height=31, width=143)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Train (Eyes Open)''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.033, rely=0.511, height=31, width=153)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Train (Eyes Closed)''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.05, rely=0.711, height=21, width=124)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Set abt_trained''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.3, rely=0.711, height=26, relwidth=0.29)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.183, rely=0.044, relheight=0.167
                          , relwidth=0.608)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=365)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.219, rely=0.267, height=31, width=207)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''TRAINING MODULE''')

        self.Radiobutton1 = tk.Radiobutton(top)
        self.Radiobutton1.place(relx=0.65, rely=0.311, relheight=0.193
                                , relwidth=0.26)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(command=training_GUI_support.setComparisonMode)
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Use trained abt''')
        self.Radiobutton1.configure(value="1")
        self.Radiobutton1.configure(variable=training_GUI_support.choice)

        self.Radiobutton2 = tk.Radiobutton(top)
        self.Radiobutton2.place(relx=0.65, rely=0.467, relheight=0.138
                                , relwidth=0.308)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(command=training_GUI_support.setComparisonMode)
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Use instantaneous abt comparison''')
        self.Radiobutton2.configure(value="2")
        self.Radiobutton2.configure(variable=training_GUI_support.choice)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.417, rely=0.844, height=42, width=128)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=lambda: [
            training_GUI_support.return_to_main_program()])
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Finish Training''')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.667, rely=0.711, height=32, width=58)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=training_GUI_support.processEntry)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Enter''')
        self.Button4.configure(width=58)

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.333, rely=0.222, height=42, width=47)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Test''')
        self.Button5.configure(command=training_GUI_support.test_connection)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.017, rely=0.222, height=41, width=147)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''BB8 Connection''')
        self.Label5.configure(width=147)



if __name__ == '__main__':
    vp_start_gui()
