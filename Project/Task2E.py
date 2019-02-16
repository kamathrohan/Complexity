
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linfit(x,a1,w1):
    return (a1 + (w1*x))


height8 = 12.966073403720461
height16 = 26.51176771291279
height32 = 53.86440529598425
height64 = 108.86492114530701
height128 = 219.27627009875573
height256 = 440.12905785600924
height512 = 883.3112396096856
height1024 = 1769.2819424160234


a0 = 1.735
heightarray = [height8,height16,height32,height64,height128,height256,height512,height1024]
lengtharray = [8,16,32,64,128,256,512,1024]
heightarrayrescaled = [1- (heightarray[i]/(a0*lengtharray[i])) for i in range(len(heightarray))]

logheight = [np.log10(i) for i in heightarrayrescaled]
loglength = [np.log10(i) for i in lengtharray]

print(np.polyfit(loglength,logheight,1))
logheightfit = [linfit(i,np.polyfit(loglength,logheight,1)[1], np.polyfit(loglength,logheight,1)[0]) for i in loglength]



plt.scatter(loglength,logheight, label = 'Observed Data',marker = 'x' )
plt.plot(loglength,logheightfit, label = "Linear Fit")
plt.xlabel("log(L)")
plt.ylabel("log(1-h/a0L)")
plt.title("Linear fit of H")
plt.grid()
plt.legend()
plt.savefig("Linfit.png")
plt.show()

def heightscaling(x,a0,a1,w1):
    h = a0*x*(1-(a1*(x**(-w1))))
    return h


A = np.polyfit(loglength,logheight,1)
print(A)
popt, pcov = curve_fit(heightscaling, lengtharray, heightarray)
print(popt)
perr = np.sqrt(np.diag(pcov))
print(perr)

plt.scatter(lengtharray,heightarray, label = "Observed Values")
plt.plot(lengtharray, [heightscaling(i,popt[0],popt[1],popt[2]) for i in lengtharray], label = "L-M Fit")
plt.xlabel("L")
plt.ylabel("h")
plt.title("L - M fit of Height against system size")
plt.savefig("L-M Fit.png")
plt.grid()
plt.show()



