import numpy as np
import pylab as pl

a = np.random.randn(5, 5)
pl.imshow(a, cmap=pl.cm.jet, interpolation='nearest')
pl.show()
