import numpy as np
import matplotlib.pyplot as plt
import logbin230119 as logbin
import pandas as pd
import complexity


"""
A = complexity.avalsize(10000,8)
np.savetxt('avalsize100008.txt',A)

A = complexity.avalsize(10000,16)
np.savetxt('avalsize1000016.txt',A)

A = complexity.avalsize(10000,32)
np.savetxt('avalsize1000032.txt',A)

A = complexity.avalsize(10000,64)
np.savetxt('avalsize1000064.txt',A)

A = complexity.avalsize(50000,128)
np.savetxt('avalsize100000256.txt',A)

A = complexity.avalsize(500000,512)
np.savetxt('avalsize500000512.txt',A)

A = complexity.avalsize(1000000,1024)
np.savetxt('avalsize10000001024.txt',A)


"""



aval08 = np.genfromtxt("avalsize100008.txt")
aval08 = aval08.astype(int)

aval16 = np.genfromtxt("avalsize1000016.txt")
aval16 = aval16.astype(int)

aval32 = np.genfromtxt("avalsize1000032.txt")
aval32 = aval32.astype(int)

aval64 = np.genfromtxt("avalsize1000064.txt")
aval64 = aval64.astype(int)


aval128 = np.genfromtxt("avalsize50000128.txt")
aval128 = aval128.astype(int)

aval256 = np.genfromtxt("avalsize100000256.txt")
aval256 = aval256.astype(int)

aval512 = np.genfromtxt("avalsize500000512.txt")
aval512 = aval512.astype(int)



aval1024 = np.genfromtxt("avalsize10000001024.txt")
aval1024 = aval1024.astype(int)


def plot(scale):
    x, y = logbin.logbin(aval08, scale = scale)
    plt.loglog(x,y, label = 'L = 8')

    x, y = logbin.logbin(aval16, scale = 1.3)
    plt.loglog(x,y, label = 'L = 16')

    x, y = logbin.logbin(aval32, scale = scale)
    plt.loglog(x,y, label = 'L = 32')

    x, y = logbin.logbin(aval64, scale = scale)
    plt.loglog(x,y, label = 'L = 64')

    x, y = logbin.logbin(aval128, scale = scale)
    plt.loglog(x,y, label = 'L = 128')



    x, y = logbin.logbin(aval256, scale = scale)
    plt.loglog(x,y, label = 'L = 256')



    x, y = logbin.logbin(aval512, scale = scale)
    plt.loglog(x,y, label = 'L = 512')


    x, y = logbin.logbin(aval1024, scale = scale)
    plt.loglog(x,y, label = 'L = 1024')
    plt.legend()
    plt.show()
    return

#plot(1.3)

def probability(array):
    s = pd.Series(array)
    probability = (s.groupby(s).transform('count') / len(s)).values
    return probability
avalarray = [aval08,aval16,aval32,aval64,aval128,aval256,aval512,aval1024]
lengtharrays = [8,16,32,64,128,256,512,1024]

def collapse(D, tau,arrayofarrays, lengtharrays):
    for i in range(len(arrayofarrays)):
        x, y = logbin.logbin(arrayofarrays[i], scale = 1.4)
        for j in range(len(x)):
            y[j] = y[j]*(x[j]**tau)
        xscaled = np.divide(x,lengtharrays[i]**D)
        plt.loglog(xscaled,y,label = 'L = %len' % float(lengtharrays[i]))
    plt.legend()
    plt.show()
    return


collapse(2.1,1.5,avalarray,lengtharrays)