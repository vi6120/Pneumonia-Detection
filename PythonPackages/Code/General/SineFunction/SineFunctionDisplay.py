# https://goelhardik.github.io/2016/05/25/sampling-sine-wave/

import matplotlib.pyplot as plt
import numpy as np
import pylab
import pickle

xlim = 40

# define functions
x = np.arange(0, xlim, 0.1)
y = np.sin(x)

# write the data out to a file
sinedata = open('sinedata.md', 'wb')
pickle.dump(y, sinedata)
sinedata.close()

# interactive mode on
pylab.ion()

# set the data limits
plt.xlim(0, xlim)
plt.ylim(-1, 1)

# plot the first 200 points in the data
plt.plot(x[0:200], y[0:200])

# plot the remaining data incrementally
#for i in range(200, len(y)):
#    plt.scatter(x[i], y[i])
#    plt.pause(0.0005)


# hold the plot until terminated
while True:
    plt.pause(0.5)