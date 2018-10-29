summa = 0
current = 0
contin = True

while contin:        
    current = int(input())
    if (summa - current == summa):
        contin = False
    summa += current
print(summa)
