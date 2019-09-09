# /usr/bin/python
# coding=utf-8

import matplotlib.pylab as pb
import numpy as np

x = np.linspace(1, 50, num=50)

y = 2 * x + 1

pb.plot(x, y)
# pb.show()
pb.savefig("./pb.pdf")
pb.show()
