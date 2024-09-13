import matplotlib.pyplot as plt
import numpy as np
from semmakkon import *
Data1 = transpose_table(read_table_from_file("Data/labaEX4.5.2.1.txt", skip_rows=1))
Data1 = transpose_table(read_table_from_file("Data/laba4.5.2.1.txt", skip_rows=1))
alfaArray = toArray(Data1[0])
h1Array = toArray(Data1[1])
h2Array = toArray(Data1[2])
h3Array = toArray(Data1[3])
h4Array = toArray(Data1[4])

h1Array+=4
h2Array+=4
h3Array+=4
h4Array+=4

# h1Array = h1Array.astype(float)
# h2Array = h2Array.astype(float)
# h1Array = h1Array.astype(float)
# h2Array = h2Array.astype(float)
dh = 0.1
deltaArray = h1Array/h2Array
gammaArray = (h4Array-h3Array)/(h4Array+h3Array)
gamma1Array = 2*np.sqrt(deltaArray)/(1+deltaArray)
gamma3Array = gammaArray/gamma1Array
gamma3zero = gamma3Array[0]
g3_g3zeroArray = gamma3Array/gamma3zero

sGammaArray = (2*dh/(h4Array-h3Array))+(2*dh/(h4Array+h3Array))
sDeltaArray = (dh/h1Array)+(dh/h2Array)
sGamma1Array = (sDeltaArray/2)+(sDeltaArray*deltaArray/(deltaArray+1))
sGamma3Array = sGamma1Array+sGammaArray
sg3_g3zeroArray = sGamma3Array+sGamma3Array[0]
dGamma3Array = sg3_g3zeroArray*g3_g3zeroArray

cosAlfaArray = degCos(alfaArray)

# print(gamma3Array)
# print(g3_g3zeroArray)
# print(sGamma3Array)
# print(dGamma3Array)

Data2 = transpose_table(read_table_from_file("Data/labaEX4.5.2.2.txt", skip_rows=1))
Data2 = transpose_table(read_table_from_file("Data/laba4.5.2.2.txt", skip_rows=1))
dx = 0.1
xArray = toArray(Data2[0])
h1Array2 = toArray(Data2[1])
h2Array2 = toArray(Data2[2])
h3Array2 = toArray(Data2[3])
h4Array2 = toArray(Data2[4])

h1Array2 += 4
h2Array2 += 4
h3Array2 += 4
h4Array2 += 4


deltaArray2 = h1Array2/h2Array2
gammaArray2 = (h4Array2-h3Array2)/(h4Array2+h3Array2)
gamma1Array2 = 2*np.sqrt(deltaArray2)/(1+deltaArray2)
gamma2Array = gammaArray2/gamma1Array2

sGammaArray2 = (2*dh/(h4Array2-h3Array2))+(2*dh/(h4Array2+h3Array2))
sDeltaArray2 = (dh/h1Array2)+(dh/h2Array2)
sGamma1Array2 = (sDeltaArray2/2)+(sDeltaArray2*deltaArray2/(deltaArray2+1))
sGamma2Array = sGamma1Array2+sGammaArray2
dGamma2Array = sGamma2Array*gamma2Array



N = [1, 2]
if 1 in N:
    linGraf(np.abs(cosAlfaArray), g3_g3zeroArray, 0, sg3_g3zeroArray, create_plot=True)

if 2 in N:
    linGraf(xArray, gammaArray2, dx, dGamma2Array, show_trendline=False, create_plot=True)

plt.show()



