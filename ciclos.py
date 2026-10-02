print("=" * 30)
print("Ejercicio 1")
import random

secreto = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número entre 1 y 10: "))
    if intento == secreto:
        print("¡Acertaste! El número era", secreto)
        break
    print("Incorrecto, intenta de nuevo.")


print("=" * 30)
print("Ejercicio 2")
n = int(input("Ingrese un número entero mayor que 0: "))

if n <= 0:
    print("Error: el número debe ser mayor que 0.")
else:
    while n >= 0:
        print(n)
        n = n - 1
    print("¡La cuenta regresiva ha terminado!")


print("=" * 30)
print("Ejercicio 3")
for i in range(1, 101):
    if i % 2 != 0:
        print(i)



print("=" * 30)
print("Ejercicio 4")
from datetime import datetime
opcion = 0
while opcion != 3:
    print("\n--- MENÚ ---")
    print("1) Mensaje de bienvenida")
    print("2) Fecha y hora actual")
    print("3) Salir")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        print("¡Bienvenido al programa!")
    elif opcion == 2:
        ahora = datetime.now()
        print("Fecha y hora actual:", ahora.strftime("%d/%m/%Y %H:%M:%S"))
    elif opcion == 3:
        print("Saliendo del programa. ¡Hasta pronto!")
    else:
        print("Opción no válida, intente de nuevo.")


print("=" * 30)
print("Ejercicio 5")
cantidad = int(input("¿Cuántas notas desea registrar? "))

if cantidad <= 0:
    print("Error: la cantidad debe ser mayor que 0.")
else:
    suma = 0

    for i in range(1, cantidad + 1):
        nota = float(input(f"Ingrese la nota {i}: "))
        suma = suma + nota

    promedio = suma / cantidad
    print(f"\nPromedio: {promedio:.2f}")

    if promedio >= 3.0:
        print("El estudiante aprobó.")
    else:
        print("El estudiante no aprobó.")