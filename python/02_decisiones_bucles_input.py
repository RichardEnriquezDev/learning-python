
# OPERADOR IF ELIF ELSE

##### IF y ELSE en Python sirven para tomar decisiones simples  ###

edad = 13

if edad >= 18:                          # Ejemplo, si edad es mayor o igual a 18 entonces haz esto
    print("Eres mayor, puedes pasar")
else:                                   # Y si no, si edad no es mayor o igual a 18, haz esto otro 
    print("Todavía no tienes la edad suficiente, no puedes pasar")

### IF, ELIF, ELSE - múltiples condiciones ###

edad = 15

if edad < 13:
    print("¡Eres un niño!")
elif edad < 18:                  # elif me permite probar otras opciones sin terminar la condición
    print("¡Eres adolescente!")
else:
    print("¡Eres un adulto!")

###############################################################################

# IF con operadores lógicos (AND, OR, NOT)

edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes ingresar al concierto")
else:
    print("No puedes ingresar al concierto")

##

edad = 15
acompañado = True
prohibido = False

if (edad >= 18 or acompañado) and not prohibido:
    print("Puedes entrar al cine")
else:
    print("No puedes ingresar al cine")

##################################################################

# Bucle FOR: repeticiones conocidas
# Repetir una cantidad conocida 2 veces

for i in range(1, 11):
    print(i)

# Bucle For - recorriendo listas

mi_lista = ["Programación", "Matemáticas", "Inglés"]

for materias in mi_lista:
    print(materias)

# FOR + IF

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

### Bucle While: se repite un código hasta que se cumple una condición ###

password = ""

while password != "python123":
    password = input("Ingrese su contraseña: ")

print("Contraseña correcta. Permitido el ingreso.")

# WHILE + BREACK: salida manual del código

while True:
    opcion = input("Escriba 'salir' para terminar: ")

    if opcion == "salir":
        print("Programa terminado")
        break

##############################################################################

# Continue y Breack: Sirven para alterar el comportamiento de un for o while

for i in range(1, 11):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

# Ejemplo práctico de breack

passwords = ["1234", "admin", "python123", "qwerty"]

for p in passwords:
    if p == "python123":
        print("Contraseña encontrada")
        break

# Ejemplo práctico de continue

numeros = [5, -3, 7, -1, 0, 4]

for n in numeros:
    if n < 0:
        continue
    print(n)

##################################################################

# Ejemplos interactivos con INPUT (requieren input del usuario)

#### Color oficial del club

color_club = ""

while color_club != "Granate":
    color_club = input("¿Cuál es el color oficial del club?: ")    

    if color_club != "Granate":
        print("No, " + color_club + " no es el color oficial del club. Intenta de nuevo")

print("Corecto " + color_club + " es el color oficial del club")

#### Suma de los dígitos de un número

tu_numero = int (input("Ingrese un número de dos dígitos: "))

if tu_numero > 9 and tu_numero < 100:
    i = tu_numero % 10
    tu_numero //= 10
    suma = i + tu_numero
    print("La suma de sus dígitos es: ",suma)
else:
    print("El número no es de dos dígitos")

###############################################################################

# Ejemplos de 'input' con los operadores lógicos (AND, OR, NOT)

#### Acceso de entrada

edad = int(input("Ingrese su edad por favor: "))
tiene_entrada = input("¿Tienes tu entrada (s/n): ") == "s"

if edad >= 18 and tiene_entrada:
    print("Puedes ingresar al concierto")
else:
    print("No puedes ingresar al concierto")

#### Ingreso al cine

edad = int(input("Ingrese su edad por favor: "))
acompañado = input("¿Estas acompañado por un mayor? (s/n): ") == "s"
prohibido = input("¿Tienes prohibición para entrar? (s/n): ") == "s"

if (edad >= 18 or acompañado) and not prohibido:
    print("Puedes entrar al cine")
else:
    print("No puedes ingresar al cine")