s = [int(i) for i in input().split()]

summ = 0

for i in range(0, (len(s) - 1) + 1):
    summ += s[i]
print(summ)
