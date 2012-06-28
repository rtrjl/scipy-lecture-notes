import numpy as np
import pylab as pl

x = np.arange(100)
linear = np.arange(100)
square = np.arange(0, 10, 0.1) ** 2
pl.plot(x[::5], linear[::5], color='k', label='linear', linewidth=4, marker='o',
        markeredgecolor='g', markerfacecolor='r', markersize=14,
        markeredgewidth=3)
pl.plot(x, square, 'r--', label='square')
pl.legend(loc='lower right')
pl.show()
