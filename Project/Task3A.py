import numpy as np
import matplotlib.pyplot as plt
import logbin230119 as logbin
import complexity



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


A = complexity.avalsize(10000,16)
x, y = logbin.logbin(A, scale = 1.2)
plt.loglog(x,y, label = 'L = 16')

A = complexity.avalsize(10000,32)
x, y = logbin.logbin(A, scale = 1.2)
plt.loglog(x, y, label = 'L = 32')

A = complexity.avalsize(10000,64)
x, y = logbin.logbin(A, scale = 1.2)
plt.loglog(x, y, label = 'L = 64')
plt.legend()
plt.show()
"""

#aval08 = np.genfromtxt("avalsize100008.txt")
#aval08 = aval08.astype(int)
#x, y = logbin.logbin(aval08, scale = 1.2)
#plt.loglog(x,y, label = 'L = 8')                                                                                                                                        
#plt.show()