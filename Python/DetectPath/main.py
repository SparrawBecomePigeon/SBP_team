import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import numpy as np
import json
from collections import OrderedDict

def mk_arr(r, num):
    temp = []
    for i in range(r):
        temp.append(num)
    temp = np.array(temp)
    return temp

machine = [0, 0]
X1 = np.array(range(60))
X1 = np.append(X1, mk_arr(130, 60))
X1 = np.append(X1, np.flip(np.array(range(45, 61))))
X1 = np.append(X1, np.flip(np.array(range(-30, 31))))
X1 = np.append(X1, np.flip(np.array(range(-60, -44))))
X1 = np.append(X1, mk_arr(130, -60))
X1 = np.append(X1, np.array(range(-60, 0)))

Y1 = mk_arr(60, -60)
Y1 = np.append(Y1, np.array(range(-60, 71)))
t = []
for i in range(45, 60):
    t.append(i * (-4) / 3 + 150)
Y1 = np.append(Y1, np.flip(np.array(t)))
t = []
Y1 = np.append(Y1, mk_arr(61, 60))
for i in range(-60, -44):
    t.append(i * 4 / 3 + 150)
Y1 = np.append(Y1, np.flip(np.array(t)))
Y1 = np.append(Y1, np.flip(np.array(range(-60, 71))))
Y1 = np.append(Y1, mk_arr(59, -60))

X = X1
Y = Y1
broken_point = [[45, 90], [30, 60], [-30, 60], [-45, 90]]
broken_point = np.array(broken_point)

plt.scatter(X1, Y1)
plt.scatter(machine[0], machine[1])
plt.scatter(broken_point[:,0], broken_point[:,1])
plt.show()

###########################################

st_x = []
st_y = []

for i in range(0, len(broken_point), 2):
    x1 = broken_point[i][0]
    y1 = broken_point[i][1]
    x2 = broken_point[i + 1][0]
    y2 = broken_point[i + 1][1]
    gap = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    rad = math.atan(20 / (gap / 2))
    ap_x = (x2 - x1) / 2 - (y2 - y1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + x1
    ap_y = (x2 - x1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + (y2 - y1) / 2 + y1

    st_x.append(round(ap_x))
    st_y.append(round(ap_y))

    print("append ( x, y ) = ")
    print(round(ap_x), round(ap_y))

plt.scatter(X1, Y1)
plt.scatter(machine[0], machine[1])
plt.scatter(broken_point[:, 0], broken_point[:, 1])
for i in range(len(st_x)):
    plt.scatter(st_x[i], st_y[i])
plt.show()

for i in range(len(st_x)):
    j = 0
    while True:
        if j == len(X1):
            break;
        if abs(st_x[i] - X1[j]) > 15:
            j += 1
            continue
        if abs(st_y[i] - Y1[j]) > 15:
            j += 1
            continue
        if math.pow(st_x[i] - X1[j], 2) + math.pow(st_y[i] - Y1[j], 2) > math.pow(15, 2):
            j += 1
            continue
        print("shorter than 15cm : i, j, ( x, y ) = ")
        print(i, j, st_x[i], st_y[i])
        st_x[i] += round((machine[0] - st_x[i]) * 0.1)
        st_y[i] += round((machine[1] - st_y[i]) * 0.1)
        j = 0


plt.scatter(X1, Y1)
plt.scatter(machine[0], machine[1])
plt.scatter(broken_point[:,0], broken_point[:,1])
for i in range(len(st_x)):
    plt.scatter(st_x[i], st_y[i])
plt.show()

file_data = OrderedDict()

file_data["st_x"] = st_x
file_data["st_y"] = st_y

with open('./words.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

print(" st_x, st_y : ", st_x, st_y)