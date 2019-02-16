import numpy as np  #some obvious imports
import matplotlib.pyplot as plt
import complexity

cross04 = 14.0
cross08 = 54.2
cross16 = 215.4
cross32 = 860.0
cross64 = 3468.8
cross128 = 13902.25
cross256 = 56137.75
cross512 = 225300
cross1024 = 906140

zmean04 = 1.5784848788303625
zmean08 = 1.6245599919541387
zmean16 = 1.6565242906715656
zmean32 = 1.6817843281950366
zmean64 = 1.7017256761833208
zmean128 = 1.7132332024311723
zmean256 = 1.7205135452098304
zmean512 = 1.7244838130920948
zmean1024 = 1.7310812512093

zerr04 =  0.5741604932442441
zerr08 = 0.5506830123976014
zerr16 = 0.5267105547095282
zerr32 = 0.5062115454376638
zerr64 = 0.49374888616642454
zerr128 =  0.4852639356624544
zerr256 = 0.48069302220209253
zerr512 = 0.47812723835298937
zerr1024 = 0.47512723835298937




"""
TASK 2D


"""

A = [4,8,16,32,64,128,256,512,1024]


B = []
def theoreticalcross(zmean,L):
    A = (zmean*(L**2)/2)*(1 + (1/L))
    #B = ((zerr*(L**2)/2)*(1 + (1/L))
    return A

"""

plt.scatter(A, [(theoreticalcross(zmean04,4)-cross04)/theoreticalcross(zerr04,4),(theoreticalcross(zmean08,8)-cross08)/theoreticalcross(zerr08,8), (theoreticalcross(zmean16,16)-cross16)/theoreticalcross(zerr16,16),
                (theoreticalcross(zmean32,32)-cross32)/theoreticalcross(zerr32,32), (theoreticalcross(zmean64,64)-cross64)/theoreticalcross(zerr64,64),
                (theoreticalcross(zmean128, 128)-cross128)/theoreticalcross(zerr128,128), (theoreticalcross(zmean256,256)-cross256)/theoreticalcross(zerr256,256), (theoreticalcross(zmean512,512)-cross512)/theoreticalcross(zerr512,512),
                (theoreticalcross(zmean1024,1024)-cross1024)/theoreticalcross(zerr1024,1024)
                 ], s = 30, marker = 'x')
plt.xlabel("L")
plt.ylabel("T_predicted - T_observed (number of standard deviations)")
plt.title("Difference in theoretical and observed crossover values")
plt.savefig("Task2D-theoreticalvsobserved.png")
plt.grid()

plt.show()

"""

plt.scatter(A,[zmean04,zmean08,zmean16,zmean32,zmean64,zmean128,zmean256,zmean512,zmean1024])
plt.xlabel("L")
plt.ylabel("<z>")
plt.title("<z> vs L")
plt.grid()
plt.savefig("Task2D-zmean.png")

plt.show()

