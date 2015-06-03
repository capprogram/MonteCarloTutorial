#leave this line commented out until the end of the exercise:
#from __future__ import division # make division act like python3 even if 2.7

import random
import matplotlib.pyplot as plt
import pylab
pylab.ion() 
import numpy as np

uu=[] # variable named uu to avoid single-letter variable name

mean, sigma = 0., 1.
for i in range(0,1000):
   uu.append(random.gauss(mean,sigma))

#3: plot histogram
# histogram plotting methods taken from http://matplotlib.org
#n1, bins1, patches1 = plt.hist(uu,bins=50,normed=1,histtype='stepfilled')
#plt.setp(patches1,'facecolor','g','alpha',0.75)

#overplot expected Gaussian distribution on histogram
#must uncomment "import numpy as np" above to be able to use np.exp and np.sqrt
#gaussfunct=# fill in using equation
#plt.plot(bins1,gaussfunct,'k--',linewidth=1.5)

#4: compute fraction in confidence interval
#uarray=np.array(uu) # "np.array" turns a list into an array
#limval= # set to value of interest
#fractinrange=np.size(np.where(abs(uarray) <= limval))/np.size(uarray)
# above line is integer division so import python3 division to get real number
#print(fractinrange)
