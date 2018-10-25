a = int(input())

if a == 0:
    print(str(a) + ' программистов')
elif a == 1 :
    print(str(a) + ' программист')
elif (a % 2 == 0 and a % 4 == 0) or a % 3 == 0 or a == 2 or a == 3 or a == 4:
    print(str(a) + ' программиста')
elif a % 5 == 0 or a == 0:
    print(str(a) + ' программистов')
    