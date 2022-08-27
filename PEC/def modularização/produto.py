def algo(a, b):
    return a+(a*(b/100))
def outro(c, b):
    return c-(c*(b/100))

x= float(input())
z= x
y= float(input())
x= algo(x,y)
z= outro(z, y)
x= round(x, 2)
z= round(z, 2)

print('%.2f'% x)
print('%.2f'% z)
