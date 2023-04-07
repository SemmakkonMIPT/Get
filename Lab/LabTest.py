import matplotlib.pyplot as plt
from semmakkon import *

D = [[0, 0, 0], [1, 1, 1], [2, 3, 4]]
X = [0, 1, 2]
Y = [0, 1, 3]
Z = [0, 1, 4]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = [4]
if 1 in n:
    ZElips3d(2, 2, 2)
if 2 in n:
    ZWayElipsoid(2, 2, 2)
if 3 in n:
    n = int(input())
    Elipsoid(2, 2, 2, n)
if 4 in n:
    ZHiperbaloid(2, 2, 2)
#plotELd(1, 1, 1)
plt.show()