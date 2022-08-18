import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import numpy as np


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
    print(i * (-4) / 3 + 150)
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

for i, j in zip(X1, Y1):
    print("(", i, ", ", j, ")")
plt.scatter(X1, Y1)
plt.scatter(machine[0], machine[1])
plt.scatter(broken_point[:,0], broken_point[:,1])
plt.show()



###########################################

st_x = []
st_y = []
pre_dist = -1

for i in range(len(X)):
    cur_dist = 0
    if i == len(X) - 1:
        cur_dist = math.pow(X[0] - X[i], 2) + math.pow(Y[0] - Y[i], 2)
    else:
        cur_dist = math.pow(X[i + 1] - X[i], 2) + math.pow(Y[i + 1] - Y[i], 2)
    if cur_dist == 0:
        pre_dist = -1
        continue
    if pre_dist == -1:
        pre_dist = cur_dist
        continue
    if cur_dist > pre_dist * 16 and (cur_dist > math.pow(10, 2) or pre_dist > math.pow(10, 2)):
        j = i + 1
        if i == len(X) - 1:
            j = 0
        machine_cur = math.pow(X[j] - machine[0], 2) + math.pow(Y[j] - machine[1], 2)
        j = i - 1
        if i == 0:
            j = len(X) - 1
        machine_pre = math.pow(X[j] - machine[0], 2) + math.pow(Y[j] - machine[1], 2)
        if machine_pre > math.pow(20, 2) and machine_cur > math.pow(20, 2):
            if machine_cur > machine_pre:
                j = (i + round(len(X) / 12)) % len(X)
                st_x.append(round((X[i] + X[j]) / 2))
                st_y.append(round((Y[i] + Y[j]) / 2))
                print("x , y : ")
                print(X[i], Y[i])
                print(X[j], Y[j])
                print("append : ")
                print(round((X[i] + X[j]) / 2), round((Y[i] + Y[j]) / 2))
                i += round(len(X) / 12)
            elif machine_pre > machine_cur:
                i += 1
                j = i - round(len(X) / 12)
                if j < 0:
                    j += len(X)
                st_x.append(round((X[i] + X[j]) / 2))
                st_y.append(round((Y[i] + Y[j]) / 2))
                print("x , y : ")
                print(X[i], Y[i])
                print(X[j], Y[j])
                print("append : ")
                print(round((X[i] + X[j]) / 2), round((Y[i] + Y[j]) / 2))
            pre_dist = -1
            continue
    pre_dist = cur_dist

print("st : ")

if len(st_x) == 0 or len(st_y) == 0:
    print("st is empty")
else:
    plt.scatter(X, Y, s=5)
    plt.scatter(machine[0], machine[1])
    for i in range(len(st_x)):
        if st_x[i] == 0 and st_y[i] == 0:
            continue
        print(st_x[i], st_y[i])
        plt.scatter(st_x[i], st_y[i])
    plt.show()
