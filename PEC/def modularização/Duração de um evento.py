segundos= int(input())

x= segundos %60 #segundos extras
y= segundos //60 #minutos
z= y //60
a= y%60

print(f'{z}:{a}:{x}')
