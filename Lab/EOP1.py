import numpy as np
from semmakkon import *

def get_intensity(File_path):
    EOP_int = read_table_from_file(File_path, row_separator='\t')
    intensity = list_to_float_array(transpose_table(EOP_int)[2])
    return(intensity)


# Функция для чтения данных из файла и записи в список
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split()
            data.append([float(value) for value in values])
    return np.array(data)

# Пути к файлам
file_paths = {
    "EOPbase": "Data/EOPbase",
    "EOPnorm": "Data/EOPnorm",
    "EOPdark": "Data/EOPdark"
}

# Чтение данных из файлов
data = {}
for key, path in file_paths.items():
    data[key] = read_data(path)

# Разделение данных на соответствующие списки
Umkp_base = data["EOPbase"][:, 0]
Ic_base = data["EOPbase"][:, 1]
Is_base = data["EOPbase"][:, 2]

Umkp_norm = data["EOPnorm"][:, 0]
Ic_norm = data["EOPnorm"][:, 1]
Is_norm = data["EOPnorm"][:, 2]

Umkp_dark = data["EOPdark"][:, 0]
Ic_dark = data["EOPdark"][:, 1]
Is_dark = data["EOPdark"][:, 2]

Ic_norm_mod = Ic_norm - Ic_base[:len(Ic_norm)]
Is_norm_mod = Is_norm - Is_base[:len(Is_norm)]
Ic_dark_mod = Ic_dark - Ic_base[len(Is_norm)-2:]
Is_dark_mod = Is_dark - Is_base[len(Is_norm)-2:]

K_norm_I = Is_norm_mod/Ic_norm_mod
K_dark_I = Is_dark_mod/Ic_dark_mod

zero_intensity = 17

intensity_norm = get_intensity("Data/EOPintNorm")
intensity_norm2 = get_intensity("Data/EOPintNorm2")
intensity_dark = get_intensity("Data/EOPintDark")

K0_norm = K_norm_I[0]
K0_dark = K_dark_I[0]


def get_K_B(unmod_intensity, K0):
    intensity = unmod_intensity-zero_intensity
    I0 = intensity[0]/K0
    K_B = intensity/I0
    return(K_B)

K_norm_B = get_K_B(intensity_norm, K0_norm)
K_dark_B = get_K_B(intensity_dark, K0_dark)

EOP_filt = transpose_table(read_table_from_file("Data/EOPfilt"))
Is_filt = toArray(list_to_float_array(EOP_filt[2]))
Ic_filt = toArray(list_to_float_array(EOP_filt[1]))
K_filt = Is_filt/Ic_filt

lambda_filt = [450, 540, 600] #Пики в спектрах



N = [1, 2, 3, 4, 5]
#Препу вроде нравятся точки, если хотите ломанную линию уберите form = '.'

if 1 in N: #Коэф. усиления тока на ЭОП от Напряжение на МКП
    linGraf(Umkp_norm, K_norm_I, show_trendline=False, create_plot=True, name = "$K(U_{мкп})$",
             OXname="Напряжение на МКП, $U_{мкп}$ (кВ)", OYname="Коэф. усиления тока на ЭОП, K",
            flabel="Без темного фильтра", form = '.')
    linGraf(Umkp_dark, K_dark_I, show_trendline=False, flabel="с темным фильтром", form = '.')

if 2 in N: #Логарифм коэф. усиления от Напряжение на МКП
    linGraf(Umkp_norm, np.log(K_norm_I), show_trendline=True, create_plot=True, name = "$ln(K)(U_{мкп})$",
             OXname="Напряжение на МКП, $U_{мкп}$ (кВ)", OYname="Логарифм коэф. усиления, ln(K)",
            flabel="Без темного фильтра", xsize=[0, Umkp_dark[-1]], ysize=[0, np.log(K_dark_I)[-1]],
            show_trendline_label=True, form = '.')
    linGraf(Umkp_dark, np.log(K_dark_I), show_trendline=False, flabel="с темным фильтром", form = '.')

if 3 in N: #Яркость измеренная по картинкам от Напряжение на МКП
    linGraf(Umkp_norm, intensity_norm, show_trendline=False, name="Яркость от напряжения на МКП",
            OXname="Напряжение на МКП, $U_{мкп}$ (кВ)", OYname="Яркость измеренная по картинкам, у.е.",
            create_plot=True, flabel="Область 1.txt", form = '.')
    linGraf(Umkp_norm, intensity_norm2, show_trendline=False, flabel="Область 2", form = '.')
    #можно с одной областью, тогда уберите второй lingraf и уберите flabel
    gorisLine(zero_intensity, gsize = Umkp_norm, show_label=True)

if 4 in N: #Коэф. усиления на ЭОП от Напряжение на МКП, и по току и по картинкам
    linGraf(Umkp_norm, K_norm_I, show_trendline=False, create_plot=True, name = "$K(U_{мкп})$",
             OXname="Напряжение на МКП, $U_{мкп}$ (кВ)", OYname="Коэф. усиления на ЭОП, K",
            flabel="Тока без темного фильтра", form = '.')
    linGraf(Umkp_dark, K_dark_I, show_trendline=False, flabel="Тока с темным фильтром", form = '.')
    linGraf(Umkp_norm, K_norm_B, show_trendline=False, flabel="Яркости без темного фильтра", form = '.')
    linGraf(Umkp_dark, K_dark_B, show_trendline=False, flabel="Яркости с темным фильтром", form = '.')
if 5 in N: #Логарифм коэф. усиления от Напряжение на МКП, и по току и по картинкам
    linGraf(Umkp_norm, np.log(K_norm_I), show_trendline=True, create_plot=True, name = "$ln(K)(U_{мкп})$",
             OXname="Напряжение на МКП, $U_{мкп}$ (кВ)", OYname="Логарифм коэф. усиления, ln(K)", form = '.',
            flabel="Тока без темного фильтра", xsize=[0, Umkp_dark[-1]], ysize=[0, np.log(K_dark_I)[-1]], show_trendline_label=True)
    linGraf(Umkp_dark, np.log(K_dark_I), show_trendline=False, flabel="Тока с темным фильтром", form = '.')
    linGraf(Umkp_norm, np.log(K_norm_B), show_trendline=False, flabel="Яркости без темного фильтра", form = '.')
    linGraf(Umkp_dark, np.log(K_dark_B), show_trendline=False, flabel="Яркости с темным фильтром", form = '.')


plt.show()


