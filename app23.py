rowInputFirst = int(input())
rowInputEnd = int(input())
columnInputFirst = int(input())
columnInputEnd = int(input())

print(end='\t')
for x in range(columnInputFirst, columnInputEnd + 1):
    print(x, end='\t')
print()
for i in range(rowInputFirst, rowInputEnd + 1):
    print(i, end='\t')
    for j in range(columnInputFirst, columnInputEnd + 1):
        print(i * j, end='\t')
    print()
print()
