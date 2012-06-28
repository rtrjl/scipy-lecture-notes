from scipy import misc
import pylab as pl

l = misc.lena()
pl.imshow(l, cmap=pl.cm.gray)
pl.axis('off')
