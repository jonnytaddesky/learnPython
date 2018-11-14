s = input()

cnt = 1

for i in range(len(s)):
    if i == len(s) - 1:
        print(s[i] + str(cnt), end='')
        break
    elif s[i] == s[i + 1]:
        cnt += 1
    else:
        print(s[i] + str(cnt), end='')
        cnt = 1
print()    
