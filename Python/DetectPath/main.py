import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit
import numpy as np
import json
from collections import OrderedDict
import math


def function(x, a, b):
    return a * x + b

def curve_line(x, y):
    # print(x[0], y[0])
    popt, cov = curve_fit(function, [x[0], x[-1]], [y[0], y[-1]])
    a, b = popt
    new_x = []
    new_y = []
    for x_, y_ in zip(x, y):
        t_x1 = x_ - a * (abs(a * x_ - y_ + b) / ((a * a) + 1))
        t_y1 = y_ + (abs(a * x_ - y_ + b) / ((a * a) + 1))
        t_x2 = x_ + a * (abs(a * x_ - y_ + b) / ((a * a) + 1))
        t_y2 = y_ - (abs(a * x_ - y_ + b) / ((a * a) + 1))
        dist1 = abs(a * t_x1 - t_y1 + b) / math.sqrt(a * a + 1)
        dist2 = abs(a * t_x2 - t_y2 + b) / math.sqrt(a * a + 1)
        if dist1 < dist2:
            new_x.append(t_x1)
            new_y.append(t_y1)
        else:
            new_x.append(t_x2)
            new_y.append(t_y2)

    # plt.scatter(x, y, s=5)
    # plt.scatter(new_x, new_y, s=5)
    # plt.plot(x, function(x, *popt))
    return new_x, new_y

def animate(i):
    if i > len(X) - size - 1:
        x = np.array([X[i], X[i + size - len(X)], X[i + 2 * size - len(X)]])
        y = np.array([Y[i], Y[i + size - len(X)], Y[i + 2 * size - len(X)]])
    elif i > len(X) - 2 * size - 1:
        x = np.array([X[i], X[i + size], X[i + 2 * size - len(X)]])
        y = np.array([Y[i], Y[i + size], Y[i + 2 * size - len(X)]])
    else:
        x = np.array([X[i], X[i + size], X[i + 2 * size]])
        y = np.array([Y[i], Y[i + size], Y[i + 2 * size]])
    line.set_data(x, y)
    time_text.set_text('time = %.1f' % i)
    theta_text.set_text('theta = %.3f' % th[i])
    len_text.set_text('len = %.1f' % math.sqrt(X[i] * X[i] + Y[i] * Y[i]))
    return line,

def onClick(event):
    global pause
    if pause:
        ani.event_source.stop()
        pause = False
    else:
        ani.event_source.start()
        pause = True

def show():
    # ########################################################################
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onClick)
    ax.scatter(X, Y, c='blue', s=5)
    ax.set_xlim((-200, 200))
    ax.set_ylim((-200, 200))
    line, = ax.plot([], [], 'o-', lw=2, c='red')
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    theta_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
    len_text = ax.text(0.02, 0.85, '', transform=ax.transAxes)
    ani = FuncAnimation(fig, animate, frames=500)
    plt.figure()
    ########################################################################
    # plt.scatter(np.arange(len(th)), th)
    # plt.xlim(0, 500)
    # plt.figure()
    # ########################################################################
    plt.scatter(X, Y, c='blue', s=5)
    plt.scatter([X[i] for i in point], [Y[i] for i in point], c='red', s=5)
    plt.scatter(machine[0], machine[1])
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    plt.figure()
    # ########################################################################
    # plt.scatter(np.arange(len(length)), length, s=5)
    # plt.figure()
    # ########################################################################
    # plt.scatter(np.arange(len(point)), point)
    # plt.show()

def remove_trash():
    t1 = []
    for i in range(len(X)):
        if i == len(X) - 1:
            next_x = X[0]
            next_y = Y[0]
        else:
            next_x = X[i + 1]
            next_y = Y[i + 1]
        xi = X[i]
        yi = Y[i]
        t1.append(i)
        if abs(X[i] - next_x) > 10 or abs(Y[i] - next_y) > 10:
            if len(t1) < 5:
                for j in t1:
                    X[j] = next_x
                    Y[j] = next_y
            t1 = []

def get_points():
    for i in range(len(X)):
        if i > len(X) - size - 1:
            x1 = X[i] - X[i + size - len(X)]
            y1 = Y[i] - Y[i + size - len(X)]
            x2 = X[i + 2 * size - len(X)] - X[i + size - len(X)]
            y2 = Y[i + 2 * size - len(X)] - Y[i + size - len(X)]
        elif i > len(X) - 2 * size - 1:
            x1 = X[i] - X[i + size]
            y1 = Y[i] - Y[i + size]
            x2 = X[i + 2 * size - len(X)] - X[i + size]
            y2 = Y[i + 2 * size - len(X)] - Y[i + size]
        else:
            x1 = X[i] - X[i + size]
            y1 = Y[i] - Y[i + size]
            x2 = X[i + 2 * size] - X[i + size]
            y2 = Y[i + 2 * size] - Y[i + size]
        ang1 = np.arctan2(x1, y1)
        ang2 = np.arctan2(x2, y2)
        res = np.rad2deg((ang1 - ang2) % (2 * np.pi))
        res = (360 - res) % 360

        th.append(res)
        length.append(math.sqrt(X[i] * X[i] + Y[i] * Y[i]))

        if X[i] != 0 and Y[i] != 0 and (res < 160 or res > 200):
            if i + size >= len(X):
                point.append(i + size - len(X))
            else:
                point.append(i + size)
        if i == len(X) - 1:
            i2 = 0
        else:
            i2 = i + 1
        if abs(X[i] - X[i2]) > 10 or abs(Y[i] - Y[i2]) > 10:
            broken_points.append([i, True])
            broken_points.append([i2, True])
            broken_xy.append([X[i], Y[i]])
            broken_xy.append([X[i2], Y[i2]])

def get_onepoint():
    temp = []
    prev_i = point[0]
    avr = 0
    for i in point:
        if len(X) - size >= abs(prev_i - i) >= 5 or i == point[-1]:
            avr /= len(temp)
            if len(temp) < 5:
                prev_i = i
                temp = [i]
            else:
                dif = 180
                prev_j = temp[0] - 1
                for j in temp:
                    if j - size < 0:
                        th_ang = th[j - size + len(th)]
                    else:
                        th_ang = th[j - size]
                    if avr < 180 and th_ang < dif:
                        dif = th_ang
                        prev_j = j
                    elif avr >= 180 and th_ang > dif:
                        dif = th_ang
                        prev_j = j

                main_point.append([prev_j, False])
                prev_i = i
                temp = [i]
                avr = 0
        elif abs(prev_i - i) < 5 or abs(prev_i - i) >= len(X) - size:
            prev_i = i
            if i - size < 0:
                th_ang = th[i - size + len(th)]
            else:
                th_ang = th[i - size]
            avr += th_ang
            temp.append(i)

def get_curve_point():
    main_point.sort()
    for i in range(len(main_point)):
        if i == len(main_point) - 1:
            i2 = 0
        else:
            i2 = i + 1
        if main_point[i][1] == main_point[i2][1] or abs(main_point[i][0] - main_point[i2][0]) > 5:
            main_point_curve.append(main_point[i2][0])
    main_point_curve.sort()

def get_result():
    nX = []
    nY = []
    for i in range(len(main_point_curve)):
        if i == len(main_point_curve) - 1:
            xdata = np.concatenate((np.array(X[int(main_point_curve[i]):]), np.array(X[:int(main_point_curve[0])])))
            ydata = np.concatenate((np.array(Y[int(main_point_curve[i]):]), np.array(Y[:int(main_point_curve[0])])))
        else:
            xdata = np.array(X[int(main_point_curve[i]):int(main_point_curve[i + 1]) + 1])
            ydata = np.array(Y[int(main_point_curve[i]):int(main_point_curve[i + 1]) + 1])
        if len(xdata) > 2:
            new_x, new_y = curve_line(xdata, ydata)
            nX += new_x[1:]
            nY += new_y[1:]
    return nX, nY
# file_path = "lidardata.json"
# file_path = "rec_with_box.json"
# file_path = "2.json"
file_path = "./words.json"

point = []
th = []
length = []
X = []
Y = []
machine = []
broken_points = []
broken_xy = []
main_point = []
main_point_curve = []
new_x_arr = []
new_y_arr = []
size = 10
pause = False
with open(file_path, 'r') as file:
    data = json.load(file)
    X = data["Lidar_x"]
    Y = data["Lidar_y"]
    machine = data["Location"]
    X[0] = X[2]
    X[1] = X[2]
    Y[0] = Y[2]
    Y[1] = Y[2]

remove_trash()
get_points()
get_onepoint()
main_point = main_point + broken_points
get_curve_point()

st_x = []
st_y = []

print("broken points [0] : ")
print(broken_xy[0][0], broken_xy[0][1])

for i in range(0, len(broken_xy), 2):
    x1 = broken_xy[i][0]
    y1 = broken_xy[i][1]
    x2 = broken_xy[i + 1][0]
    y2 = broken_xy[i + 1][1]
    gap = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    rad = math.atan(20 / (gap / 2))
    ap_x = (x2 - x1) / 2 - (y2 - y1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + x1
    ap_y = (x2 - x1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + (y2 - y1) / 2 + y1

    st_x.append(round(ap_x))
    st_y.append(round(ap_y))

    #print("append ( x, y ) = ")
    #print(round(ap_x), round(ap_y))

#plt.scatter(X1, Y1)
#plt.scatter(machine[0], machine[1])
#plt.scatter(broken_point[:, 0], broken_point[:, 1])
#for i in range(len(st_x)):
#    plt.scatter(st_x[i], st_y[i])
#plt.show()

for i in range(len(st_x)):
    j = 0
    while True:
        if j == len(X):
            break;
        if abs(st_x[i] - X[j]) > 15:
            j += 1
            continue
        if abs(st_y[i] - Y[j]) > 15:
            j += 1
            continue
        if math.pow(st_x[i] - X[j], 2) + math.pow(st_y[i] - Y[j], 2) > math.pow(15, 2):
            j += 1
            continue
        #print("shorter than 15cm : i, j, ( x, y ) = ")
        #print(i, j, st_x[i], st_y[i])
        st_x[i] += round((machine[0] - st_x[i]) * 0.1)
        st_y[i] += round((machine[1] - st_y[i]) * 0.1)
        j = 0

plt.scatter(X, Y, c='blue', s=5)
plt.scatter(machine[0], machine[1], c='yellow', s=20)
plt.scatter([i[0] for i in broken_xy], [i[1] for i in broken_xy], c='red', s=20)
for i in range(len(st_x)):
    plt.scatter(st_x[i], st_y[i], c='orange', s=20)
plt.show()

file_data = OrderedDict()

file_data["st_x"] = st_x[0]
file_data["st_y"] = st_y[0]

with open('./words.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

print(" st_x, st_y : ", st_x[0], st_y[0])