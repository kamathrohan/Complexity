import numpy as np
import matplotlib.pyplot as plt
import logbin230119 as logbin
import pandas as pd
import complexity
from scipy.optimize import curve_fit
def linfit(x,a,b):
    return (a*x + b)

"""
A = complexity.avalsize(10000,4)
np.savetxt('avalsize100004.txt',A)

A = complexity.avalsize(10000,8)
np.savetxt('avalsize100008.txt',A)

A = complexity.avalsize(10000,16)
np.savetxt('avalsize1000016.txt',A)

A = complexity.avalsize(10000,32)
np.savetxt('avalsize1000032.txt',A)

A = complexity.avalsize(50000,64)
np.savetxt('avalsize1000064.txt',A)

A = complexity.avalsize(100000,128)
np.savetxt('avalsize100000256.txt',A)

A = complexity.avalsize(350000,256)
np.savetxt('avalsize100000256.txt',A)

A = complexity.avalsize(1000000,512)
np.savetxt('avalsize500000512.txt',A)

A = complexity.avalsize(1200000,1024)
np.savetxt('avalsize10000001024.txt',A)


"""

aval04 = np.genfromtxt("avalsize100004.txt")
aval04 = aval04.astype(float)

aval08 = np.genfromtxt("avalsize100008.txt")
aval08 = aval08.astype(float)

aval16 = np.genfromtxt("avalsize1000016.txt")
aval16 = aval16.astype(float)

aval32 = np.genfromtxt("avalsize1000032.txt")
aval32 = aval32.astype(float)

aval64 = np.genfromtxt("avalsize1000064.txt")
aval64 = aval64.astype(float)


aval128 = np.genfromtxt("avalsize100000128.txt")
aval128 = aval128.astype(float)

aval256 = np.genfromtxt("avalsize100000256.txt")
aval256 = aval256.astype(float)

aval512 = np.genfromtxt("avalsize500000512.txt")
aval512 = aval512.astype(float)



aval1024 = np.genfromtxt("avalsize10000001024.txt")
aval1024 = aval1024.astype(float)


def plot(scale):
    x, y = logbin.logbin(aval04, scale = scale)
    plt.loglog(x,y, label = 'L = 4')
    
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


    plt.xlabel("Binned Avalanche Sizes")
    plt.ylabel("Probability Distribution")
    plt.title("Avalanche Sizes (s) vs Probability Distribution")
    plt.legend()
    plt.grid()
    #plt.savefig("Binnedavalanches.png")
    plt.show()
    
    return

#plot(1.2)

avalarray = [aval04,aval08,aval16,aval32,aval64,aval128,aval256,aval512,aval1024]
lengtharrays = [4, 8,16,32,64,128,256,512,1024]



def collapse(D, tau,arrayofarrays, lengtharrays):
    for i in range(len(arrayofarrays)):
        x, y = logbin.logbin(arrayofarrays[i], scale = 1.3)
        for j in range(len(x)):
            y[j] = y[j]*(x[j]**tau)
        xscaled = np.divide(x,lengtharrays[i]**D)
        plt.loglog(xscaled,y,label = 'L = %len' % float(lengtharrays[i]))
    plt.xlabel("s/L^D")
    plt.ylabel("P*(s**tau)")
    plt.title("Data Collapse of Avalanche Size")
    plt.grid()
    plt.legend()
    plt.savefig("fullcollapse.png")
    plt.show()
    return

def moment(arrays,k):
    average = []
    for i in arrays:
        A = [s**k for s in i]
        average.append(np.average(A))
    return [np.log10(i) for i in average]
def momentnolog(arrays,k):
    average = []
    for i in arrays:
        A = [s**k for s in i]
        average.append(np.average(A))
    return average

loglength = [np.log10(i) for i in lengtharrays]
linfit1 = np.polyfit(loglength,moment(avalarray,1),1)
linfit2 = np.polyfit(loglength,moment(avalarray,2),1)
linfit3 = np.polyfit(loglength,moment(avalarray,3),1)
linfit4 = np.polyfit(loglength,moment(avalarray,4),1)
linfit5 = np.polyfit(loglength,moment(avalarray,5),1)


print(linfit1[0])
print(linfit2[0])
print(linfit3[0])
print(linfit4[0])
print(linfit5[0])

plt.scatter(loglength,moment(avalarray,1), label = 'k = 1')
plt.scatter(loglength,moment(avalarray,2), label = 'k = 2')
plt.scatter(loglength,moment(avalarray,3), label = 'k = 3')
plt.scatter(loglength,moment(avalarray,4), label = 'k = 4')
plt.scatter(loglength,moment(avalarray,5), label = 'k = 5')
plt.plot(loglength, [linfit(i,linfit1[0],linfit1[1]) for i in loglength])
plt.plot(loglength, [linfit(i,linfit2[0],linfit2[1]) for i in loglength])
plt.plot(loglength, [linfit(i,linfit3[0],linfit3[1]) for i in loglength])
plt.plot(loglength, [linfit(i,linfit4[0],linfit4[1]) for i in loglength])
plt.plot(loglength, [linfit(i,linfit5[0],linfit5[1]) for i in loglength])


plt.legend()
plt.grid()
plt.xlabel("log(L)")
plt.ylabel("log(Sk)")
plt.title("L vs <s_k> (log-log)")
#plt.savefig("momentvl.png")
plt.show()
"""
k = [1,2,3,4,5]
slopes = [0.9998227215203218,3.1261540551168516,5.295790536005037,7.476765077733716,9.664775172545411]
popt, pcov = curve_fit(linfit,k,slopes)
plt.scatter(k,slopes)
plt.plot(k, [linfit(i,popt[0],popt[1]) for i in k])
plt.grid()
plt.xlabel("k")
plt.ylabel("D(1+k-tau)")
plt.title("k vs D(1+k-tau)")
plt.savefig("kvsslope.png")
plt.show()
print(popt)
print(np.sqrt(np.diag(pcov)))
#


def momenttheor(lenarray,k):
    D =2.19
    tau = 1.55
    L = np.asarray(lenarray)
    array = L**(D*(1+k-tau))
    return ( array)

def ratio(k):
    ratio = []
    theoretical = momenttheor(lengtharrays,k)
    actual = momentnolog(avalarray,k)
    for i in range(len(lengtharrays)):
        ratio.append(actual[i]/theoretical[i])
    return(ratio)


#plt.plot(lengtharrays,momenttheor(lengtharrays,2))
plt.plot(lengtharrays,ratio(1), label = "k = 1")
plt.plot(lengtharrays,ratio(2), label = "k = 2")
plt.plot(lengtharrays,ratio(3), label = "k = 3")
plt.plot(lengtharrays,ratio(4), label = "k = 4")
plt.plot(lengtharrays,ratio(5), label = "k = 5")
plt.xlabel("L")
plt.ylabel("Ratio of obsereved and theoretical moments")
plt.title("Comparision of Theoretical and observed values")
plt.grid()
plt.savefig("theoreticalvactual.png")
plt.show()
"""
collapse(2.19,1.55,avalarray,lengtharrays)
