import numpy as np
from semmakkon import *
import matplotlib.pyplot as plt

# Указываем пути к файлам
file_path_zhzs = 'Data/zhzs1.txt'
file_path_calibration = 'Data/calibration.txt'
file_path_fs = 'Data/fs1.txt'
file_path_os = 'Data/os14.txt'

# Инициализируем два пустых списка для хранения данных
lambda_data = []
intensity_data = []
lambda_colibr = []
k_colibration = []
lambda_fs = []
array_fs = []
lambda_os = []
array_os = []

# Читаем данные из файла zhzs1.txt
with open(file_path_zhzs, 'r') as file:
    # Пропускаем первые 14 строк (индексация с 0)
    for _ in range(14):
        next(file)

    # Читаем данные начиная с 15 строки
    for line in file:
        # Разделяем строку на два значения, предполагая, что они разделены пробелом
        values = line.split()
        # Заменяем запятые на точки и преобразуем значения в числа с плавающей точкой
        lambda_data.append(float(values[0].replace(',', '.')))
        intensity_data.append(float(values[1].replace(',', '.')))

# Читаем данные из файла calibration.txt
with open(file_path_calibration, 'r') as file:
    for line in file:
        # Разделяем строку на два значения, предполагая, что они разделены пробелом
        values = line.split()
        # Преобразуем значения в числа с плавающей точкой и добавляем в соответствующие списки
        lambda_colibr.append(float(values[0]))
        k_colibration.append(float(values[1]))

# Читаем данные из файла fs.txt
with open(file_path_fs, 'r') as file:
    # Пропускаем первые 14 строк (индексация с 0)
    for _ in range(14):
        next(file)
    for line in file:
        # Разделяем строку на два значения, предполагая, что они разделены пробелом
        values = line.split()
        # Преобразуем значения в числа с плавающей точкой и добавляем в соответствующие списки
        lambda_fs.append(float(values[0].replace(',', '.')))
        array_fs.append(float(values[1].replace(',', '.')))

# Читаем данные из файла os.txt
with open(file_path_os, 'r') as file:
    # Пропускаем первые 14 строк (индексация с 0)
    for _ in range(14):
        next(file)
    for line in file:
        # Разделяем строку на два значения, предполагая, что они разделены пробелом
        values = line.split()
        # Преобразуем значения в числа с плавающей точкой и добавляем в соответствующие списки
        lambda_os.append(float(values[0].replace(',', '.')))
        array_os.append(float(values[1].replace(',', '.')))

# Преобразуем списки в массивы numpy
lambda_zhzs_array = np.array(lambda_data)
intensity_zhzs_array = np.array(intensity_data)
lambda_colibr_array = np.array(lambda_colibr)
k_colibration_array = np.array(k_colibration)
lambda_fs_array = np.array(lambda_fs)
intensity_fs_array = np.array(array_fs)
lambda_os_array = np.array(lambda_os)
intensity_os_array = np.array(array_os)

intensity_zhzs_colibr = intensity_zhzs_array*k_colibration_array
intensity_os_colibr = intensity_os_array*k_colibration_array
intensity_fs_colibr = intensity_fs_array*k_colibration_array

lambda_array = lambda_zhzs_array
n = len(lambda_array)
int_zhzs = sum(intensity_zhzs_colibr)
sred_zhzs = int_zhzs/n
int_os = sum(intensity_os_colibr)
sred_os = int_os/n
int_fs = sum(intensity_fs_colibr)
sred_fs = int_fs/n
def get_int_array(intensity):
    int_array = [sum(intensity[:i]) for i in range(1, n + 1)]
    return int_array

int_zhzs_array = get_int_array(intensity_zhzs_colibr)
int_zhzs_array_uncal = get_int_array(intensity_zhzs_array)


int_os_array = get_int_array(intensity_os_colibr)
int_os_array_uncal = get_int_array(intensity_os_array)

int_fs_array = get_int_array(intensity_fs_colibr)
int_fs_array_uncal = get_int_array(intensity_fs_array)


integrals = toArray([int_fs_array[2300], int_zhzs_array[2300], int_os_array[2300]])

EOP_filt = transpose_table(read_table_from_file("Data/EOPfilt"))
Is_filt = toArray(list_to_float_array(EOP_filt[2]))
Ic_filt = toArray(list_to_float_array(EOP_filt[1]))
K_filt = Is_filt/Ic_filt
lambda_filt = toArray([450, 540, 600]) #Пики в спектрах

A = toArray(Is_filt[1:]) / integrals

N = [0, 4, 6, 7, 8]
if 0 in N: #
    linGraf(lambda_array, k_colibration_array, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Калибровочный множитель", name="Калибровочные коэффициенты")

# Графики по отдельность не особо нужны
if 1 in N:
    linGraf(lambda_array, intensity_zhzs_array, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Cпектр источника через желто-зеленый фильтр")

    linGraf(lambda_array, intensity_zhzs_colibr, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Калиброванный спектр через желто-зеленый фильтр")
if 2 in N:
    linGraf(lambda_array, intensity_os_array, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Спектр источника через красный фильтр")

    linGraf(lambda_array, intensity_os_colibr, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Калиброванный спектр через красный фильтр")

if 3 in N:
    linGraf(lambda_array, intensity_fs_array, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Спектр источника через синий фильтр")

    linGraf(lambda_array, intensity_fs_colibr, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Калиброванный спектр через синий фильтр")

#.....................

if 4 in N: #Интегралы пластин
    linGraf(lambda_array, int_zhzs_array, show_trendline=False, create_plot=True, OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интеграл спектра интенсивности", name="Интегралы пластин",
            flabel="Зелено-желтый фильтр", fcolor='yellowgreen')
    linGraf(lambda_array, int_os_array, show_trendline=False, flabel="Красный фильтр", fcolor='r')
    linGraf(lambda_array, int_fs_array, show_trendline=False, flabel="Синий фильтр", fcolor='b')


if 5 in N: # этот график тоже не особо нужен
    linGraf(lambda_filt, K_filt[1:], form = '.', show_trendline=True, MNKlinestyle='--', create_plot=True,
            name = "Коэф. усиления тока для разных фильтров",  OXname="Длина волны пика пропускания, $\lambda$ (нм)", OYname="Коэф. усиления тока ЭОП")
    #gorisLine(K_filt[0], lambda_filt)
#.........


if 6 in N: #Все спектры на одном графике
    linGraf(lambda_array, intensity_zhzs_array, show_trendline=False, create_plot=True,
            OXname="Длина волны, $\lambda$, нм", OYname="Интенсивность I, у.е.",
            name="Cпектры источника через разные фильтры", flabel="Желто-зеленый фильтр", fcolor="yellowgreen")

    linGraf(lambda_array, intensity_os_array, show_trendline=False, create_plot=False,
            OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Спектр источника через красный фильтр",
            flabel="Красный фильтр", fcolor="r")

    linGraf(lambda_array, intensity_fs_array, show_trendline=False, create_plot=False,
            OXname="Длина волны, $\lambda$ (нм)",
            OYname="Интенсивность I, у.е.", name="Спектр источника через синий фильтр",
            flabel="Синий фильтр", fcolor="b")

if 7 in N: #Все откалиброванные спектр на одном графике (да, в правой части графика должен быть треш)
    linGraf(lambda_array, intensity_zhzs_colibr, show_trendline=False, create_plot=True,
            OXname="Длина волны, $\lambda$, нм", OYname="Интенсивность I, у.е.",
            name="Калиброванные спектры источника через разные фильтры", flabel="Желто-зеленый фильтр", fcolor="yellowgreen")

    linGraf(lambda_array, intensity_os_colibr, show_trendline=False, create_plot=False,
            OXname="Длина волны, $\lambda$, нм",
            OYname="Интенсивность I, у.е.", name="Спектр источника через красный фильтр",
            flabel="Красный фильтр", fcolor="r")

    linGraf(lambda_array, intensity_fs_colibr, show_trendline=False, create_plot=False,
            OXname="Длина волны, $\lambda$, нм",
            OYname="Интенсивность I, у.е.", name="Калиброванные спектры источника через синий фильтр",
            flabel="Синий фильтр", fcolor="b")

if 8 in N: #Спектральная чувствитеьность фотокатода, сравниваем с фоточкой из слайдов
    linGraf(lambda_filt, A, form = '.', show_trendline=False, MNKlinestyle='-', create_plot=True,
            OYname = "Спектральная чувствительность, у.е.",  OXname="Длина волны пика пропускания, $\lambda$ (нм)",
            name="Зависимость чувствительности фотокатода от длины волны", ms = 10)


plt.show()

