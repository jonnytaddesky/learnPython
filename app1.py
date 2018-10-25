a = int(input())
b = int(input())
c = int(input())

if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= c >= b:
    print(c)

if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
elif a >= c <= b:
    print(c)

if b <= a <= c or c <= a <= b:
    print(a)
elif a <= b <= c or c <= b <= a:
    print(b)
elif a <= c <= b or b <= c <= a:
    print(c)
