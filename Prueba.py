print("Ejercicio Propuesto")
edad = int(input("¿Cuál es tu edad?"))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    for i in range(1, edad):
        print(i)
print("Nueva Linea")