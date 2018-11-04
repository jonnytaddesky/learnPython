b = int(input())
a = int(input())
c = int(input())
d = 0

d = b ** b + 4 * a * c

if d > 0:
    print('roots 2')
elif d == 0:
    print('roots 1')
else:
    print('no roots')
