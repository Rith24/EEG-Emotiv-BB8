#!/bin/bash

# Install packages
sudo apt install python python-pip bpython ipython libglib2.0-dev build-essential cmake qt5-default libboost-all-dev libudev-dev libusb-1.0-0-dev libfox-1.6-dev autotools-dev autoconf automake libtool
# Install Python Packages
sudo pip install -U bluepy
pip install -U pygame pycrypto pytest future numpy scipy mne

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
