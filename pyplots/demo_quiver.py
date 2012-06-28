import numpy as np
import pylab as pl

x, y = np.mgrid[0:10, 0:10]
u = np.ones((10, 10))
v = np.ones((10, 10))
u[4, 4] = 3
v[1, 1] = -1
pl.quiver(x, y, u, v)
pl.show()
