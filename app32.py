rows, column, mines = (int(i) for i in input().split())

arrayList = [[0 for i in range(column)] for i in range(rows)]

for i in range(mines):
    rowsMines, columnMines = (int(i) - 1 for i in input().split())
    arrayList[rowsMines][columnMines] = -1

print(arrayList)

for i in range(rows):
    for j in range(column):
        if arrayList[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < rows and 0 <= aj < column and arrayList[ai][aj] == -1:
                        arrayList[i][j] += 1
for i in range(rows):
    for j in range(column):
        if arrayList[i][j] == -1:
            print('*', end='')
        elif arrayList[i][j] == 0:
            print('.' , end='')
        else :
            print(arrayList[i][j], end='')
    print()
