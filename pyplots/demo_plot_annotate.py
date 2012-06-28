import numpy as np
import pylab as pl

pl.plot(np.arange(10))
t1 = pl.text(5, 5, 'Text in the middle')
t2 = pl.figtext(0.6, 0.8, 'Upper right text')

ax = pl.gca()
ax.annotate('Here is something special', xy=(2, 7))

pl.plot(np.arange(10))
ax = pl.gca()
ax.annotate('Here too', xy=(4, 1), xytext=(1, 5),
            arrowprops={'facecolor': 'r'})
pl.show()
