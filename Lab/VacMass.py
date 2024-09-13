from semmakkon import *

Data = read_table_from_file("DataVac/DataVac2", transpose = False)
x = [1, 2, 3, 4, 5]
fig, ax = plt.subplots()
ax.set(title="", xlabel="", ylabel="")
# ModeData = [[toArray(Data[i])/Data[3]]]

names = read_table_from_file("DataVac/DataVac2Names", isFloat=False, isInt=False)
colors = read_table_from_file("DataVac/DataVac2Colors", isFloat=False, isInt=False, transpose = False)
for i in range(len(Data)):
    # print(line)
    linGraf(x, toArray(Data[i])/toArray(Data[3]), flabel=names[0][i], fcolor = colors[0][i])
    # linGraf(x, toArray(Data[i])/toArray(Data[3]), flabel=names[0][i])

plt.legend()
ax.grid()

plt.show()