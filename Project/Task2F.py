import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit



hstd08 = 0.4302153945559708
hstd16 = 0.5023506279317981
hstd32 = 0.6053027376264722
hstd64 = 0.7282721011499772
hstd128 = 0.8418874506605555
hstd256 = 1.073128838461994
hstd512 = 1.2463902121512476
hstd1024 = 1.4370870167462262
L = [8,16,32,64,128,256,512,1024]
stdarray = [hstd08,hstd16,hstd32,hstd64,hstd128,hstd256,hstd512,hstd1024]

zmean08 = 1.6207591754650577
zmean16 = 1.6569854820570493
zmean32 = 1.6832626654995078
zmean64 = 1.701014392895422
zmean128 = 1.7130958601465291
zmean256 = 1.719254132250036
zmean512 = 1.7244838130920948
zmean1024 = 1.7310812512093

zerr08 =  0.5500053274238199
zerr16 = 0.5251204893169296
zerr32 = 0.5081624150270349
zerr64 = 0.49374888616642454
zerr128 =  0.4855043704216542
zerr256 = 0.47974050911754534
zerr512 = 0.47512723835298937


def expon(x,a,b):
    return (a* (x**b))

popt, pcov = curve_fit(expon,L, stdarray )

print(popt)
perr = np.sqrt(np.diag(pcov))
print(perr)

fig = plt.figure()
ax = plt.gca()
ax.scatter(L,stdarray, label = "Standard Deviation values")
ax.plot(L, [expon(i,popt[0],popt[1]) for i in L], label = "Fit")
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel("log(L)")
plt.ylabel("log(Std)")
plt.title("Variation of standard deviation of height with system size")
plt.grid()
plt.savefig("Hstd.png")
plt.show()


"""

plt.scatter([8,16,32,64,128,256,512,1024],[zmean08,zmean16,zmean32,zmean64,zmean128,zmean256,zmean512,zmean1024])
plt.xlabel("L")
plt.ylabel("<z>")
plt.title("Variation of <z> with system size")
plt.grid()
plt.show()
"""
