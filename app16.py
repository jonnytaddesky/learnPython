a = int(input())
b = int(input())

m = a * b
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(m // (a + b))

# 17 20 
# else = 17 

# print(17 * 20 // 17 * 17) 
