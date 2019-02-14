import numpy as np
import matplotlib.pyplot as plt
import complexity
import pandas as pd


def probability(array):
    stddv = np.std(array)
    s = pd.Series(array)
    probability = (s.groupby(s).transform('count') / len(s)).values
    return probability*stddv

def datacollapse(array):
    mean = np.average(array)
    stddv = np.std(array)
    movedarray = [i - mean for i in array]
    return np.divide(movedarray,stddv)


size04 = np.genfromtxt("100000405.csv")
size08 = np.genfromtxt("100000805.csv")
size16 = np.genfromtxt("100001605.csv")
size32 = np.genfromtxt("100003205.csv")
size64 = np.genfromtxt("100006405.csv")
size128 = np.genfromtxt("7000012805.csv")
size256 = np.genfromtxt("7000025605.csv")
#size512 = np.genfromtxt("5000005121.csv")
#size1024 = np.genfromtxt("100000010241.csv")


cross04 = 16.0
cross08 = 54.2
cross16 = 218.4
cross32 = 860.0
cross64 = 3468.8
cross128 = 13902.25
cross256 = 56137.75
cross512 = 223300
cross1024 = 904140

stable04 = complexity.stableheightarray(size04,cross04)
stable08 = complexity.stableheightarray(size08,cross08)
stable16 = complexity.stableheightarray(size16,cross16)
stable32 = complexity.stableheightarray(size32,cross32)
stable64 = complexity.stableheightarray(size64,cross64)
stable128 =complexity.stableheightarray(size128,cross128)
stable256 =complexity.stableheightarray(size256,cross256)





plt.scatter(datacollapse(stable08),probability(stable08))
plt.scatter(datacollapse(stable16),probability(stable16))
plt.scatter(datacollapse(stable32),probability(stable32))
plt.scatter(datacollapse(stable64),probability(stable64))
plt.scatter(datacollapse(stable128),probability(stable128))
plt.scatter(datacollapse(stable256),probability(stable256))

plt.show()
"""
plt.scatter(stable16,probability(stable16))
plt.scatter(stable32,probability(stable32))
plt.scatter(stable64,probability(stable64))
plt.scatter(stable128,probability(stable128))
plt.scatter(stable256,probability(stable256))


"""






