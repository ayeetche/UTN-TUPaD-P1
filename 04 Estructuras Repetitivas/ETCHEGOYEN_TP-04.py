# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#%%
for x in range(101):
    print(x)
#%%


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

#%%
numero = input('Ingresar numero entero: ')
contador = 0

for x in range(len(numero)): 
    contador += 1

print(contador)
#%%

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

#%%
numero_1 = int(input('Ingresar numero entero: '))
numero_2 = int(input('Ingresar otro numero entero: '))
suma = 0

while numero_1 != numero_2:
    if(numero_1 < numero_2): 
        numero_2 -= 1
        if(numero_1 == numero_2):
            break
        suma += numero_2
    else:
        numero_1 -=1
        if(numero_1 == numero_2):
            break
        suma += numero_1

print(suma)
#%%


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

#%%
numero = int(input('Ingresar numero entero'))
suma = 0
while numero != 0:
    suma += numero
    print(f'Suma: {suma}')
    numero = int(input('Ingresar numero entero'))

print(f'Total: {suma}')
#%%

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#%%

import random
numero_aleatorio = random.randint(0, 9)
numero = int(input('Adivina el número aleatorio entre 0 y 9'))
intentos = 1

while numero != numero_aleatorio:
    numero = int(input('Adivina el número aleatorio entre 0 y 9'))
    intentos += 1
    
print(f'Intentos: {intentos}')

#%%

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# %%
for x in range(100,-1, -1):
    print(x)

# %%


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


#%%
numero = int(input('Suma numeros comprendidos entre 0 y un número deseado. Ingrese numero entero'))
suma = 0
while numero > 0:
    suma += numero
    numero -= 1
print(f'La suma es {suma}')
#%%

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#%%
positivos = 0
negativos = 0
pares = 0
impares = 0

for x in range(100):
    numero = int(input('Ingresar número entero'))
    if(numero > 0):
        positivos += 1
    elif(numero < 0): 
        negativos += 1

    if(numero % 2 == 0):
        pares += 1
    else:
        impares += 1
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')
print(f'Números positivos: {positivos}')
print(f'Números negativos: {negativos}')
#%%

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

#%%
from statistics import mean
numeros = []
for x in range(100):
    numero = int(input('Ingresar número entero'))
    numeros.append(numero)
    
print(mean(numeros))

#%%

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# %%
numero = input('Ingrese número: ')
numero_invertido = ''

for x in range(len(numero)):
    numero_invertido = numero[x] + numero_invertido
print(f'El número invertido es: {numero_invertido}')
# %%

