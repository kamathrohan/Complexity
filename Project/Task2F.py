import matplotlib.pyplot as plt

import complexity
import numpy as np


complexity.heightextractor()

hstd08 = 0.4302153945559708
hstd16 = 0.5023506279317981
hstd32 = 0.6053027376264722
hstd64 = 0.7282721011499772
hstd128 = 0.8418874506605555
hstd256 = 1.073128838461994
hstd512 = 2.78844487296973
hstd1024 = 3.208062394395017

plt.scatter([8,16,32,64,128,256,512,1024],[hstd08,hstd16,hstd32,hstd64,hstd128,hstd256,hstd512,hstd1024])
plt.show( )
