X = int(input())
H = int(input())
M = int(input())

m = H * 60 + M

res = X + m

aHour = res // 60
aMin = res % 60

print(aHour)
print(aMin)
