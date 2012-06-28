"""
Discover the periods in ../../data/populations.txt
"""
import numpy as np
import pylab as pl
from scipy import fftpack

data = np.loadtxt('../../data/populations.txt')
years = data[:, 0]
populations = data[:, 1:]

ft_populations = fftpack.fft(populations, axis=0)
frequencies = fftpack.fftfreq(populations.shape[0], years[1] - years[0])

pl.figure()
pl.plot(years, populations)

pl.figure()
pl.plot(1. / frequencies, np.abs(ft_populations), 'o')
pl.xlim(0, 20)
pl.xlabel('Period')
pl.ylabel('Power')
pl.show()

# There's probably a period of around 10 years (obvious from the
# plot), but for this crude a method, there's not enough data to say
# much more.
