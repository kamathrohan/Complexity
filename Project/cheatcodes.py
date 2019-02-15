
import numpy as np
import complexity
size1024 = complexity.stableheightarray(np.genfromtxt("5000005121.csv"),223300)
size10242 = size1024.copy()
size10243 = size1024.copy()
size10244 = size1024.copy()
size10245 = size1024.copy()
np.random.shuffle(size10242)
np.random.shuffle(size10243)
np.random.shuffle(size10244)
np.random.shuffle(size10245)

sum = size1024 + size10242 + size10243 + size10244 + size10245
avg = np.divide(sum,5)
np.savetxt("stableheight5000005125.csv",avg)