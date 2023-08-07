import random

# Ejercicio 1
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print("Nombre:", nombre)
print("Edad:", edad)

# Ejercicio 2
def calcular_area_circulo(radio):
    return 3.14159 * radio ** 2

# Ejercicio 3
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print("Números aleatorios:", numeros_aleatorios)

# Ejercicio 4
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejercicio 5
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ejercicio 6
def suma_lista(lista):
    return sum(lista)

# Ejercicio 7
def encontrar_extremos(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

# Ejercicio 8
def invertir_lista(lista):
    return lista[::-1]

# Ejercicio 9
filas = 3
columnas = 4
matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
for fila in matriz:
    print(fila)

# Ejercicio 10
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Ejercicio 11
numeros_pares = [i for i in range(2, 101, 2)]
print("Números pares:", numeros_pares)

# Ejercicio 12
for i in range(1, 11):
    print(i)

# Ejercicio 13
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Ejercicio 14
def media_aritmetica(lista):
    return sum(lista) / len(lista)

# Ejercicio 15
cadena = input("Ingrese una cadena de texto: ")
if cadena == cadena[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
