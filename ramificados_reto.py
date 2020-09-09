<
print('Este Programa compara la edad de dos personas')
nombre_1 = input('Hola, cual es tu nombre? : ')
edad_1 = int(input(f'{nombre_1} cual es tu edad? :'))
print(f'Gracias {nombre_1}, el siguiente por favor')
nombre_2 = input('Hola, cuales tu nombre? : ')
edad_2 = int(input(f'{nombre_2} cual es tu edad? :'))
comp_edades = abs(edad_1 - edad_2)
print(f'Gracias {nombre_2}')
print('Ahora les dire los resultados')

if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}')
    print(f'Tiene actualmente {edad_1} años y es mayor por {comp_edades} años')
elif edad_1 < edad_2:
    print(f'{nombre_2} es mayor que {nombre_1}')
    print(f'Tiene actualmente {edad_2} años y es mayor por {comp_edades} años')
else:
    print(f'{nombre_1} y {nombre_2} tienen la misma edad')
    print(f'Ambos tienen {edad_1} años')

print(f'Gracias {nombre_1} y {nombre_2} nos vemos')
>
