i = 0

while True:
    i = int(input())
    if i < 10:
        continue
    if 10 <= i <= 100:
        print(i)
    elif i > 100:
        break
