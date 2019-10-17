# coding=utf-8
import numpy as np

import matplotlib.pylab as pb

x = np.linspace(1, 50, num=50)

y1 = 2 * x + 1
y2 = x ** 2

pb.figure()
pb.plot(x, y1)
# pb.savefig("./pb.pdf")
# pb.show()

pb.figure()
pb.plot(x, y1, )
pb.plot(x, y2, color='green', linestyle="--")
pb.xlim(1, 40)
pb.ylabel(u"y(number)")
pb.xlabel(u"x(number)")
pb.xticks([10, 20])
pb.yticks([100, 400], [r"$low$", r"$middle$"])
pb.show()
