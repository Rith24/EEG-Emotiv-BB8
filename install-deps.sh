#!/bin/bash

set -e
set -x

# Update
sudo apt update
sudo apt upgrade

# Install packages
sudo apt install python python-pip bpython ipython libglib2.0-dev build-essential cmake qt5-default libboost-all-dev libudev-dev libusb-1.0-0-dev libfox-1.6-dev autotools-dev autoconf automake libtool python-dev python-opengl libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf libfreetype6-dev
# Install Python Packages
sudo python -m pip install -U bluepy
sudo python -m pip install -U pycrypto
sudo python -m pip install -U pytest
sudo python -m pip install -U future
sudo python -m pip install -U numpy
sudo python -m pip install -U scipy
sudo python -m pip install -U mne
sudo python -m pip install -U pygame

mkdir -p ~/Documents/GitHub

# Clone Git Repositories
cd ~/Documents/GitHub/
git clone --recursive https://github.com/sccn/labstreaminglayer.git
git clone https://github.com/signal11/hidapi.git
git clone https://gitlab.com/NF6X_Archive/pyhidapi.git
git clone https://github.com/openyou/emokit.git

# labstreaminglayer LSL (shared library)
cd ~/Documents/GitHub/labstreaminglayer/
mkdir build
cd build
cmake ..
cmake --build . --config Release --target install
cd install/LSL
sudo cp include/* /usr/include/
sudo cp lib/* /usr/lib/
sudo cp share/* /usr/share/
cd lib/
cp liblsl64.so.1.13.0 ~/.local/lib/python2.7/site-packages/pylsl/
cd ~/.local/lib/python2.7/site-packages/pylsl
cp liblsl64.so.1.13.0 liblsl64.so

# PyLSL
cd ~/Documents/GitHub/labstreaminglayer/LSL/liblsl-Python/
pip install .

# hidapi
cd ~/Documents/GitHub/hidapi/
./bootstrap
./configure
make
sudo make install

# pyhihapi
cd ~/Documents/GitHub/pyhidapi/
sudo ./setup.py install

# emokit
cd ~/Documents/GitHub/emokit/python/
python -m pytest tests/test_emokit.py tests/test_util.py
sudo python setup.py install
