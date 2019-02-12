import numpy as np  #some obvious imports
import matplotlib.pyplot as plt

size04 = np.genfromtxt("100000405.csv")
size08 = np.genfromtxt("100000805.csv")
size16 = np.genfromtxt("100001605.csv")
size32 = np.genfromtxt("100003205.csv")
size64 = np.genfromtxt("100006405.csv")
size128 = np.genfromtxt("7000012805.csv")
size256 = np.genfromtxt("7000025605.csv")




xaxis1 = np.arange(10000)
xaxis2 = np.arange(70000)

cross04 = 16.0
cross08 = 54.2
cross16 = 218.4
cross32 = 860.0
cross64 = 3468.8
cross128 = 13902.25
cross256 = 56137.75


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

"""
#plt.plot(scarrx04,scarr04)
plt.plot(scarrx08,scarr08, label = "L = 8")
plt.plot(scarrx16,scarr16, label = "L = 16")
plt.plot(scarrx32,scarr32, label = "L = 32")
plt.plot(scarrx64,scarr64, label = "L = 64")
plt.plot(scarrx128,scarr128, label = "L =128")
plt.plot(scarrx256,scarr256, label = "L = 264")
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



def heightextractor(heightarray,tcross):
    tcrossint = np.int(tcross)
    A = heightarray[tcrossint:]
    print(np.average(A))
    print(np.std(A))


heightextractor(size256,cross256)


"""
size512 = np.genfromtxt("5000005121.csv")
plt.plot(size512)
plt.show()

def theoreticalcross(zmean,L):
    A = (zmean*(L**2)/2)*(1 + (1/L))
    return A





A = [4,8,16,32,64,128,256]


B = []

for i in A:
    B.append(theoreticalcross(1.73,i))

plt.scatter(A,B)
plt.scatter(A, [cross04,cross08,cross16,cross32,cross64,cross128,cross256])
plt.show()
