import random
import matplotlib.pyplot as plt
import pylab
pylab.ion() 

x=[]
y=[]

#random.seed(555)
for i in range(0,10):
   x.append(random.random())

#random.seed(555)
for i in range(0,10):
   y.append(random.random())

plt.plot(x,y,'g*')
plt.xlabel('x')
plt.ylabel('y')
