print("=" * 30)
print("Ejercicio 1")
# Solicitar datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
# Validar que la edad no sea negativa
if edad < 0:
    print("Error: la edad no puede ser un valor negativo.")
else:
    # Determinar si es mayor o menor de edad
    if edad >= 18:
        resultado = "Mayor de edad"
        print(f"\nNombre: {nombre}")
        print(f"Edad: {edad} años")
        print(f"Resultado: {resultado}")
    else:
        faltan = 18 - edad
        resultado = "Menor de edad"
        print(f"\nNombre: {nombre}")
        print(f"Edad: {edad} años")
        print(f"Resultado: {resultado}")
        print(f"Le faltan {faltan} años para cumplir la mayoría de edad.")


print("=" * 30)
print("Ejercicio 2")
# Solicitar datos
nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la calificación final (0.0 a 5.0): "))

# Validar el rango permitido
if nota < 0.0 or nota > 5.0:
    print("Error: la calificación debe estar entre 0.0 y 5.0.")
else:
    # Determinar si aprueba o reprueba
    if nota >= 3.0:
        resultado = "Aprueba"
    else:
        resultado = "Reprueba"

    # Clasificar el desempeño
    if nota >= 4.5:
        desempeno = "Excelente"
    elif nota >= 3.5:
        desempeno = "Bueno"
    elif nota >= 3.0:
        desempeno = "Aceptable"
    else:
        desempeno = "Insuficiente"

    # Mostrar resultados
    print(f"\nEstudiante: {nombre}")
    print(f"Calificación: {nota}")
    print(f"Resultado: {resultado}")
    print(f"Desempeño: {desempeno}")


print("=" * 30)
print("Ejercicio 3")
# Solicitar datos
nombre = input("Ingrese el nombre del cliente: ")
valor = float(input("Ingrese el valor total de la compra: "))

# Validar que el valor sea mayor a cero
if valor <= 0:
    print("Error: el valor de la compra debe ser mayor a cero.")
else:
    # Determinar el porcentaje de descuento
    if valor >= 500000:
        porcentaje = 20
    elif valor >= 300000:
        porcentaje = 15
    elif valor >= 100000:
        porcentaje = 10
    else:
        porcentaje = 0

    # Calcular el descuento y el total a pagar
    descuento = valor * porcentaje / 100
    total = valor - descuento

    # Mostrar resultados
    print(f"\nCliente: {nombre}")
    print(f"Valor de la compra: ${valor:,.0f}")
    print(f"Descuento aplicado: {porcentaje}%")
    print(f"Valor descontado: ${descuento:,.0f}")
    print(f"Total a pagar: ${total:,.0f}")


print("=" * 30)
print("Ejercicio 4")
# Solicitar datos
ciudad = input("Ingrese el nombre de la ciudad: ")
temperatura = float(input("Ingrese la temperatura actual en °C: "))

# Clasificar la temperatura
if temperatura < 10:
    clasificacion = "Muy fría"
elif temperatura < 18:
    clasificacion = "Fría"
elif temperatura < 26:
    clasificacion = "Templada"
elif temperatura <= 32:
    clasificacion = "Caliente"
else:
    clasificacion = "Muy caliente"

# Recomendación de abrigo
if temperatura < 18:
    recomendacion = "Se recomienda llevar abrigo."
else:
    recomendacion = "No es necesario llevar abrigo."
# Mostrar resultados
print(f"\nCiudad: {ciudad}")
print(f"Temperatura: {temperatura} °C")
print(f"Clasificación: {clasificacion}")
print(f"Recomendación: {recomendacion}")


print("=" * 30)
print("Ejercicio 5")
# Solicitar datos
nombre = input("Ingrese el nombre del empleado: ")
horas = float(input("Ingrese las horas trabajadas en el mes: "))
valor_hora = float(input("Ingrese el valor de cada hora: "))

# Validar que los valores sean positivos
if horas <= 0 or valor_hora <= 0:
    print("Error: las horas trabajadas y el valor de la hora deben ser positivos.")
else:
    # Separar horas normales y horas extra
    if horas > 160:
        horas_normales = 160
        horas_extra = horas - 160
    else:
        horas_normales = horas
        horas_extra = 0

    # Calcular pagos
    pago_normal = horas_normales * valor_hora
    pago_extra = horas_extra * valor_hora * 1.25

    # Salario bruto, descuento y salario neto
    salario_bruto = pago_normal + pago_extra
    descuento = salario_bruto * 0.08
    salario_neto = salario_bruto - descuento

    # Mostrar resultados
    print(f"\nEmpleado: {nombre}")
    print(f"Horas normales: {horas_normales}")
    print(f"Horas extra: {horas_extra}")
    print(f"Pago horas normales: ${pago_normal:,.0f}")
    print(f"Pago horas extra: ${pago_extra:,.0f}")
    print(f"Salario total (bruto): ${salario_bruto:,.0f}")
    print(f"Descuento salud y pensión (8%): ${descuento:,.0f}")
    print(f"Salario neto: ${salario_neto:,.0f}")