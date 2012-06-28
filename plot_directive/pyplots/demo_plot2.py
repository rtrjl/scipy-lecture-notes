import numpy as np
import pylab as pl

x = np.arange(100)
linear = np.arange(100)
square = np.arange(0, 10, 0.1) ** 2
lines = pl.plot(x, linear, x, square)
pl.legend(('linear', 'square'))
pl.show()
