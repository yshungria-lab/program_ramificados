print("-----Bienvenido al programa de compración de edades-----")
usuario1 = input('Cómo se llama el usuario 1?')
edad_usuario1 = int(input(f'Que edad tiene {usuario1}?: '))
usuario2 = input('Cómo se llama el usuario 2?')
edad_usuario2 = int(input(f'Que edad tiene {usuario2}?: '))

print('-----------Resultado------------')

if edad_usuario1 < edad_usuario2:
    print(f'{usuario1} tiene {edad_usuario1} años y es menor que {usuario2} que tiene {edad_usuario2} años')
elif edad_usuario1 > edad_usuario2:
    print(f'{usuario1} tiene {edad_usuario1} años y es mayor que {usuario2} que tiene {edad_usuario2} años')
else :
    print(f'{usuario1} y {usuario2} tienen la misma edad {edad_usuario1} años')```
