# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).

import math
import random
from itertools import count
from operator import countOf
import matplotlib.pyplot as plt

############  !Create field!  ############

field = []
def show_field():
    for i in range(len(field)-2,0,-1):
        print(field[i][1:-1])

def bomb_placement(bomb_count,a,b):
    while bomb_count!=0:
        i = random.randint(1,a)
        j = random.randint(1,b)
        if field[i][j] != -1:
            field[i][j] = -1
            bomb_count-=1
    print("The bombs are successfully loaded")

def cell_numbers(a,b):
    for i in range(1,a+1):
        for j in range(1, b + 1):
            if(field[i][j]!=-1):
                c = 0
                c = countOf([field[i-1][j-1], field[i-1][j],field[i-1][j+1],field[i][j-1],
                            field[i][j+1],field[i+1][j-1],field[i+1][j],field[i+1][j+1]], -1)
                field[i][j] = c
    print("The numbers are successfully loaded")

def create_field(a,b):
    bomb_count = random.randint(int(math.sqrt(a*b) // 2), int(math.sqrt(a*b)*1.5))
    for i in range (a+2):
        field.append([0]*(b+2))
    bomb_placement(bomb_count,a,b)
    cell_numbers(a,b)
a,b = map(int, input("Введите границы полля:").split())
create_field(a,b)
show_field()


############  !Show field!  ############

fig, m_field = plt.subplots()
size_rec = 1
colors = [ "white", "grey"]
m_field.set_xlim(0, size_rec*b)
m_field.set_ylim(0, size_rec*a)
colors_t = ["white","green", "yellow", "red", "burgundy","burgundy","burgundy","burgundy","burgundy"]
def createRec(i,j):
    rect = plt.Rectangle((size_rec * j, size_rec * i), size_rec , size_rec, color=colors[(i+j)%2], label = "")
    m_field.add_patch(rect)
    # print("REC CREATED")
def createBomb(i,j):
    circle = plt.Circle((size_rec * (j+0.5), size_rec * (i+0.5)), 0.3, color="black", alpha = 0.8, label="bomb")
    m_field.add_patch(circle)
def createNumber(i,j):
    # n = plt.get_fignums()
    n = plt.text(size_rec * (j+0.4), size_rec * (i+0.4), str(field[i+1][j+1]), fontdict={"size": 20, "color": colors_t[field[i+1][j+1]]})
    # m_field.add_patch(n)

def show_just_cells():
    for i in range(a):
        for j in range(b):
            createRec(i, j)
def show_another_things():
    for i in range(1,a+1):
        for j in range(1, b + 1):
            print(i,j,field[i][j])
            if field[i][j] == -1:
                print("YEY")
                createBomb(i-1,j-1)
            elif field[i][j] != 0:
                createNumber(i-1,j-1)
def show_field_matplotlib():
    show_just_cells()
    show_another_things()
show_field_matplotlib()
show_field()
plt.show()
