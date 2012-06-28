"""
Simple image blur by convolution with a Gaussian kernel
"""

import numpy as np
from scipy import ndimage, misc
import pylab as pl

# load image
lena = misc.lena().astype(np.float)

lena_dog = ndimage.gaussian_filter(lena, .5) - ndimage.gaussian_filter(lena, 1)

pl.imshow(lena_dog, cmap=pl.cm.gray)
pl.axis('off')
pl.show()

