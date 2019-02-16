import numpy as np  #some obvious imports
import matplotlib.pyplot as plt


""" 

The following block of code analyses CSV files for height arrays generated after running smoothheight 
and cross over times in the complexity.py program.
"""
size04 = np.genfromtxt("700000405.csv")
size08 = np.genfromtxt("700000805.csv")
size16 = np.genfromtxt("700001605.csv")
size32 = np.genfromtxt("700003205.csv")
size64 = np.genfromtxt("700006405.csv")
size128 = np.genfromtxt("7000012805.csv")
size256 = np.genfromtxt("7000025605.csv")
size512 = np.genfromtxt("5000005121.csv")
size1024 = np.genfromtxt("100000010241.csv")

cross04 = 16.0
cross08 = 54.2
cross16 = 218.4
cross32 = 860.0
cross64 = 3468.8
cross128 = 13902.25
cross256 = 56137.75
cross512 = 223300
cross1024 = 904140

zmean08 = 1.6207591754650577
zmean16 = 1.6569854820570493
zmean32 = 1.6832626654995078
zmean64 = 1.701014392895422
zmean128 = 1.7130958601465291
zmean256 = 1.719254132250036
zmean512 = 1.72448
zmean1024 = 1.7278125


"""

plt.plot(size04, label = "L = 4")
plt.plot(size08, label = "L = 8")
plt.plot(size16, label = "L = 16")
plt.plot(size32, label = "L = 32")
plt.plot(size64, label = "L = 64")
plt.plot(size128, label = "L =128")
plt.plot(size256, label = "L = 256")
plt.plot(size512, label = "L = 512")
plt.plot(size1024, label = "L = 1024")
plt.xlabel("log(Grains (t))")
plt.ylabel("log(Height (H))")
plt.title("Evolution of height as a function of time for different system sizes")
plt.legend()
plt.grid()
#plt.savefig("HeightVTimeloglog.png")
plt.show()
"""


"""
plt.loglog(size04, label = "L = 4")
plt.loglog(size08, label = "L = 8")
plt.loglog(size16, label = "L = 16")
plt.loglog(size32, label = "L = 32")
plt.loglog(size64, label = "L = 64")
plt.loglog(size128, label = "L =128")
plt.loglog(size256, label = "L = 256")
plt.loglog(size512, label = "L = 512")
plt.loglog(size1024, label = "L = 1024")
plt.xlabel("log(Grains (t))")
plt.ylabel("log(Height (H))")
plt.title("Evolution of height as a function of time for different system sizes")
plt.legend()
plt.grid()
plt.savefig("HeightVTimeloglog.png")
plt.show()


"""



"""
    TASK 2C

"""


""" This block of code generates 4 ranges for 4 x axes, and rescales them for system sizes"""
xaxis1 = np.arange(10000)
xaxis2 = np.arange(70000)
xaxis3 = np.arange(500000)
xaxis4= np.arange(1000000)
scarrx04 = np.divide(xaxis2,4**2)
scarrx08 = np.divide(xaxis2,8**2)
scarrx16 = np.divide(xaxis2,16**2)
scarrx32 = np.divide(xaxis2,32**2)
scarrx64 = np.divide(xaxis2,64**2)
scarrx128 = np.divide(xaxis2,(128**2))
scarrx256 = np.divide(xaxis2,256**2)
scarrx512 = np.divide(xaxis3,512**2)
scarrx1024 = np.divide(xaxis4,1024**2)

""" This block of code rescales the heights"""
scarr04 = np.divide(size04,4)
scarr08 = np.divide(size08,8)
scarr16 = np.divide(size16,16)
scarr32 = np.divide(size32,32)
scarr64 = np.divide(size64,64)
scarr128 = np.divide(size128,128)
scarr256 = np.divide(size256,256)
scarr512 = np.divide(size512,512)
scarr1024 = np.divide(size1024,1024)

""" This block of code plots the rescaled axis for a data collapse"""

"""

plt.plot(scarrx04[1:],scarr04[1:], label = "L = 4")
plt.plot(scarrx08[1:],scarr08[1:], label = "L = 8")
plt.plot(scarrx16[1:],scarr16[1:], label = "L = 16")
plt.plot(scarrx32[1:],scarr32[1:], label = "L = 32")
plt.plot(scarrx64[1:],scarr64[1:], label = "L = 64")
plt.plot(scarrx128[1:],scarr128[1:], label = "L =128")
plt.plot(scarrx256[1:],scarr256[1:], label = "L = 256")
plt.plot(scarrx512[1:],scarr512[1:], label = "L = 512")
plt.plot(scarrx1024[1:],scarr1024[1:], label = "L = 1024")
plt.xlim([0,3])
plt.xlabel("t/L^2")
plt.ylabel("h/L")
plt.title("Data Collapse of height")
plt.legend()
plt.grid()
plt.savefig("datacollapse.png")
plt.show()

"""






"""This block of code plots the data collapse on a log log axis"""

"""

plt.loglog(scarrx04[1:],scarr04[1:], label = "L = 4")
plt.loglog(scarrx08[1:],scarr08[1:], label = "L = 8")
plt.loglog(scarrx16[1:],scarr16[1:], label = "L = 16")
plt.loglog(scarrx32[1:],scarr32[1:], label = "L = 32")
plt.loglog(scarrx64[1:],scarr64[1:], label = "L = 64")
plt.loglog(scarrx128[1:],scarr128[1:], label = "L =128")
plt.loglog(scarrx256[1:],scarr256[1:], label = "L = 256")
plt.loglog(scarrx512[1:],scarr512[1:], label = "L = 512")
plt.loglog(scarrx1024[1:],scarr1024[1:], label = "L = 1024")
plt.xlabel("t/L^2")
plt.ylabel("h/L")
plt.title("Data Collapse of height - Log-Log")
plt.legend()
plt.grid()
plt.savefig("datacollapse-loglog.png")
plt.show()


"""

