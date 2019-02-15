import matplotlib.pyplot as plt
import numpy as np

hstd08 = 0.4302153945559708
hstd16 = 0.5023506279317981
hstd32 = 0.6053027376264722
hstd64 = 0.7282721011499772
hstd128 = 0.8418874506605555
hstd256 = 1.073128838461994
hstd512 = 1.2463902121512476
hstd1024 = 1.4370870167462262

fig = plt.figure()
ax = plt.gca()
ax.scatter([8,16,32,64,128,256,512,1024],[hstd08,hstd16,hstd32,hstd64,hstd128,hstd256,hstd512,hstd1024])
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel("log(L)")
plt.ylabel("log(Std)")
plt.title("Variation of standard deviation of height with system size")
plt.show()
