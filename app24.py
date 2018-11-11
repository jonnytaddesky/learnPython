a = -5
b = 12

s = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        count += 1
s = s / count
print(s)
