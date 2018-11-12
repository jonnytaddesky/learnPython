s = 'ttatAATAataccGGgCGata'

c = s.upper().count('c'.upper())
g = s.upper().count('g'.upper())

sum = ((s.upper().count('c'.upper()) + s.upper().count('g'.upper())) / len(s)) * 100  

print(len(s))
print(str(sum) + '%')

