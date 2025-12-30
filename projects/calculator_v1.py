
######## Calculadora personal ##########

def pedir_numeros():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            return a, b
        except ValueError:
            print("Ingrese solo números por favor. Intentelo de nuevo: ")    
def sumar (a, b):
    return a + b
def restar (a, b):
    return a - b
def multiplicar (a, b):
    return a * b
def dividir (a, b):
    return a / b
def exponente (a, b):
    return a ** b
def porcentaje (a, b):
    return a * b / 100

while True:
    in_o_out = input("Desea operar o salir. (o/s): ")
    if in_o_out.lower() == "s":
        print("Cerrando calculadora.")
        break

    num_1, num_2 = pedir_numeros()
    operador = input("Ingrese la operación (+, -, *, /, **, %): ")
    
    if operador == "+":
        resultado = sumar(num_1, num_2)
    elif operador == "-":
        resultado = restar(num_1, num_2)
    elif operador == "*":
        resultado = multiplicar(num_1, num_2)
    elif operador == "/":
        try:
            resultado = dividir(num_1, num_2)
        except ZeroDivisionError:
            print("Error no se puede dividir por cero.")
            continue
    elif operador == "**":
        resultado = exponente(num_1, num_2)
    elif operador == "%":
        resultado = porcentaje(num_1, num_2)
    else:
        print("Opción inválida.")
        continue
    print("El resultado es: ", resultado)

### Calculadora con operaciones básicas ####