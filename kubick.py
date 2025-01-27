# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import matplotlib.pyplot as plt


# plt.title("Простой график")
# plt.xlabel("Ось X")
# plt.ylabel("Ось Y")

import random
def throw():
    return random.randint(1,6)
l = [0,0,0,0,0,0]
count_max_delta = 0
count_max = 0
max_num = 1
for i in range(1000):
    num = throw()
    l[num-1]+=1
    if num==max_num:
        count_max_delta+=1
    else:
        if count_max<count_max_delta:
            max_num=num
            count_max=count_max_delta
        count_max_delta=0
fig, ax = plt.subplots()
categories = [1,2,3,4,5,6]
plt.bar(categories, l, color='purple')
plt.title("Выпадение кубиков")

plt.subplots_adjust(left=0.1, bottom=0.35)

text_stats = (
        f"номер| выпало всего| шанс\n"
    f"1:       |  {l[0]}               |  {l[0] / 1000} \n"
    f"2:       |  {l[1]}               |  {l[1] / 1000} \n"
    f"3:       |  {l[2]}               |  {l[2] / 1000} \n"
    f"4:       |  {l[3]}               |  {l[3] / 1000} \n"
    f"5:       |  {l[4]}               |  {l[4] / 1000} \n"
    f"6:       |  {l[5]}               |  {l[5] / 1000} \n"
    f"Максимальное количество одинаковых кубиков, выпавших подряд: {count_max}, и их значение было равно: {max_num}"
)
stats_ax = fig.add_axes([0.1, 0.1, 1., 0.2])  # Позиция для статистики [x, y, width, height]
stats_ax.axis('off')  # Скрываем оси
stats_box = stats_ax.text(0, 1, text_stats,
                fontsize=10, verticalalignment='top')
plt.show()
