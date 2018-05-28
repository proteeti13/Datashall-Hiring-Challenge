from scipy import integrate
import numpy as np
import math
f= lambda x:1/9*math.exp(-x/9)
more=integrate.quad(f,13,np.inf)
print('Probability of 13 or more successive dry days occur after a rainstorm',round(more[0],4))
few=integrate.quad(f,0,2)
print('Probability of fewer than 2 dry days occur after a rainstorm',round(few[0],4))
