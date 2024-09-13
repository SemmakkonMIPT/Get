from semmakkon import *
import matplotlib.pyplot as plt
from math import *
import numpy as np

Data1 =  transpose_table(read_table_from_file("DataVac/DataVac1.1", number_separator=',', row_separator='\t', isFloat=True))
# print_table(Data1)
pArray = toArray(Data1[1])
uArray = toArray(Data1[2])
klnpArray = toArray(Data1[3])
klnuArray = toArray(Data1[4])

Data2 =  transpose_table(read_table_from_file("DataVac/DataVac1.2", number_separator=',', row_separator='\t',
                                              isFloat=True, skip_rows=2))
# print_table(DataVac)
u80Array = toArray(Data2[0])
IArray = toArray(Data2[1])
u20Array = toArray(Data2[2])

Data3 =  transpose_table(read_table_from_file("DataVac/DataVac1.3", number_separator=',', row_separator='\t',
                                              isFloat=True, skip_rows=2))
pArrayAr = toArray(Data3[1])
uArrayAr = toArray(Data3[2])

Data4 =  transpose_table(read_table_from_file("DataVac/DataVac1.4", number_separator=',', row_separator='\t',
                                              isFloat=True, skip_rows=2))
# print_table(Data4.txt)
u100Array = toArray(Data4[0])
IArrayAr = toArray(Data4[1])
u16Array = toArray(Data4[2])



N = [0.6]
if 1 in N:
    linGraf(pArray, uArray, show_trendline=False, create_plot=True)
if 2 in N:
    linGraf(klnpArray, klnuArray, show_trendline=False, create_plot=True)
if 3 in N:
    linGraf(u80Array, IArray, create_plot=True)
if 4 in N:
    linGraf(u20Array, IArray, create_plot=True)
if 5 in N:
    linGraf(u80Array, IArray, create_plot=True)
    linGraf(u20Array[:-1], IArray[:-1], create_plot=False)
if 6 in N:
    linGraf(pArrayAr, uArrayAr, create_plot=True, show_trendline=False)
if 7 in N:
    linGraf(pArray, uArray, show_trendline=False, create_plot=True)
    linGraf(pArrayAr, uArrayAr, create_plot=False, show_trendline=False)
if 8 in N:
    linGraf(u100Array, IArrayAr, create_plot=True)
if 9 in N:
    linGraf(u16Array, IArrayAr, create_plot=True)
if 10 in N:
    linGraf(u100Array, IArrayAr, create_plot=True)
    linGraf(u16Array[::-1], IArrayAr)
if 11 in N:
    linGraf(u100Array, IArrayAr, create_plot=True)
    linGraf(u16Array, IArrayAr)
if 12 in N:
    linGraf(u80Array, IArray, 5,  create_plot=True)
    linGraf(u20Array[:-1], IArray[:-1], 5,  create_plot=False)
    linGraf(u100Array, IArrayAr, 5)
    linGraf(u16Array, IArrayAr, 5)
if 0.1 in N:
    linGraf(pArray, uArray, show_trendline=False, create_plot=True, name = "Зависимость U(p)",
            OXname="Давление p, torr", OYname="Напряжение u, $10^{-2}$ kv")
if 0.2 in N:
    linGraf(pArrayAr, uArrayAr, show_trendline=False, create_plot=True, name = "Зависимость U(p) для Аргона",
            OXname="Давление p, torr", OYname="Напряжение u, $10^{-2}$ kv")
if 0.3 in N:
    linGraf(pArray, uArray, show_trendline=False, create_plot=True, name = "Зависимость U(p)",
            OXname="Давление p, torr", OYname="Напряжение u, $10^{-2}$ kv", show_label=True, flabel="Воздух")
    linGraf(pArrayAr, uArrayAr, show_trendline=False, name = "Зависимость U(p) для Аргона",
            OXname="Давление p, torr", OYname="Напряжение u, $10^{-2}$ kv", flabel="Аргон")
if 0.4 in N:
    linGraf(u80Array, IArray, create_plot=True, name = "Зависимость I(U)", OXname="Напряжение u, $10^{-2}$ kv",
            OYname="Ток I, $10^{-4}$ A", flabel="Натекание 80", fcolor="red")
    linGraf(u20Array[:-1], IArray[:-1], create_plot=False, flabel="Натекание 20", fcolor="g")
if 0.5 in N:
    linGraf(u100Array, IArrayAr, create_plot=True, name = "Зависимость I(U) для Аргона", OXname="Напряжение u, $10^{-2}$ kv",
            OYname="Ток I, $10^{-4}$ A", flabel="Натекание 100", fcolor="red")
    linGraf(u16Array, IArrayAr, create_plot=False, flabel="Натекание 16", fcolor="g")
if 0.6 in N:
    linGraf(u80Array, IArray, 5,  create_plot=True, name = "Зависимость I(U)", OXname="Напряжение u, $10^{-2}$ kv",
            OYname="Ток I, $10^{-4}$ A", flabel="Воздух", fcolor="red")
    linGraf(u20Array[:-1], IArray[:-1], 5,  create_plot=False, fcolor="red")
    linGraf(u100Array, IArrayAr, 5,  create_plot=False, name = "Зависимость I(U) для Аргона", OXname="Напряжение u, $10^{-2}$ kv",
            OYname="Ток I, $10^{-4}$ A", flabel="Аргон", fcolor="g")
    linGraf(u16Array, IArrayAr, 5,  create_plot=False, fcolor="g")



plt.show()