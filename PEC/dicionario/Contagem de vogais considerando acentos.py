x= input().strip().lower()
a= 0
e= 0
i= 0
o= 0
u= 0

for j in range(len(x)):
    if x[j] in "aáàâã":
        a+= 1
    elif x[j] in "eéèê":
        e+= 1
    elif x[j] in "iíìî":
        i+= 1
    elif x[j] in "oóòôõ":
        o+= 1
    elif x[j] in "uúùû":
        u+= 1

print(f'A: {a}')
print(f'E: {e}')
print(f'I: {i}')
print(f'O: {o}')
print(f'U: {u}')
