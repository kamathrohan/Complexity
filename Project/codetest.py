import numpy as np  #some obvious imports
import matplotlib.pyplot as plt

size04 = np.genfromtxt("100000405.csv")
size08 = np.genfromtxt("100000805.csv")
size16 = np.genfromtxt("100001605.csv")
size32 = np.genfromtxt("100003205.csv")
size64 = np.genfromtxt("100006405.csv")
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
#zmean1024 =

"""

    TASK 2C


"""

xaxis1 = np.arange(10000)
xaxis2 = np.arange(70000)
xaxis3 = np.arange(500000)
xaxis4= np.arange(1000000)

scarr04 = np.divide(size04,4)
scarrx04 = np.divide(xaxis1,4**2)
scarr08 = np.divide(size08,8)
scarrx08 = np.divide(xaxis1,8**2)
scarr16 = np.divide(size16,16)
scarrx16 = np.divide(xaxis1,16**2)
scarr32 = np.divide(size32,32)
scarrx32 = np.divide(xaxis1,32**2)
scarr64 = np.divide(size64,64)
scarrx64 = np.divide(xaxis1,64**2)
scarr128 = np.divide(size128,128)
scarrx128 = np.divide(xaxis2,(128**2))
scarr256 = np.divide(size256,256)
scarrx256 = np.divide(xaxis2,256**2)
scarr512 = np.divide(size512,512)
scarrx512 = np.divide(xaxis3,512**2)
scarr1024 = np.divide(size1024,1024)
scarrx1024 = np.divide(xaxis4,1024**2)
"""
#plt.plot(scarrx04,scarr04)
plt.plot(scarrx08,scarr08, label = "L = 8")
plt.plot(scarrx16,scarr16, label = "L = 16")
plt.plot(scarrx32,scarr32, label = "L = 32")
plt.plot(scarrx64,scarr64, label = "L = 64")
plt.plot(scarrx128,scarr128, label = "L =128")
plt.plot(scarrx256,scarr256, label = "L = 264")
plt.plot(scarrx512,scarr512, label = "L = 512")
plt.plot(scarrx1024,scarr1024, label = "L = 1024")
plt.xlim([0,3])
plt.legend()
plt.show()


"""


"""
mean = np.average(size256[56138:])
stddv = np.std(size256[56138:])
zeeav = mean/256
zeestddv = stddv/256
print("Mean = ",mean)
print("Stddv = ", stddv)
print("<z> =", zeeav)
print("sigmaz =", zeestddv)


"""


"""
plt.scatter([4,8,16,32,64,128,256],[cross04,cross08,cross16,cross32,cross64,cross128,cross256])
plt.show()






size512 = np.genfromtxt("5000005121.csv")
plt.plot(size512)
plt.show()









"""


def heightextractor(heightarray,tcross):
    tcrossint = np.int(tcross)
    A = heightarray[tcrossint:]
    print(np.average(A))
    print(np.std(A))
    return


heightextractor(size1024,cross1024)