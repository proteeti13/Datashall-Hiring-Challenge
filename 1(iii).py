import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

x = np.arange(2,100)
y = [(-1/(i+2)**2)+4 for i in x]

plt.plot(x,y)
plt.show()
