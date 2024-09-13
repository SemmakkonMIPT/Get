import matplotlib.pyplot as plt
import numpy as np
from semmakkon import *
Data4 = (read_table_from_file("5.2.1/Data4.txt", skip_rows=1))
Data6 = (read_table_from_file("5.2.1/Data6", skip_rows=1))
Data8 = (read_table_from_file("5.2.1/Data8", skip_rows=1))
U4 = Data4[0]
I4 = Data4[1]
U6 = Data6[0]
I6 = Data6[1]
U8 = Data8[0]
I8 = Data8[1]
linGraf(U4, I4, show_trendline=False)
linGraf(U6, I6, show_trendline=False)
linGraf(U8, I8, show_trendline=False)
plt.show()

