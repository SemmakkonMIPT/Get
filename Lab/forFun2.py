from semmakkon import *
import numpy as np
import matplotlib.pyplot as plt
import itertools as it

print(comb(10, 5))
x = [i*2 for i in range(1, 20)]
y = [0 for i in x]
for i in range(len(x)):
    y[i] = comb(2*i, i)/(2**(i*2))
plt.plot(x, y)
plt.show()