import matplotlib.pyplot as plt
from semmakkon import *
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ar = np.concatenate([np.array([1, 2, 3]), np.array([1, 2, 3])])
ar2 = np.ones(10)*10
ar3 = np.hstack([np.array([[1, 2, 3], [1, 2, 3]]), np.array([[1, 2, 3], [1, 2, 3]])])
ar4 = np.sin(ar)
#print(ar4)
ArrPlot(RaddotEllidArrZ(2, 2, 2))
#ArrPlot(dotEllidArrZ(2, 2, 2), O = [5, 0, 0])
makeMash(4)
plt.show()