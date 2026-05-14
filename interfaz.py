import calculadora as sl

n1 = int(input("Digite el primer número: "))
n2 = int(input("Digite el segundo número: "))

print("\n--- CALCULADORA ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

opcion = input("Seleccione una opción: ")


if opcion == "1":
    print("Resultado:", sl.sumar(n1, n2))

elif opcion == "2":
    print("Resultado:", sl.restar(n1, n2))

elif opcion == "3":
    print("Resultado:", sl.multiplicacion(n1, n2))

else:
    print("Opción inválida")