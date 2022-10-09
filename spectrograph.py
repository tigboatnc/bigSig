# For this coding assignment you won’t be able to use a Jupyter notebook (ipynb) because we’ll be making 
# a real-time app, so create a regular .py file and you can run it with “python yourapp.py” in a terminal.  
# Starting from Assignment 2 Part 3 (i.e., the spectrogram code we’ve been working on for several weeks 
# now), if you haven’t already done so, add proper x/y axis labels to your spectrogram.  Your x-axis should 
# have center_frequency in the center, center_frequency – sample_rate/2 on the left, and then 
# center_frequency + sample_rate/2 on the right (if that doesn’t make any sense, email me and we can 
# chat about what it means).  Y-axis is in time, so whether your first sample is at the bottom or top, that 
# should start at 0, and remember that each row corresponds to fft_size * sample_period time, and 
# sample_period is just 1/sample_rate.  For units please use milliseconds and MHz.  If you don’t know 
# whether the first sample is at the top or bottom, just set it to a really big number and see whether the 
# top row or bottom row gets stronger.  
# The last task for you to do, one you finished the above, is to make your spectrogram auto-refresh, so 
# that you can see it changing over time.  There are several ways to do this in matplotlib, one is shown 
# below, but feel free to Google around to find other ways.  

# For your submission, 
    # set center_frequency to 100 MHz (the FM band), 
    # sample_rate to 20 MHz,
    #  and plug 
# in your antenna, then take a screenshot of your spectrogram and submit it as a separate image in 
# addition to your code.



import numpy as np
import adi
from matplotlib import pyplot as plt
import time 

sample_rate = 600e5 # Hz.  This is the “Fs” we always talk about
center_freq = 200e6 # Hz.  Aka Carrier Frequency
num_samps = 2000 # samples returned per call to rx()

sdr = adi.Pluto('ip:192.168.2.1') 
sdr.gain_control_mode_chan0 = 'manual' # turns off automatic gain control
sdr.rx_hardwaregain_chan0 = 70.0 # sets the gain, in dB. it goes from 0 to 74.5 dB
sdr.rx_lo = int(center_freq)
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate) # filter width, set the same as sample rate for now
sdr.rx_buffer_size = num_samps 


BIG_PICTURE = np.zeros((400,400))
# extent = [sample_rate/-2,sample_rate/2,0,400]

for i in range(1000):

    samples = sdr.rx()
    # print(samples)

    y1_ = samples.reshape((5,400))
    N = y1_.shape[1]
    f = np.arange(sample_rate/-2, sample_rate/2, sample_rate/num_samps)
    calculated_FFT = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(y1_)))**2)

    partials = BIG_PICTURE[:400-5]
    BIG_PICTURE = np.vstack((calculated_FFT,partials))

    
    # vanilla
    # plt.imshow(BIG_PICTURE)

    # only aspect
    # plt.imshow(BIG_PICTURE,aspect='auto')

    # original F 
    # plt.imshow(BIG_PICTURE,extent=[sample_rate/-2, sample_rate/2,0,1])


    plt.imshow(BIG_PICTURE,extent=[sample_rate/-2, sample_rate/2,0,1],aspect='auto',interpolation=None)






    # plt.xticks([1,2,3,4,5]) 
    # plt.set_xticks(f)
    plt.draw()
    
    plt.pause(0.001)
    plt.clf()
    # time.sleep(5)
    print('sleeping')