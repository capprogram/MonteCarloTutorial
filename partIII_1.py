# uncomment this line if you need to
#from __future__ import division # make division act like python3 even if 2.7

import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt
import pylab
pylab.ion()

# notes: probability distribution, its integral, and its reverse lookup
#### next 3 lines are pseudo-code, do not uncomment but use for reference
#### p_r=2.*3.14159*r / (3.14159*R**2)
#### intp_r=3.14159*r**2 / (3.14159*R**2)  =  r**2 for R=1
#### r_at_given_intp_r= ??? solve analytically on paper

# choose nran random numbers in uniform interval 0-1
nran = 1000
xvals = npr.random(nran)

# the integral of a uniform distribution p_u*dx (=1*dx) from 0 to x is just x
intp_uni = xvals # rename variable for clarity

# solve for radius that gives the same integrated area under p_r
intp_r = intp_uni # rename variable for clarity
#radvals = ??? # use analytic solution you found above

# make a histogram
#n1, bins1, patches1 = plt.hist(radvals,bins=50,normed=1,histtype='stepfilled')
#plt.setp(patches1,'facecolor','g','alpha',0.75)

# insert code below stolen/modified from other codes
