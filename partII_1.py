# adapted from
# http://niallohiggins.com/2007/07/05/monte-carlo-simulation-in-python-1/

import random

DARTS=10000 # how many darts to you need to get a good, consistent estimate?
hits = 0
throws = 0
for i in range (0, DARTS):
    throws += 1
    x = random.uniform(-1,1) # square box circumscribes circle with radius 1
    y = random.uniform(-1,1)
    distsquared = x**2 + y**2 # taking the square root here would slow the code
    if distsquared <= 1.0:
        hits = hits + 1.0

# hits / throws = area of circle / area of square = Pi 1^2 / 2^2
estpi = 4 * (hits / throws)

print("pi = %s" % estpi)
