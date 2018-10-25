a = float(input())
b = float(input())
c = str(input())

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if b == 0.0:
        print('Деление на 0!')
    else:
        print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod':
    if b == 0.0:
        print('Деление на 0!')
    else:
        print(a % b)
elif c == 'pow':
        print(pow(a, b))
elif c == 'div':
    if b == 0.0:
        print('Деление на 0!')
    else:
        print(a // b)