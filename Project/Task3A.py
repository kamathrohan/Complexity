import numpy as np
import matplotlib.pyplot as plt
import logbin230119 as logbin
import complexity



A = complexity.avalsize(10000,8)
x, y = logbin.logbin(A, scale = 1.2)
plt.loglog(x,y, label = 'L = 8')

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