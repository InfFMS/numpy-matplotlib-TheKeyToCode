# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений,
# где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
import math
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def get_dir():
    return random.randint(1,4)
x = [0]
y = [0]
l = []
for i in range(100):
    l.append(get_dir())
for i in l:
    if i == 1:
        y.append(y[-1]+1)
        x.append(x[-1])
    if i == 2:
        y.append(y[-1]-1)
        x.append(x[-1])
    if i == 3:
        y.append(y[-1])
        x.append(x[-1]+1)
    if i == 4:
        y.append(y[-1])
        x.append(x[-1]-1)
fig, axs = plt.subplots(left=0.1, bottom=0.35, )  # 1 ряд, 2 столбца

axs.plot(x, y, color="blue")
axs.set_title("Движение")
axs.set_xlabel("X")
axs.set_ylabel("Y")
plt.title("Движение")
plt.button = Button(axs, 'next move')
plt.show()
