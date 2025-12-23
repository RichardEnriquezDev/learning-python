
# Funciones que devuelven valores (return)

def suma_dos_numeros(num1, num2):
    return num1 + num2
print(suma_dos_numeros(15, 7))

def par_o_impar(numero):
    return numero % 2 == 0

numero = int(input("Ingrese un número por favor: ")) 

resultado = par_o_impar(numero)
if resultado:
    print("Es par")
else:
    print("Es impar")
        
def par_o_impar_texto(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"
numero_par_impar = par_o_impar_texto(43)
print(numero_par_impar)

##### Entrelazar dos fuciones #####


numero = int(input("Ingrese un número por favor: ")) 

def es_par_o_impar(numero):
    return numero % 2 == 0

numero_texto = es_par_o_impar(numero)

def definir_texto(numero_texto):
    if numero_texto:
        return "Es par"
    else:
        return "Es impar"

mensaje = definir_texto(numero_texto)
print(mensaje)

### Determinar un número ###


def number_to_determined(number_in):
    if number_in > 0:
        return "Es positivo"
    elif number_in < 0:
        return "Es negativo"
    else:
        return "Es cero"

number_in = int(input("Ingrese el número a determinar: "))
specified_number = number_to_determined(number_in)
print(specified_number)
