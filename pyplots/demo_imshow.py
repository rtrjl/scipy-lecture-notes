import scipy as sp
import pylab as pl

l = sp.misc.lena()
pl.imshow(l, cmap=pl.cm.gray)
pl.axis('off')
