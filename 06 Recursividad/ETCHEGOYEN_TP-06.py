# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

#%%
def factorial(n):
    if n == 1:
        return n
    else: 
        return n * factorial(n-1)

numero = int(input('Ingresar un número para obtener su factorial'))
for i in range(1, numero + 1):
    print(f'{i}! = {factorial(i)}')
#%%

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

#%%
def fibonacci_recursivo(n):
    if n == 0:
        return n
    if n == 1:
        return n
    else: 
        return fibonacci_recursivo(n-2) + fibonacci_recursivo(n-1)

numero = int(input('Indique una posición de fibonacci'))
for n in range(numero+1):
    print(f'Fibonacci, posición {n}: {fibonacci_recursivo(n)}')
#%%

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula n^m = n*n^(m-1)
# Prueba esta función en un algoritmo general.

#%%
def calcula_potencia(n,m):
    if m == 0:
        return 1
    else: 
        return n * calcula_potencia(n,m-1)
numero = int(input('Ingrese un numero para calcular la potencia'))
potencia = int(input('Ingrese el numero de potencia'))
calcula_potencia(numero,potencia)

#%%

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

#%%
def calcula_binario(n):
    if n == 1:
        return 1
    else:
        return f'{calcula_binario(n // 2)}{n % 2}'

numero = int(input('Ingresar numero para convertir a binario'))
calcula_binario(numero)
#%%
# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

#%%
def es_palindromo(palabra):
    if len(palabra) == 1:
        return True
    if len(palabra) == 2:
        return palabra[0] == palabra[1]
    else:
        if palabra[0] == palabra[len(palabra) - 1]:
            return es_palindromo(palabra[1:len(palabra) - 1])
        else:
            return False

entrada = input('Ingresar palabra para saber si es palindromo')
es_palindromo(entrada)
#%%

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

#%%
def suma_digitos(n):
    if n < 10: 
        return n
    else: 
        return (n % 10) + suma_digitos(n // 10)

numero = int(input('Ingresar numero'))
suma_digitos(numero)

#%%

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

#%%
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
numero = int(input('Ingresar numero de bloques en el nivel mas bajo'))
print(f'Bloques necesarios: {contar_bloques(numero)}')
#%%

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0 

#%%
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
numero = int(input('Ingresar numero'))
digito = int(input('Ingresar digito a contar'))
print(f'El digito {digito} aparece {contar_digito(numero, digito)} veces en el numero {numero}')
#%%