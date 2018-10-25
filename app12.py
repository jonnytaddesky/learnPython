x = str(input())

y = x[:3]

a = int(y[0])
b = int(y[1])
c = int(y[2])

z = x[3:]

d = int(z[0])
e = int(z[1])
f = int(z[2])

if a + b + c == e + d + f:
    print('Счастливый')
else:
    print('Обычный')
