import numpy as np
import pylab as pl

fig, axes = pl.subplots(2, 2, sharex=True, sharey=True)

for ax in axes.flat:
    ax.plot(np.random.randn(10))
    ax.grid(True)

pl.show()
