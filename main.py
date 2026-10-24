
#ESTIBEN ALEJANDRO LOZANO USECHE

print("Calculadora de Notas Instituto i3")

nombre = input("SARAY LIZETH LOZANO USECHE: ")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("\nNombre:", nombre)
print("Promedio:", round(promedio, 2))

if promedio >= 3.0:
    print("El estudiante aprobo")
else:
    print("El estudiante reprobo")
