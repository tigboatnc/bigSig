# bigSig : Machine Learning + SDR Experiments 



## Data 

#### Self Collected  

Done using [data_collection.py](./data_collection.py) and PLUTOSDR. 
__Sampling Parameters__

``` python
sample_rate = 40e6
center_freq = 433e6
num_samps = 40000 
```
#### Online Datasets 

> planned

## Trials and Tribulations 

### method 1 - Manual AWGN Noise Imputation -> Convoltion Denoising AutoEncoder
Manually adding AWGN noise to PlutoSDR signals in python as a substitute for a real world noisy signal 
- [Reference for Noise Addition](https://pysdr.org/content/noise.html)<br/>
- Data collected with 70 gain. 
- [Preprocessing Notebook](./m1_preprocessing.ipynb)<br/>
- [AutoEncoder Training Notebook (Colab Pro GPU + High RAM Instance)](./m1_train_colab.ipynb) <br/>

#### Outputs `run 1 : small poc with 190 training sample and 10 test samples`
![op1](./assets/m1_op1.png)



#### Conclusions? 
Idk yet but 
- the model output does make the difference between the floor and signal more apparent 
- the model sometimes tries to create signals on the right (bias due to training as samples similar looking)
- [ ] Try on totally random signals on which no training done (maybe different encoing even)
