# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt
size_rec = 1
colors = [ "white", "black"]
def createRec(i,j):
    rect = plt.Rectangle((size_rec * i, size_rec * j), size_rec , size_rec, color=colors[(i+j)%2], label = "")
    ax.add_patch(rect)
def createFig(i,j):
    rect = plt.Rectangle((size_rec * (i + 0.4), size_rec * (j+0.1)), 0.2 * size_rec,0.5 * size_rec , color=colors[(i+j+1)%2], label = "")
    ax.add_patch(rect)
    rect = plt.Rectangle((size_rec * (i + 0.2), size_rec * (j+0.1)), 0.6 * size_rec, 0.1 * size_rec , color=colors[(i+j+1)%2], label = "")
    ax.add_patch(rect)
    circle = plt.Circle((size_rec * (i+0.5), size_rec * (j+0.6)), 0.2, color=colors[(i+j+1)%2], label="Окружность")
    ax.add_patch(circle)
def createCircle(i,j):
    circle = plt.Circle((size_rec * (i+0.5), size_rec * (j+0.5)), 0.3, color="purple", alpha = 0.8, label="Окружность")
    ax.add_patch(circle)

f = input("Введите фигуру: (Ка - кароль, Ко - конь, Ф - Ферзь, П - Пешка, С - слон, Л - ладья): ")
x,y=map(int,input("Введите расположение фигуры: ").split())
fig, ax = plt.subplots()

x+=1
y+=1
field = []
for i in range(12):
    field.append([0,0,0,0,0,0,0,0,0,0,0,0])
print(field)
if f == "Ка":
    for i in range(x-1,x+2):
        for j in range(y - 1, y + 2):
            field[i][j]=1
            if i==x and j!=y:
                field[i][j] = 2
elif f == "Ко":
    field[x][y] = 2
    field[x-2][y-1] = 1
    field[x-2][y+1] = 1
    field[x+2][y+1] = 1
    field[x+2][y-1] = 1
    field[x-1][y-2] = 1
    field[x-1][y+2] = 1
    field[x+1][y+2] = 1
    field[x+1][y-2] = 1
elif f == "Л":
    for i in range (12):
        field[x][i] = 1
        field[i][y] = 1
    field[x][y] = 2
elif f == "С":
    for i in range(12):
        for j in range(12):
            if x-y == i-j :
                field[i][j]=1
            if x+y == i+j:
                field[i][j]=1

    field[x][y] = 2
elif f == "Ф":
    for i in range(12):
        for j in range(12):
            if x-y == i-j :
                field[i][j]=1
            if x+y == i+j:
                field[i][j]=1
    for i in range(12):
        field[x][i] = 1
        field[i][y] = 1
    field[x][y] = 2

print(field)
for i in range(8):
    for j in range(8):
        createRec(i, j)
        if(field[i+2][j+2] == 1):
            createCircle(i,j)
        elif(field[i+2][j+2] == 2):
            createFig(i,j)
# createFig(5,6)
# createCircle(1,2)
# Настройка
ax.set_xlim(0, size_rec*8)
ax.set_ylim(0, size_rec*8)
# plt.legend()
plt.title("Доска")
plt.show()
