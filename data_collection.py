import numpy as np
import adi
from matplotlib import pyplot as plt
import time 
from tqdm import tqdm 


sample_rate = 40e6 # Hz.  This is the “Fs” we always talk about
center_freq = 433e6 # Hz.  Aka Carrier Frequency
num_samps = 160000 # samples returned per call to rx()
gain = 70.0

sdr = adi.Pluto('ip:192.168.2.1') 
sdr.gain_control_mode_chan0 = 'manual' # turns off automatic gain control
sdr.rx_hardwaregain_chan0 = gain # sets the gain, in dB. it goes from 0 to 74.5 dB
sdr.rx_lo = int(center_freq)
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate) # filter width, set the same as sample rate for now
sdr.rx_buffer_size = num_samps 


# BIG_PICTURE = np.zeros((400,400))

for i in tqdm(range(200)):
    samples = sdr.rx()
    with open(f'dataset/{int(gain)}_{i}.npy', 'wb') as f:
        np.save(f, samples)