import numpy as np
import pylab as pl

pl.close('all')
fig = pl.figure(edgecolor='y', facecolor='k')
pl.rcParams['axes.linewidth'] = 2
pl.rcParams['axes.edgecolor'] = 'y'
pl.rcParams['axes.facecolor'] = 'k'
pl.rcParams['xtick.color'] = 'y'
pl.rcParams['ytick.color'] = 'y'
pl.hist(np.random.randn(100), color='w')
pl.xlabel('x', color='y')
pl.ylabel('y', color='y')
pl.show()
