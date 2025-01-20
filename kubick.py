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
for i in range(1000):
    l[throw()-1]+=1

categories = [1,2,3,4,5,6]

plt.bar(categories, l, color='purple')
plt.title("Выпадение кубиков")
plt.show()
