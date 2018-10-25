import math
pi = 3.14
s = str(input())

if s == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif s == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif s == 'круг':
    r = int(input())
    print(pi * math.pow(r, 2))
