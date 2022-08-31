#import matplotlib.pyplot as plt
import numpy
# from scipy.optimize import curve_fit
# import numpy as np
import json
from collections import OrderedDict
import math
import os.path

#
# def function(x, a, b):
#     return a * x + b
#
# def curve_line(x, y):
#     # print(x[0], y[0])
#     popt, cov = curve_fit(function, [x[0], x[-1]], [y[0], y[-1]])
#     a, b = popt
#     new_x = []
#     new_y = []
#     for x_, y_ in zip(x, y):
#         t_x1 = x_ - a * (abs(a * x_ - y_ + b) / ((a * a) + 1))
#         t_y1 = y_ + (abs(a * x_ - y_ + b) / ((a * a) + 1))
#         t_x2 = x_ + a * (abs(a * x_ - y_ + b) / ((a * a) + 1))
#         t_y2 = y_ - (abs(a * x_ - y_ + b) / ((a * a) + 1))
#         dist1 = abs(a * t_x1 - t_y1 + b) / math.sqrt(a * a + 1)
#         dist2 = abs(a * t_x2 - t_y2 + b) / math.sqrt(a * a + 1)
#         if dist1 < dist2:
#             new_x.append(t_x1)
#             new_y.append(t_y1)
#         else:
#             new_x.append(t_x2)
#             new_y.append(t_y2)
#
#     # plt.scatter(x, y, s=5)
#     # plt.scatter(new_x, new_y, s=5)
#     # plt.plot(x, function(x, *popt))
#     return new_x, new_y
#
# def animate(i):
#     if i > len(X) - size - 1:
#         x = np.array([X[i], X[i + size - len(X)], X[i + 2 * size - len(X)]])
#         y = np.array([Y[i], Y[i + size - len(X)], Y[i + 2 * size - len(X)]])
#     elif i > len(X) - 2 * size - 1:
#         x = np.array([X[i], X[i + size], X[i + 2 * size - len(X)]])
#         y = np.array([Y[i], Y[i + size], Y[i + 2 * size - len(X)]])
#     else:
#         x = np.array([X[i], X[i + size], X[i + 2 * size]])
#         y = np.array([Y[i], Y[i + size], Y[i + 2 * size]])
#     line.set_data(x, y)
#     time_text.set_text('time = %.1f' % i)
#     theta_text.set_text('theta = %.3f' % th[i])
#     len_text.set_text('len = %.1f' % math.sqrt(X[i] * X[i] + Y[i] * Y[i]))
#     return line,
#
# def onClick(event):
#     global pause
#     if pause:
#         ani.event_source.stop()
#         pause = False
#     else:
#         ani.event_source.start()
#         pause = True
#
# def show():
#     # ########################################################################
#     fig, ax = plt.subplots()
#     fig.canvas.mpl_connect('button_press_event', onClick)
#     ax.scatter(X, Y, c='blue', s=5)
#     ax.set_xlim((-200, 200))
#     ax.set_ylim((-200, 200))
#     line, = ax.plot([], [], 'o-', lw=2, c='red')
#     time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
#     theta_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
#     len_text = ax.text(0.02, 0.85, '', transform=ax.transAxes)
#     ani = FuncAnimation(fig, animate, frames=500)
#     plt.figure()
#     ########################################################################
#     # plt.scatter(np.arange(len(th)), th)
#     # plt.xlim(0, 500)
#     # plt.figure()
#     # ########################################################################
#     plt.scatter(X, Y, c='blue', s=5)
#     plt.scatter([X[i] for i in point], [Y[i] for i in point], c='red', s=5)
#     plt.scatter(machine[0], machine[1])
#     plt.xlim(-200, 200)
#     plt.ylim(-200, 200)
#     plt.figure()
#     # ########################################################################
#     # plt.scatter(np.arange(len(length)), length, s=5)
#     # plt.figure()
#     # ########################################################################
#     # plt.scatter(np.arange(len(point)), point)
#     # plt.show()
#
# def remove_trash():
#     t1 = []
#     for i in range(len(X)):
#         if i == len(X) - 1:
#             next_x = X[0]
#             next_y = Y[0]
#         else:
#             next_x = X[i + 1]
#             next_y = Y[i + 1]
#         xi = X[i]
#         yi = Y[i]
#         t1.append(i)
#         if abs(X[i] - next_x) > 10 or abs(Y[i] - next_y) > 10:
#             if len(t1) < 5:
#                 for j in t1:
#                     X[j] = next_x
#                     Y[j] = next_y
#             t1 = []
#
# def get_points():
#     for i in range(len(X)):
#         if i > len(X) - size - 1:
#             x1 = X[i] - X[i + size - len(X)]
#             y1 = Y[i] - Y[i + size - len(X)]
#             x2 = X[i + 2 * size - len(X)] - X[i + size - len(X)]
#             y2 = Y[i + 2 * size - len(X)] - Y[i + size - len(X)]
#         elif i > len(X) - 2 * size - 1:
#             x1 = X[i] - X[i + size]
#             y1 = Y[i] - Y[i + size]
#             x2 = X[i + 2 * size - len(X)] - X[i + size]
#             y2 = Y[i + 2 * size - len(X)] - Y[i + size]
#         else:
#             x1 = X[i] - X[i + size]
#             y1 = Y[i] - Y[i + size]
#             x2 = X[i + 2 * size] - X[i + size]
#             y2 = Y[i + 2 * size] - Y[i + size]
#         ang1 = np.arctan2(x1, y1)
#         ang2 = np.arctan2(x2, y2)
#         res = np.rad2deg((ang1 - ang2) % (2 * np.pi))
#         res = (360 - res) % 360
#
#         th.append(res)
#         length.append(math.sqrt(X[i] * X[i] + Y[i] * Y[i]))
#
#         if X[i] != 0 and Y[i] != 0 and (res < 160 or res > 200):
#             if i + size >= len(X):
#                 point.append(i + size - len(X))
#             else:
#                 point.append(i + size)
#         if i == len(X) - 1:
#             i2 = 0
#         else:
#             i2 = i + 1
#         if abs(X[i] - X[i2]) > 10 or abs(Y[i] - Y[i2]) > 10:
#             broken_points.append([i, True])
#             broken_points.append([i2, True])
#             broken_xy.append([X[i], Y[i]])
#             broken_xy.append([X[i2], Y[i2]])
#
# def get_onepoint():
#     temp = []
#     prev_i = point[0]
#     avr = 0
#     for i in point:
#         if len(X) - size >= abs(prev_i - i) >= 5 or i == point[-1]:
#             avr /= len(temp)
#             if len(temp) < 5:
#                 prev_i = i
#                 temp = [i]
#             else:
#                 dif = 180
#                 prev_j = temp[0] - 1
#                 for j in temp:
#                     if j - size < 0:
#                         th_ang = th[j - size + len(th)]
#                     else:
#                         th_ang = th[j - size]
#                     if avr < 180 and th_ang < dif:
#                         dif = th_ang
#                         prev_j = j
#                     elif avr >= 180 and th_ang > dif:
#                         dif = th_ang
#                         prev_j = j
#
#                 main_point.append([prev_j, False])
#                 prev_i = i
#                 temp = [i]
#                 avr = 0
#         elif abs(prev_i - i) < 5 or abs(prev_i - i) >= len(X) - size:
#             prev_i = i
#             if i - size < 0:
#                 th_ang = th[i - size + len(th)]
#             else:
#                 th_ang = th[i - size]
#             avr += th_ang
#             temp.append(i)
#
# def get_curve_point():
#     main_point.sort()
#     for i in range(len(main_point)):
#         if i == len(main_point) - 1:
#             i2 = 0
#         else:
#             i2 = i + 1
#         if main_point[i][1] == main_point[i2][1] or abs(main_point[i][0] - main_point[i2][0]) > 5:
#             main_point_curve.append(main_point[i2][0])
#     main_point_curve.sort()
#
# def get_result():
#     nX = []
#     nY = []
#     for i in range(len(main_point_curve)):
#         if i == len(main_point_curve) - 1:
#             xdata = np.concatenate((np.array(X[int(main_point_curve[i]):]), np.array(X[:int(main_point_curve[0])])))
#             ydata = np.concatenate((np.array(Y[int(main_point_curve[i]):]), np.array(Y[:int(main_point_curve[0])])))
#         else:
#             xdata = np.array(X[int(main_point_curve[i]):int(main_point_curve[i + 1]) + 1])
#             ydata = np.array(Y[int(main_point_curve[i]):int(main_point_curve[i + 1]) + 1])
#         if len(xdata) > 2:
#             new_x, new_y = curve_line(xdata, ydata)
#             nX += new_x[1:]
#             nY += new_y[1:]
#     return nX, nY

def getEquidistantPoints(p1, p2, parts):
    return [numpy.linspace(p1[0], p2[0], parts+1).tolist(),
               numpy.linspace(p1[1], p2[1], parts+1).tolist()]

def my_algo():
    X = [] # 현재 측정한 Lidar_x
    Y = [] # 현재 측정한 Lidar_y
    machine = [] # 머신 위치 [x, y]

    main_X = [] # x축 맵을 선으로 저장 [시작, 끝]
    main_Y = [] # y축 맵을 선으로 저장 [시작, 끝]

    main_point_X = [] # x 전체 맵을 점으로 저장
    main_point_Y = [] # y 전체 맵을 점으로 저장

    #
    #
    # file_path = "./testcase/2022-8-27_11_8_0.json"
    #
    # with open(file_path, 'r') as f:
    #     data = json.load(f)
    #     X = data["Lidar_x"]
    #     Y = data["Lidar_y"]
    #     machine = data["Location"]
    #     X[0] = X[2]
    #     X[1] = X[2]
    #     Y[0] = Y[2]
    #     Y[1] = Y[2]
    #     for i in range(len(X)):
    #         X[i] = round(X[i])
    #         Y[i] = round(Y[i])
    #
    # px = []
    # gap = 0
    #
    # for i in range(len(X)):
    #     gap = 15
    #     len1 = math.sqrt(math.pow(X[i], 2) + math.pow(Y[i], 2))
    #     gap = gap - round(len1 / 50)
    #     if gap <= 2:
    #         gap == 2
    #     print(gap)
    #     bi = i - gap
    #     ni = i + gap
    #     if bi < 0:
    #         bi += len(X)
    #     if ni >= len(X):
    #         ni -= len(X)
    #     x1 = X[bi] - X[i]
    #     y1 = Y[bi] - Y[i]
    #     x2 = X[ni] - X[i]
    #     y2 = Y[ni] - Y[i]
    #     p21 = math.sqrt(math.pow(x1, 2) + math.pow(y1, 2))
    #     p23 = math.sqrt(math.pow(x2, 2) + math.pow(y2, 2))
    #     comb = round(abs((x1 * y2) - (y1 * x2)))
    #     div = round(abs(p21 * p23))
    #     if div == 0 or comb == 0 or div == comb:
    #         continue
    #     deg = math.degrees(math.asin(comb / div))
    #     if deg > 30:
    #         px.append(i)
    # X1 = []
    # for i in range(len(X) - 1):
    #     gap = 30
    #     len1 = math.sqrt(math.pow(X[i], 2) + math.pow(Y[i], 2))
    #     gap = gap - round(1500 / len1)
    #     if gap < 10:
    #         gap = 10
    #     if math.pow(X[i] - X[i + 1], 2) + math.pow(Y[i] - Y[i + 1], 2) > math.pow(gap, 2):
    #         X1.append(i)
    #         X1.append(i + 1)
    #
    # pltpx = []
    # pltpy = []
    # for i in range(len(px)):
    #     pltpx.append(X[px[i]])
    #     pltpy.append(Y[px[i]])
    # pltX1 = []
    # pltY1 = []
    # for i in range(len(X1)):
    #     pltX1.append(X[X1[i]])
    #     pltY1.append(Y[X1[i]])
    #
    # plt.title("px")
    # plt.scatter(X, Y, c='blue', s=5)
    # plt.scatter(pltpx, pltpy, c='red', s=5)
    # plt.scatter(pltX1, pltY1, c='yellow', s=5)
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()
    #
    # ppx = []
    # sum_x = 0
    # sum_count = 0
    # for i in range(len(px)):
    #     j = i + 1
    #     if j >= len(px):
    #         j -= len(px)
    #     if abs(X[px[i]] - X[px[j]]) < 8 and abs(Y[px[i]] - Y[px[j]]) < 8:
    #         sum_x += px[i]
    #         sum_count += 1
    #     else:
    #         if sum_count == 0:
    #             ppx.append(px[i])
    #         else:
    #             sum_x += px[i]
    #             sum_count += 1
    #             ppx.append(round(sum_x / sum_count))
    #             sum_x = 0
    #             sum_y = 0
    #             sum_count = 0
    #
    # pltppx = []
    # pltppy = []
    # for i in range(len(ppx)):
    #     pltppx.append(X[ppx[i]])
    #     pltppy.append(Y[ppx[i]])
    #
    # plt.title("ppx")
    # plt.scatter(X, Y, c='blue', s=5)
    # plt.scatter(pltppx, pltppy, c='red', s=5)
    # plt.scatter(pltX1, pltY1, c='yellow', s=5)
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()
    #
    # plt.title("ppx_plot")
    # for i in range(len(X1)):
    #     ppx.append(X1[i])
    # print(ppx)
    # ppx.sort()
    # for i in range(len(ppx)):
    #     check_ppx = True
    #     j = i + 1
    #     if j >= len(ppx):
    #         j -= len(ppx)
    #     for ti in range(len(X1)):
    #         if X1[ti] == ppx[i] or X1[ti] == ppx[j]:
    #             check_ppx = False
    #             break
    #     if check_ppx:
    #         main_X.append([X[ppx[i]], X[ppx[j]]])
    #         main_Y.append([Y[ppx[i]], Y[ppx[j]]])
    #         plt.plot([X[ppx[i]], X[ppx[j]]], [Y[ppx[i]], Y[ppx[j]]], "blue")
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()
    #
    # machine = []
    # X = []
    # Y = []

    map_path = "./html/map.json"
    file_path = "./html/words.json"

    if os.path.isfile(map_path):
        with open(map_path, 'r') as f:
            data = json.load(f)
            main_X = data["Map_x"]
            main_Y = data["Map_y"]

    with open(file_path, 'r') as f:
        data = json.load(f)
        X = data["Lidar_x"]
        Y = data["Lidar_y"]
        machine = data["Location"]
        X[0] = X[2]
        X[1] = X[2]
        Y[0] = Y[2]
        Y[1] = Y[2]
        for i in range(len(X)):
            X[i] = round(X[i])
            Y[i] = round(Y[i])

    px = []

    for i in range(len(X)):
        gap = 15
        len1 = math.sqrt(math.pow(X[i], 2) + math.pow(Y[i], 2))
        gap = gap - round(len1 / 50)
        if gap <= 2:
            gap == 2
        bi = i - gap
        ni = i + gap
        if bi < 0:
            bi += len(X)
        if ni >= len(X):
            ni -= len(X)
        x1 = X[bi] - X[i]
        y1 = Y[bi] - Y[i]
        x2 = X[ni] - X[i]
        y2 = Y[ni] - Y[i]
        p21 = math.sqrt(math.pow(x1, 2) + math.pow(y1, 2))
        p23 = math.sqrt(math.pow(x2, 2) + math.pow(y2, 2))
        comb = round(abs((x1 * y2) - (y1 * x2)))
        div = round(abs(p21 * p23))
        if div == 0 or comb == 0 or div == comb:
            continue
        deg = math.degrees(math.asin(comb / div))
        if deg > 30:
            px.append(i)
    X1 = []
    for i in range(len(X) - 1):
        gap = 30
        len1 = math.sqrt(math.pow(X[i], 2) + math.pow(Y[i], 2))
        gap = gap - round(1500 / len1)
        if gap < 10:
            gap = 10
        if math.pow(X[i] - X[i + 1], 2) + math.pow(Y[i] - Y[i + 1], 2) > math.pow(gap, 2):
            X1.append(i)
            X1.append(i + 1)

    pltpx = []
    pltpy = []
    for i in range(len(px)):
        pltpx.append(X[px[i]])
        pltpy.append(Y[px[i]])
    pltX1 = []
    pltY1 = []
    for i in range(len(X1)):
        pltX1.append(X[X1[i]])
        pltY1.append(Y[X1[i]])

    # plt.title("px")
    # plt.scatter(X, Y, c='blue', s=5)
    # plt.scatter(pltpx, pltpy, c='red', s=5)
    # plt.scatter(pltX1, pltY1, c='yellow', s=5)
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()

    ppx = []
    sum_x = 0
    sum_count = 0
    for i in range(len(px)):
        j = i + 1
        if j >= len(px):
            j -= len(px)
        if abs(X[px[i]] - X[px[j]]) < 8 and abs(Y[px[i]] - Y[px[j]]) < 8:
            sum_x += px[i]
            sum_count += 1
        else:
            if sum_count == 0:
                ppx.append(px[i])
            else:
                sum_x += px[i]
                sum_count += 1
                ppx.append(round(sum_x / sum_count))
                sum_x = 0
                sum_count = 0

    pltppx = []
    pltppy = []
    for i in range(len(ppx)):
        pltppx.append(X[ppx[i]])
        pltppy.append(Y[ppx[i]])

    # plt.title("ppx")
    # plt.scatter(X, Y, c='blue', s=5)
    # plt.scatter(pltppx, pltppy, c='red', s=5)
    # plt.scatter(pltX1, pltY1, c='yellow', s=5)
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()
    #
    # plt.title("ppx_plot")
    for i in range(len(X1)):
        ppx.append(X1[i])
    #print(ppx)
    ppx.sort()
    # for i in range(len(main_X)):
    #     plt.plot(main_X[i], main_Y[i], "blue")
    check_X1 = False
    broken_point_x = []
    broken_point_y = []
    for i in range(len(ppx)):
        check_ppx = True
        j = i + 1
        if j >= len(ppx):
            j -= len(ppx)
        for ti in range(len(X1)):
            if abs(X1[ti] - ppx[i]) < 5 and abs(X1[ti] - ppx[j]) < 5:
                check_ppx = False
                if not check_X1:
                    broken_point_x.append(X[ppx[i]])
                    broken_point_y.append(Y[ppx[i]])
                break
            if check_X1:
                broken_point_x.append(X[ppx[j]])
                broken_point_y.append(Y[ppx[j]])
            check_X1 = False
        if check_ppx:
            # plt.plot([X[ppx[i]], X[ppx[j]]], [Y[ppx[i]], Y[ppx[j]]], "blue")
            main_X.append([X[ppx[i]], X[ppx[j]]])
            main_Y.append([Y[ppx[i]], Y[ppx[j]]])
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()

    for i in range(0, len(main_X) - 1):
        for j in range(i + 1, len(main_X)):
            if abs(main_X[i][0] - main_X[j][0]) < 10 and abs(main_Y[i][0] - main_Y[j][0]) < 10:
                dist_i = math.pow(main_X[i][0] - main_X[i][1], 2) + math.pow(main_Y[i][0] - main_Y[i][1], 2)
                dist_j = math.pow(main_X[j][0] - main_X[j][1], 2) + math.pow(main_Y[j][0] - main_Y[j][1], 2)
                if dist_i > dist_j:
                    main_X[j] = main_X[i]
                    main_Y[j] = main_Y[i]
                else:
                    main_X[i] = main_X[j]
                    main_Y[i] = main_Y[j]
            if abs(main_X[i][1] - main_X[j][1]) < 10 and abs(main_Y[i][1] - main_Y[j][1]) < 10:
                dist_i = math.pow(main_X[i][0] - main_X[i][1], 2) + math.pow(main_Y[i][0] - main_Y[i][1], 2)
                dist_j = math.pow(main_X[j][0] - main_X[j][1], 2) + math.pow(main_Y[j][0] - main_Y[j][1], 2)
                if dist_i > dist_j:
                    main_X[j] = main_X[i]
                    main_Y[j] = main_Y[i]
                else:
                    main_X[i] = main_X[j]
                    main_Y[i] = main_Y[j]
            if abs(main_X[i][0] - main_X[j][1]) < 10 and abs(main_Y[i][0] - main_Y[j][1]) < 10:
                main_X[i][0] = main_X[j][1]
                main_Y[i][0] = main_Y[j][1]

    # plt.title("main_plot")
    # for i in range(len(main_X)):
    #     plt.plot(main_X[i], main_Y[i], "blue")
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()

    tmp_X = []
    tmp_Y = []
    for value in main_X:
        if value not in tmp_X:
            tmp_X.append(value)

    for value in main_Y:
        if value not in tmp_Y:
            tmp_Y.append(value)

    main_X = tmp_X
    main_Y = tmp_Y

    for i in range(len(main_X)):
        each_dist = math.sqrt(math.pow(main_X[i][0] - main_X[i][1], 2) + math.pow(main_Y[i][0] - main_Y[i][1], 2))
        tlist = getEquidistantPoints((main_X[i][0], main_Y[i][0]), (main_X[i][1], main_Y[i][1]), round(each_dist))
        for j in range(len(tlist[0])):
            main_point_X.append(tlist[0][j])
            main_point_Y.append(tlist[1][j])
    # plt.title("main_point_plot")
    # plt.scatter(main_point_X, main_point_Y, c='blue', s=5)
    # plt.scatter(broken_point_x, broken_point_y, c='yellow', s=5)
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()

    file_data = OrderedDict()
    file_data["Map_x"] = main_X
    file_data["Map_y"] = main_Y

    # print(main_X)
    # print(main_Y)

    for i in range(len(main_point_X)):
        main_point_X[i] = round(main_point_X[i])
    for i in range(len(main_point_Y)):
        main_point_Y[i] = round(main_point_Y[i])

    tmp_X = []
    tmp_Y = []
    for value in broken_point_x:
        if value not in tmp_X:
            tmp_X.append(value)

    for value in broken_point_y:
        if value not in tmp_Y:
            tmp_Y.append(value)

    broken_point_x = tmp_X
    broken_point_y = tmp_Y

    st_x = []
    st_y = []
    for i in range(0, len(broken_point_x) - 1, 2):
        x1 = broken_point_x[i]
        y1 = broken_point_y[i]
        x2 = broken_point_x[i + 1]
        y2 = broken_point_y[i + 1]
        gap = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        rad = math.atan(25 / (gap / 2))
        ap_x = (x2 - x1) / 2 - (y2 - y1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + x1
        ap_y = (x2 - x1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + (y2 - y1) / 2 + y1

        st_x.append(round(ap_x))
        st_y.append(round(ap_y))

        # print("append ( x, y ) = ")
        # print(round(ap_x), round(ap_y))

    # plt.scatter(X1, Y1)
    # plt.scatter(machine[0], machine[1])
    # plt.scatter(broken_point[:, 0], broken_point[:, 1])
    # for i in range(len(st_x)):
    #    plt.scatter(st_x[i], st_y[i])
    # plt.show()

    for i in range(len(st_x)):
        j = 0
        while True:
            if j == len(X):
                break
            if abs(st_x[i] - X[j]) > 15:
                j += 1
                continue
            if abs(st_y[i] - Y[j]) > 15:
                j += 1
                continue
            if math.pow(st_x[i] - X[j], 2) + math.pow(st_y[i] - Y[j], 2) > math.pow(15, 2):
                j += 1
                continue
            # print("shorter than 15cm : i, j, ( x, y ) = ")
            # print(i, j, st_x[i], st_y[i])
            st_x[i] += round((machine[0] - st_x[i]) * 0.1)
            st_y[i] += round((machine[1] - st_y[i]) * 0.1)
            j = 0

    file_data["st_x"] = st_x
    file_data["st_y"] = st_y
    # plt.title("main_point_plot_round")
    # plt.scatter(main_point_X, main_point_Y, c='blue', s=5)
    # plt.scatter(st_x, st_y, c='yellow', s=5)
    # plt.scatter(machine[0], machine[1])
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    # plt.show()

    with open(map_path, 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    print("st_x : ")
    print(st_x)
    print("st_y : ")
    print(st_y)

my_algo()
# file_path = "./html/words.json"
#
# point = []
# th = []
# length = []
# X = []
# Y = []
# machine = []
# broken_points = []
# broken_xy = []
# main_point = []
# main_point_curve = []
# new_x_arr = []
# new_y_arr = []
# size = 10
# pause = False
#
# with open(file_path, 'r') as file:
#     data = json.load(file)
#     X = data["Lidar_x"]
#     Y = data["Lidar_y"]
#     machine = data["Location"]
#
# X[0] = X[2]
# X[1] = X[2]
# Y[0] = Y[2]
# Y[1] = Y[2]
#
# # remove_trash()
# # get_points()
# # get_onepoint()
# # main_point = main_point + broken_points
# # get_curve_point()
#
# st_x = []
# st_y = []
#
# #print("broken points [0] : ")
# #print(broken_xy[0][0], broken_xy[0][1])
#
# for i in range(0, len(broken_xy), 2):
#     x1 = broken_xy[i][0]
#     y1 = broken_xy[i][1]
#     x2 = broken_xy[i + 1][0]
#     y2 = broken_xy[i + 1][1]
#     gap = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
#     rad = math.atan(25 / (gap / 2))
#     ap_x = (x2 - x1) / 2 - (y2 - y1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + x1
#     ap_y = (x2 - x1) / 2 * (1 / math.cos(rad)) * math.sin(rad) + (y2 - y1) / 2 + y1
#
#     st_x.append(round(ap_x))
#     st_y.append(round(ap_y))
#
#     #print("append ( x, y ) = ")
#     #print(round(ap_x), round(ap_y))
#
# #plt.scatter(X1, Y1)
# #plt.scatter(machine[0], machine[1])
# #plt.scatter(broken_point[:, 0], broken_point[:, 1])
# #for i in range(len(st_x)):
# #    plt.scatter(st_x[i], st_y[i])
# #plt.show()
#
# for i in range(len(st_x)):
#     j = 0
#     while True:
#         if j == len(X):
#             break
#         if abs(st_x[i] - X[j]) > 15:
#             j += 1
#             continue
#         if abs(st_y[i] - Y[j]) > 15:
#             j += 1
#             continue
#         if math.pow(st_x[i] - X[j], 2) + math.pow(st_y[i] - Y[j], 2) > math.pow(15, 2):
#             j += 1
#             continue
#         #print("shorter than 15cm : i, j, ( x, y ) = ")
#         #print(i, j, st_x[i], st_y[i])
#         st_x[i] += round((machine[0] - st_x[i]) * 0.1)
#         st_y[i] += round((machine[1] - st_y[i]) * 0.1)
#         j = 0
#
# #plt.scatter(X, Y, c='blue', s=5)
# #plt.scatter(machine[0], machine[1], c='yellow', s=20)
# #plt.scatter([i[0] for i in broken_xy], [i[1] for i in broken_xy], c='red', s=20)
# #for i in range(len(st_x)):
# #    plt.scatter(st_x[i], st_y[i], c='orange', s=20)
# #plt.show()
#
# file_data = OrderedDict()
#
# if len(st_x) == 0 or len(st_y) == 0:
#     st_x.append(-1)
#     st_y.append(-1)
# file_data["st_x"] = st_x[0]
# file_data["st_y"] = st_y[0]
#
# #file_data["st_x"] = st_x
# #file_data["st_y"] = st_y
#
# with open(file_path, 'w', encoding="utf-8") as make_file:
#     json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
#
# print("st_x, st_y : ", st_x[0], st_y[0])
#
# #for i in range(len(st_x)):
# #    print("st = ( " + st_x[i] + ", " + st_y[i] + " )")
