a= float(input())
b= float(input())

def coisa(x, y):
    algo= x/(y**2)

    if algo< 18.5:
        print('%d'%algo)
        return 'Abaixo do peso'
            
    elif algo< 25:
        print('%d'%algo)
        return 'Peso normal'
        
    elif algo< 30:
        print('%d'%algo)
        return 'Sobrepeso'
        
    elif algo< 35:
        print('%d'%algo)
        return 'Obeso leve'
        
    elif algo< 40:
        print('%d'%algo)
        return 'Obeso moderado'
        
    else:
        print('%d'%algo)
        return 'Obeso mórbido'


print(f'{coisa(a, b)}')
