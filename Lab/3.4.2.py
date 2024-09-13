import matplotlib.pyplot as plt
import numpy as np
from semmakkon import *
Um = 0.5/24
k = 24
T0 = 8.252
print(Um)
U = np.array([-0.05, -0.025, -0.03, -0.026, -0.024, -0.029 ,-0.02, -0.02, -0.01, -0.023, -0.016, 0.028, 0.07, 0.046]) #мвольт
T = np.array([14.12, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])
Tau = np.array([9.88, 9.98, 9.8, 9.49, 10, 19.27, 70.98, 26.85, 166, 313, 206.98, 49, 3000, 52.46]) #милисек
Tv = T+k*U
print(Tv)
TT = Tau*Tau-T0**2
TT_1 = 1/TT
print(TT)
linGraf(Tv, TT_1)
plt.show()