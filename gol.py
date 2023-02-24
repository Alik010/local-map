import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

file = open("examp7.txt").read().split("\n")
data = []
for line in file:
    data.append(line.split(";"))

pos_robot = []  # позиции робота
lidar = []  # данные по лидару
for i, inf in enumerate(data):
    if i == len(data) - 1:
        continue
    result = [float(item) for item in inf[0].split(", ")]
    pos_robot.append(result)

    value_lidar = inf[1]
    value_lidar = value_lidar[1:]
    res = [float(item) for item in value_lidar.split(", ")]
    lidar.append(res)

vision_zone_lidar = 240  # градусы

step = vision_zone_lidar / len(lidar[0])  # шаг испускания сигнала
print(step)
x_obs = []
y_obs = []

s = []
angle = -120

for i in range(len(lidar[0])):
    s.append(angle + step * i)

for i in range(len(lidar)):
    x = [(r + 0.3) * math.cos(-s[j] * math.pi/180 + pos_robot[i][2]) for j, r in enumerate(lidar[i]) if r < 5.6 and r > 0.5]
    y = [(r + 0.3) * math.sin(-s[j] * math.pi/180 + pos_robot[i][2]) for j, r in enumerate(lidar[i]) if r < 5.6 and r > 0.5]

    x_obs.append(x)
    y_obs.append(y)

result_x = []
result_y = []

for i in range(len(x_obs)):
    for j in range(len(x_obs[i])):
        x_obs[i][j] = x_obs[i][j] + pos_robot[i][0]
        y_obs[i][j] = y_obs[i][j] + pos_robot[i][1]

    plt.scatter(x_obs[i], y_obs[i], s = 1)
    plt.scatter(pos_robot[i][0], pos_robot[i][1], marker="*")
    plt.xlim((-3, 12))
    plt.ylim((-10, 5))
    plt.pause(0.1)

plt.axis("off")
plt.savefig("fig.png")


