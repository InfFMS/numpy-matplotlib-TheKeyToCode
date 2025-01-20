# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.

import matplotlib.pyplot as plt
import numpy as np


# plt.title("Простой график")
# plt.xlabel("Ось X")
# plt.ylabel("Ось Y")
t_min = -20
t_max = 30
t_border = 0
import random
def random_weather():
    return random.randint(t_min,t_max)
l = []
t_r = []
for i in range(t_max-t_min+1):
    t_r.append(0)
negative_t_delta = 0
negative_t_max = 0
rw=0
for i in range(365):
    rw = random_weather()
    l.append(rw)
    t_r[rw-t_min]+=1
    if l[i] < 0:
        negative_t_delta+=1
    elif negative_t_delta>negative_t_max:
        negative_t_max = negative_t_delta
categories = []
for i in range(t_max-t_min+1):
    categories.append(i)

days = []
for i in range(365):
    days.append(i+1)
# Создание подграфиков
fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # 1 ряд, 2 столбца

# График 1
axs[0].plot(days, l, color="blue")
axs[0].set_title("Температура")
axs[0].set_xlabel("Дни")
axs[0].set_ylabel("Градусы")

# График 2

plt.bar(categories, t_r, color='purple')
plt.title("Температура")

plt.tight_layout()
plt.show()
