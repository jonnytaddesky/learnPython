arrayList = [int(i) for i in input().split()]

currentValue = arrayList[0]

for value in arrayList:
    if currentValue > value:
        currentValue = value
print(currentValue)