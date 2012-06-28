import numpy as np
import pylab as pl

pl.plot(np.arange(10))
pl.xlabel('measured')
pl.ylabel('calculated')
pl.title('Measured vs. calculated')
pl.grid(True)
pl.show()
