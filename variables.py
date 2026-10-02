print("=" * 30)
print("Ejercicio 1")

#definir las variables
ancho = float(input("Ingrese el ancho del terreno:"))
largo = float(input("Ingrese el largo del terreno:"))

#Realizar el calculo
perimetro = ancho*largo
print(f"El perimetro del terreno es: {perimetro}")

print("=" * 30)
print("Ejercicio 2")
#pedir los numeros al usuario

numero1 = float(input("Ingrese el numero:"))
print(f"el numero 1 que ingresaste es: {numero1}")
numero2 = float(input("Ingrese el numero:"))
print(f"el numero 1 que ingresaste es: {numero2}")
numero3 = float(input("Ingrese el numero:"))
print(f"el numero 1 que ingresaste es: {numero3}")

#calcular su promedio
promedio =float(numero1+numero2+numero3)/3
print(f"El promedio es: {promedio}")

print("=" * 30)
print("Ejercicio 3")
#solicitar datos
nombre = input("Ingrese su nombre ")
edad = input("Ingrese su edad ")
print(f'"Hola,mi nombre es {nombre} y tengo {edad}"')

print("=" * 30)
print("Ejercicio 4")

#solicitar valor en  cop
valor = float(input("Ingrese el valor en COP:"))
# Convertir a dolares
usd = 400
convercion = valor * usd
print(f"El valor en dolares de {valor} es: {convercion}")

print("=" * 30)
print("Ejercicio 5")
segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_restantes)