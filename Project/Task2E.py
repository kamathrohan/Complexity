
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit




height8 = 12.966073403720461
height16 = 26.51176771291279
height32 = 53.86440529598425
height64 = 108.86492114530701
height128 = 219.27627009875573
height256 = 440.12905785600924
height512 = 883.3112396096856
height1024 = 1769.2819424160234


heightarray = [height8,height16,height32,height64,height128,height256,height512,height1024]
lengtharray = [8,16,32,64,128,256,512,1024]



def heightscaling(x,a0,a1,w1):
    h = a0*x*(1-(a1*(x**(-w1))))
    return h

popt, pcov = curve_fit(heightscaling, lengtharray, heightarray)
print(popt)
perr = np.sqrt(np.diag(pcov))
print(perr)
