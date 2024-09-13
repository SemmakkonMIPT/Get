import matplotlib.pyplot as plt
from math import *
import numpy as np
from tabulate import tabulate

'''
Ваш файл Python содержит следующие функции:

toArray(list) - Преобразует список в массив NumPy.

osiKord(l1, l2) - Рисует оси координат на графике, используя минимальные и максимальные значения списков l1 и l2.

MNK(x, y) - Вычисляет параметры метода наименьших квадратов для линейной зависимости.

sred(l) - Вычисляет среднее значение и стандартное отклонение списка значений.

linGraf(...) - Строит график с возможностью добавления error bar, линии тренда, подписей и других элементов.

gorisLine(A, gsize, linestyle, show_label) - Рисует горизонтальную линию на заданной высоте A с возможностью добавления подписи.

plotEL(A, B) - Рисует эллипс на плоскости.

plotELd(A, B, C) - Рисует дискретизированный трёхмерный эллипс.

plotEL3d(A, B, C) - Рисует трёхмерный эллипс вдоль оси Z.

Elips(A, B, n, fcolor) - Рисует двумерный эллипс на плоскости.

ZElips3d(A, B, C, n, fcolor) - Рисует трёхмерный эллипс вдоль оси Z.

YElips3d(A, B, C, n, fcolor) - Рисует трёхмерный эллипс вдоль оси Y.

XElips3d(A, B, C, n, fcolor) - Рисует трёхмерный эллипс вдоль оси X.

Elipsoid(A, B, C, n) - Рисует трёхмерный эллипсоид, создавая эллипсы вдоль всех трёх осей.

ZHiperbaloid(A, B, C, n) - Рисует трёхмерный гиперболоид вдоль оси Z.

dotEllArrZ(A, B, C, n) - Создаёт точки для отображения эллипса вдоль оси Z.

RaddotEllArrZ(A, B, C, n) - Создаёт радиально распределённые точки для эллипса вдоль оси Z.

dotEllZ(A, B, C, n, fcolor) - Рисует точки для трёхмерного эллипса на графике.

dotEllidArrZ(A, B, C, n, m) - Создаёт дискретизированный массив точек для трёхмерного эллипса.

RaddotEllidArrZ(A, B, C, n, m) - Создаёт радиально и углово распределённые точки для трёхмерного эллипса.

dotEllidZ(A, B, C, n, m, fcolor) - Рисует дискретизированные точки для трёхмерного эллипса.

dotEllidY(A, B, C, n, m, fcolor) - Рисует дискретизированные точки для трёхмерного эллипса вдоль оси Y.

ArrPlot(Arr, fcolor, O) - Отображает массив точек на графике с заданным цветом и смещением.

makeMash(n) - Создаёт и отображает массив точек в форме кубической сетки.

Graf3dArr(A, B, fun, C, D, n) - Генерирует трёхмерный массив точек для функции fun.

swapXZ(Arr) - Обменивает местами оси X и Z в массиве точек.

swapYZ(Arr) - Обменивает местами оси Y и Z в массиве точек.

swapXY(Arr) - Обменивает местами оси X и Y в массиве точек.

AllSwaps(Arr) - Генерирует все возможные перестановки осей в массиве точек.

read_table_from_file(file_path, skip_rows, number_separator, row_separator, isFloat) - Читает данные из файла и преобразует их в таблицу.

print_table(table) - Выводит таблицу в консоль.

transpose_table(table) - Транспонирует таблицу.

list_to_float_array(list) - Преобразует список строк в массив вещественных чисел.

integral(list, l, r) - Вычисляет интеграл данных в массиве.

degCos(array) - Вычисляет косинус углов в градусах, преобразованных в радианы.

def minutes_to_degrees(Deg, Min) - преобразует градусы и минуты в дробные градусы.


'''

def toArray(list):
    arr = np.array(list)
    return arr
def osiKord(l1, l2):
    x1 = min(l1)
    x2 = max(l1)
    y1 = min(l2)
    y2 = max(l2)
    plt.plot([x1, x2], [0, 0], color = 'k')
    plt.plot([0, 0], [y1, y2], color = 'k')

def MNK(x, y):
    n = len(x)
    sX = 0
    sY = 0
    sXY = 0
    sXX = 0
    sYY = 0
    for i in range(n):
        X = x[i]
        Y = y[i]
        sX += X/n
        sY += Y/n
        sXY += X*Y/n
        sXX += X*X/n
        sYY += Y*Y/n
    b = (sXY-sX*sY)/(sXX-sX**2)
    a = sY-b*sX
    sb = 1/n**0.5*((sYY-sY**2)/(sXX-sX**2)-b**2)**0.5
    sa = sb*(sXX-sX**2)**0.5
    return [b, a, sb, sa]

def sred(l):
    n = len(l)
    N = n if n>=10 else n-1
    s = sum(l)/n
    x = 0
    for i in l:
        x+=(i-s)**2
    sx = (x/N)**0.5
    return ([s, sx])


# def linGraf2(X, Y, Xerr = None, Yerr = None, tipe = [0], plsize = 1.txt, fcolor = None, OXname = None,
#             OYname = None, name = None, gsize = [],  flabel = None, form = '', ms = 5,
#             grid = True, mnkcolor = None, ecolor = None, ):
#     Label = flabel
#     if 0 in tipe:
#         fig, ax = plt.subplots()
#         ax.set(title = name, xlabel = OXname, ylabel = OYname)
#         if grid:
#             ax.grid()
#     plt.errorbar(X, Y, xerr=Xerr, yerr=Yerr, ecolor = ecolor if ecolor!=None else fcolor,
#                  c = fcolor, fmt = form, label = Label, ms = ms)
#     K = MNK(X, Y)
#
#     if gsize == []:
#         Right, Left = max(X), min(X)
#     else:
#         Right, Left = max(gsize), min(gsize)
#
#     MNKcolor = mnkcolor if mnkcolor != None else fcolor
#     if 2 not in tipe:
#         x = np.arange(Left, Right, (Right - Left)*0.0001)
#         plt.plot(x, K[1.txt]+K[0]*x, linewidth = plsize, color = MNKcolor)
#     return(MNK(X, Y))


def linGraf(X, Y, Xerr=None, Yerr=None, create_plot=False, show_errorbar=True, show_trendline=True,
            plsize=1, fcolor=None, OXname=None, OYname=None, name=None, xsize=[], ysize = [],  flabel=None,
            form='', ms=5, grid=True, mnkcolor=None, ecolor=None, show_label=None, show_trendline_label = False,
            show = False, MNKlinestyle = None, show_exp_trendline = False, round_label = 2):
    """
    Построение графика с опциональными параметрами.

    Параметры:
        X (list): Данные для построения по оси X.
        Y (list): Данные для построения по оси Y.
        Xerr (list, optional): Массив с ошибками по оси X для каждой точки.
        Yerr (list, optional): Массив с ошибками по оси Y для каждой точки.
        create_plot (bool, optional): Создавать ли отдельный график.
        show_errorbar (bool, optional): Строить ли errorbar.
        show_trendline (bool, optional): Строить ли линию тренда.
        plsize (int, optional): Толщина линии тренда.
        fcolor (str, optional): Цвет точек и линии тренда.
        OXname (str, optional): Название оси X.
        OYname (str, optional): Название оси Y.
        name (str, optional): Название графика.
        xsize (list, optional): Диапазон для построения линии тренда по оси x.
        ysize (list, optional): Диапазон для построения линии тренда по оси y.
        flabel (str, optional): Метка для легенды.
        form (str, optional): Формат точек.
        ms (int, optional): Размер точек.
        grid (bool, optional): Отображение сетки на графике.
        mnkcolor (str, optional): Цвет линии тренда.
        ecolor (str, optional): Цвет ошибок.
        show_label (bool, optional): Добавлять ли метку для легенды.
        MNKlinestyle вид линии тренда

    Возвращает:
        list: Параметры метода наименьших квадратов [b, a, sb, sa].
    """
    if flabel is not None:
        show_label = True if show_label is None else show_label
    else:
        show_label = False if show_label is None else show_label

    if create_plot:
        fig, ax = plt.subplots()
        ax.set(title=name, xlabel=OXname, ylabel=OYname)
        if grid:
            ax.grid()

    if show_errorbar:
        plt.errorbar(X, Y, xerr=Xerr, yerr=Yerr, ecolor=ecolor if ecolor is not None else fcolor,
                     c=fcolor, fmt=form, label=flabel, ms=ms)

    K = MNK(X, Y)
    if show_trendline:
        if xsize == [] and ysize == []:
            Right, Left = max(X), min(X)
        elif ysize == []:
            Right, Left = max(xsize), min(xsize)
        elif xsize == []:
            xysize = toArray(ysize)/K[0]-K[1]/K[0]
            yRight, yLeft = max(xysize), min(xysize)
            Right, Left = yRight, yLeft
        else:
            xRight, xLeft = max(xsize), min(xsize)
            xysize = toArray(ysize)/K[0]-K[1]/K[0]
            yRight, yLeft = max(xysize), min(xysize)
            if xRight<yLeft or xLeft >yRight:
                Right, Left = yRight, yLeft
            else:
                Right = min(xRight, yRight)
                Left = max(xLeft, yLeft)
        MNKcolor = mnkcolor if mnkcolor is not None else fcolor
        x = np.arange(Left, Right, (Right - Left) * 0.0001)
        y = K[1] + K[0] * x

        if show_trendline_label:
            plt.plot(x, y, linewidth=plsize, color=MNKcolor, linestyle = MNKlinestyle,
                     label = "y = " + ((str(round_small(K[0], round_label))+ '$\cdot$'+ "x + ")if K[0]!=0 else "")
                             + str(round_small(K[1], round_label)))
        else:
            plt.plot(x, y, linewidth=plsize, color=MNKcolor, linestyle = MNKlinestyle)

    if show_exp_trendline:
        expK = MNK(X, np.log(toArray(Y)))
        if xsize == [] and ysize == []:
            Right, Left = max(X), min(X)
        else:
            Right, Left = max(xsize), min(xsize)

        MNKcolor = mnkcolor if mnkcolor is not None else fcolor
        x = np.arange(Left, Right, (Right - Left) * 0.0001)
        y = np.exp((expK[1] + expK[0] * x))

        if show_trendline_label:
            plt.plot(x, y, linewidth=plsize, color=MNKcolor, linestyle = MNKlinestyle,
                     label = "y = " + (str(exp(expK[1]))) + ('' if expK[0] == 0 else "$\cdot e^{expK[0] x}$"))
        else:
            plt.plot(x, y, linewidth=plsize, color=MNKcolor, linestyle = MNKlinestyle)


    if (show_label and flabel is not None) or show_trendline_label:
        plt.legend()
    if show:
        plt.show()

    return MNK(X, Y)

def gorisLine(A, gsize, linestyle = '--', show_label = False):
    linGraf([0, 1], [A, A], xsize = gsize, MNKlinestyle=linestyle, show_errorbar=False, show_label = show_label, show_trendline_label=True)
def plotEL(A, B):
    x = np.arange(-(1/A)**0.5, (1/A)**0.5, 0.00001)
    plt.plot(x, ((1-A*x**2)/B)**0.5, color = 'b')
    plt.plot(x, -((1-A*x**2)/B)**0.5, color = 'b')

def plotELd(A, B, C):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    '''
    x = np.arange(-(1.txt / A) ** 0.5, (1.txt / A) ** 0.5, 0.00001)
    plt.plot(x, ((1.txt - A * x ** 2) / B) ** 0.5, 0*x, color='b')
    plt.plot(x, -((1.txt - A * x ** 2) / B) ** 0.5, 0*x, color='b')
    '''
    z = np.linspace(-(1 / C) ** 0.5, (1 / C) ** 0.5, 20)
    for c in z:
        a = (A**2+(c/C*A)**2)**0.5
        b = (B**2+(c/C*B)**2)**0.5

        plotEL3d(a, b, c)


def plotEL3d(A, B, C):
    x = np.linspace(-(1 / A) ** 0.5, (1 / A) ** 0.5, 10)
    plt.plot(x, ((1 - A * x ** 2) / B) ** 0.5, 0 * x + C, color='b')
    plt.plot(x, -((1 - A * x ** 2) / B) ** 0.5, 0 * x + C, color='b')

def Elips(A, B, n=100, fcolor='b'):
    x = np.linspace(-A, A, n)
    plt.plot(x, B * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)
    plt.plot(x, -B * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)
def ZElips3d(A, B, C, n=50, fcolor='b'):
    x = np.linspace(-A, A, n)
    plt.plot(x, B * (1 - x ** 2 / A ** 2) ** 0.5, x*0 + C, color=fcolor)
    plt.plot(x, -B * (1 - x ** 2 / A ** 2) ** 0.5, x*0 + C, color=fcolor)

def YElips3d(A, B, C, n=50, fcolor='b'):
    x = np.linspace(-A, A, n)
    plt.plot(x, x*0 + B, C * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)
    plt.plot(x, x*0 + B, -C * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)

def XElips3d(A, B, C, n=50, fcolor='b'):
    y = np.linspace(-B, B, n)
    plt.plot(y*0 + A, y, C * (1 - y ** 2 / B ** 2) ** 0.5, color=fcolor)
    plt.plot(y*0 + A, y, -C * (1 - y ** 2 / B ** 2) ** 0.5, color=fcolor)

def ZWayElipsoid(A, B, C, n=5):
    z = np.linspace(-C, C, n)
    for c in z:
        a = (A ** 2 - (c / C * A) ** 2) ** 0.5
        b = (B ** 2 - (c / C * B) ** 2) ** 0.5
        ZElips3d(a, b, c)

def YWayElipsoid(A, B, C, n=5):
    y = np.linspace(-B, B, n)
    for b in y:
        a = (A ** 2 - (b / B * A) ** 2) ** 0.5
        c = (C ** 2 - (b / B * C) ** 2) ** 0.5
        YElips3d(a, b, c)

def XWayElipsoid(A, B, C, n=5):
    x = np.linspace(-A, A, n)
    for a in x:
        b = (B ** 2 - (a / A * B) ** 2) ** 0.5
        c = (C ** 2 - (a / A * C) ** 2) ** 0.5
        XElips3d(a, b, c)

def Elipsoid(A, B, C, n=5):
    XWayElipsoid(A, B, C, n=n)
    YWayElipsoid(A, B, C, n=n)
    ZWayElipsoid(A, B, C, n=n)

def ZHiperbaloid(A, B, C, n=10):
    z = np.linspace(-C, C, n)
    for c in z:
        a = (A ** 2 + (c / C * A) ** 2) ** 0.5
        b = (B ** 2 + (c / C * B) ** 2) ** 0.5
        ZElips3d(a, b, c)

def dotEllArrZ(A, B, C, n=5):
    x = np.linspace(-A/2**0.5, A/2**0.5, n)
    y = np.linspace(-B/2**0.5, B/2**0.5, n)
    Y = np.concatenate([B * (1 - x ** 2 / A ** 2) ** 0.5, -B * (1 - x ** 2 / A ** 2) ** 0.5, y, y])
    X = np.concatenate([x, x, A * (1 - y ** 2 / B ** 2) ** 0.5, -A * (1 - y ** 2 / B ** 2) ** 0.5])
    Z = np.ones(4*n)*C
    Arr = np.array([X, Y, Z])
    return Arr

def RaddotEllArrZ(A, B, C, n=5):
    F = np.linspace(0, 2*pi, 4*n)
    X = np.cos(F)*A
    Y = np.sin(F)*B
    Z = np.ones(4 * n) * C
    Arr = np.array([X, Y, Z])
    return Arr

def dotEllZ(A, B, C, n=5, fcolor = 'b'):
    Arr = dotEllArrZ(A, B, C, n)
    plt.plot(Arr[0], Arr[1], Arr[2], color = fcolor, linestyle = ' ', marker = '.', markeredgewidth = 0.1)
def dotEllidArrZ(A, B, C, n=5, m=10):
    z = np.linspace(-C, C, m)
    Arr = np.array([[0, 0], [0, 0], [C, -C]])
    X = dotEllArrZ(A, B, 0, n)[0]
    Y = dotEllArrZ(A, B, 0, n)[1]
    for c in z:
        a = (A ** 2 - (c / C * A) ** 2) ** 0.5
        b = (B ** 2 - (c / C * B) ** 2) ** 0.5
        newArr = dotEllArrZ(a, b, c, n)
        Arr = np.hstack([Arr, newArr])
    return Arr

def RaddotEllidArrZ(A, B, C, n=5, m=10):
    z = np.linspace(0, pi, m)
    Arr = np.array([[0, 0], [0, 0], [C, -C]])
    X = RaddotEllArrZ(A, B, 0, n)[0]
    Y = RaddotEllArrZ(A, B, 0, n)[1]
    for c in z:
        a = np.sin(c)*A
        b = np.sin(c)*B
        newArr = dotEllArrZ(a, b, cos(c)*C, n)
        Arr = np.hstack([Arr, newArr])
    return Arr

def dotEllidZ(A, B, C, n=5, m=7, fcolor = 'b'):
    Arr = dotEllidArrZ(A, B, C, n=n, m=m)
    plt.plot(Arr[0], Arr[1], Arr[2], color = fcolor, linestyle = ' ', marker = '.', markeredgewidth = 0.1)

def dotEllidY(A, B, C, n=5, m=10, fcolor = 'b'):
    Arr = dotEllidArrZ(A, C, B, n=5, m=10)
    plt.plot(Arr[0], Arr[2], Arr[1], color = fcolor, linestyle = ' ', marker = '.', markeredgewidth = 0.1)

def ArrPlot(Arr, fcolor = 'b', O = [0, 0, 0]):
    plt.plot(Arr[0]+O[0], Arr[1]+O[1], Arr[2]+O[2], color=fcolor, linestyle=' ', marker='.', markeredgewidth=0.1)

def makeMash(n):
    Arr = np.array([[n, n, n, n, -n, -n, -n, -n], [n, n, -n, -n, n, n, -n, -n], [n, -n, n, -n, n, -n, n, -n]])
    print(Arr)
    ArrPlot(Arr)

def Graf3dArr(A, B, fun, C = None, D = None, n = 10):
    if C==None: c = -A
    else: c = C
    if D==None: d = -B
    else: d = D
    X = np.linspace(c, A, n)
    Y = np.linspace(d, B, n)
    Arr = np.array([[], [], []])
    for x in X:
        for y in Y:
            newArr = np.array([[x], [y], [fun(x, y)]])
            Arr = np.hstack([Arr, newArr])
    return Arr

def swapXZ(Arr):
    newArr = np.array([Arr[2], Arr[1], Arr[0]])
    return newArr

def swapYZ(Arr):
    newArr = np.array([Arr[0], Arr[2], Arr[1]])
    return newArr
def swapXY(Arr):
    newArr = np.array([Arr[1], Arr[0], Arr[2]])
    return newArr

def AllSwaps(Arr):
    newArr = Arr
    newArr = np.hstack([newArr, swapXY(Arr)])
    newArr = np.hstack([newArr, swapXZ(Arr)])
    newArr = np.hstack([newArr, swapYZ(Arr)])
    return newArr

def read_table_from_file(file_path, skip_rows=0, number_separator='.', row_separator=' ',
                         isFloat = True, transpose = True, isInt = False):
    table_data = []
    with open(file_path, 'r') as file:
        for _ in range(skip_rows):
            next(file)  # Пропускаем указанное количество строк
        for line in file:
            row = line.strip().split(row_separator)
            # Если разделитель в числах не совпадает с дефолтным, заменяем
            if number_separator != '.':
                row = [cell.replace(number_separator, '.') for cell in row]
            table_data.append(toArray(row).astype(float) if isFloat else toArray(row).astype(int)
            if isInt else toArray(row))
    if transpose:
        table_data = transpose_table(table_data)
    return table_data

def print_table(table):
    for raw in table:
        print(raw)

def transpose_table(table):
    # Получаем количество строк и столбцов в таблице
    num_rows = len(table)
    num_cols = len(table[0])

    # Создаем новую таблицу для транспонированных данных
    transposed_table = []
    for j in range(num_cols):
        transposed_row = []
        for i in range(num_rows):
            transposed_row.append(table[i][j])
        transposed_table.append(transposed_row)

    return toArray(transposed_table)

def list_to_float_array(list):
    array = np.array([float(i) for i in list])
    return array

def integral(list, l = 0, r = None):
    if r == None: r = len(list)
    sum = sum(list[l:r])
    return sum

def degCosArray(array):
    ys = []
    for x in array:
        y = x*pi/180
        ys.append(y)
    ys = toArray(ys)
    return(np.cos(ys))

def degSinArray(array):
    ys = []
    for x in array:
        y = x*pi/180
        ys.append(y)
    ys = toArray(ys)
    return(np.sin(ys))

def degSin(Deg):
    return(sin(Deg*pi/180))

def degCos(Deg):
    return(cos(Deg*pi/180))

def minutes_to_degrees(Deg, Min):
    D = toArray(Deg)
    M = toArray(Min)
    Ans = D+M/60
    return Ans

def round_small(x, n = 2):
    k = 0
    while abs(x) < 1:
        x*=10
        k+=1
        if k > 10: break
    xr = round(x, n)
    if k < 2:
        return(xr)
    else:
        strx = str(xr)+"e"+str(k)
        return strx

