import numpy as np  #some obvious imports
import matplotlib.pyplot as plt
import complexity

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
zmean512 = 1.7244838130920948

zerr08 =  0.5500053274238199
zerr16 = 0.5251204893169296
zerr32 = 0.5081624150270349
zerr64 = 0.49374888616642454
zerr128 =  0.4855043704216542
zerr256 = 0.47974050911754534
zerr512 = 0.47512723835298937




"""
TASK 2D


"""

A = [8,16,32,64,128,256,512]


B = []
def theoreticalcross(zmean,L):
    A = (zmean*(L**2)/2)*(1 + (1/L))
    #B = ((zerr*(L**2)/2)*(1 + (1/L))
    return A


plt.scatter(A, [theoreticalcross(zmean08,8), theoreticalcross(zmean16,16), theoreticalcross(zmean32,32), theoreticalcross(zmean64,64),
theoreticalcross(zmean128, 128), theoreticalcross(zmean256,256), theoreticalcross(zmean512,512)], s = 30, marker = 'x')
plt.scatter(A, [cross08,cross16,cross32,cross64,cross128,cross256,cross512], s = 30, marker = 'x')
plt.show()
