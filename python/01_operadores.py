
##############################################################

# OPERADORES ARITMETICOS - Ejemplos

variable_suma = 10 + 3 

print("Suma: 10 + 3 = " + str(variable_suma))

# Agregare una interpolación, f{}, que todavía no la estudié para poder simplificar

print( f"Suma: 10 + 3 = {10 + 3}") # Suma

print( f"Resta: 2 - 15 = {2 - 15}") # Resta

print( f"Multiplica: 7 * 2 = {7 * 2}") # Multiplicación

print( f"Divide: 25 / 5 = {25 / 5}") # División

print( f"Módulo: 25 % 5 = {25 % 5}") # Módulo 

# Módulo refiere al resto de una división, por ejemplo en el ejercicio anterior 25/5 el resultado seria 5, pero el resto sería 0, entonces cero sería nuestro módulo, mas adelante veremos mejor otros ejemplos para entenderlos

print( f"Exponente: 4 ** 2 = {4 ** 2}") # Potencia

print( f"Division entera: 30 // 4 = {30 // 4}") # División entera

# La división entera refiere a que el programa nos entrega un número entero en la división aunque el resultado diera decimales. En el ejemplo 30 dividido entre 4 daría 7.5, pero el programa nos arroja solo 7, el entero. También más adelante lo veremos con más presición.

##################################################################

# OPERADORES DE COMPARACION

print( f"Igualdad: 25 == 5 = es {25 == 5}")

# El operador de igualdad en nuestros ejemplos con números, nos compara si dos números son iguales, el resultado será una expreción booleana, si es igual nos dirá True pero si es incorrecta dirá False, como en el de nuestro ejemplo.

# Este operador también lo podemos utilizar en otros ejemplos, como en lineas de texto

print( f"Desigualdad: 25 != 5 = es {25 != 5}")

print( f"Mayor que: 25 > 5 = {25 > 5}")

print( f"Menor que: 25 < 5 = {25 < 5}")

print( f"Mayor o igual que: 25 >= 25 = {25 >= 25}")

print( f"Menor o igual que: 25 <= 5 = {25 <= 5}")

##################################################################

# OPERADORES LOGICOS

print( f"AND &&: 25 > 5 and 25 >= 25 = {25 > 5 and 25 >= 25}") # Esto 'y' esto para que se cumpla la condición

print( f"OR ||: 25 < 3 or 25 >= 52 = {25 < 3 or 25 >= 52}") # Esto 'o' esto para que se cumpla la condición

print( f"NOT !: not 10 == 3 = {not 10 == 3}") # Esto 'no es' esto para que se cumpla la condición

#######################################################################

# OPERADORES DE ASIGNACION

my_number = 25

# En este ejemplo, como vimos antes, el signo '=', es un operador de asignación. A la variable "my_number", le asigna de valor de un numero, aunque también se puede usar para textos, ect.

print(my_number)

my_number += 7 # Esta es una suma y una asignación

print(my_number)

# Este le suma un valor numérico a la variable my_number

my_number -= 7 # resta y asignación

print(my_number)

my_number *= 7 # multiplicacion y asignación

print(my_number)

my_number /= 7 # division y asignación

print(my_number)

my_number **= 2 # potencia y asignación

print(my_number)

my_number %= 2 # modulo y asignación

print(my_number)

my_number //= 2 # division entera y asignación

print(my_number)

####################################################################

# OPERADORES DE PERTENENCIA (Solo conozco para que sirve, por ahora)

# Nos permite averiguar si algo pertenece a otra cosa

print(f"'i' in 'Richard' = { 'i' in 'Richard'}")
print(f"'i' not in 'Richard' = { 'i' not in 'Richard'}")

####################################################################

# OPERADORES BINARIOS

# Primero pasaremos los números decimales a binarios para entender

a = 10  # 1010 
b = 3  # 0011

print(f"AND: 10 & 3 = {10 & 3}")

# Este operador compara los números binarios por posición
# si los bits son  1 coloca 1, y si no 0.
# La primera fila no son 1 coloca 0
# La segunada son dos 1, iguales, coloca 1
# La tercera son dos 0, no son 1, coloca 0
# Y la tercera no son 1 iguales, coloca 0
# De manera que, por orden coloca 0010 en binario, 2 en decimal.

print(f"OR: 10 | 3 = {10 | 3}") # Si al menos unos de los dos comparados es 1 coloca 1

print(f"XOR: 10 ^ 3 = {10 ^ 3}") # Si los comparados son diferentes coloca 1, si son iguales coloca 0

print(f"NOT: ~10 = {~10}") # Cambia el valor asignado bit a bit

print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  

print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") 

# Hace un desplazamiento bit a bit hacia una dirección tantas veces se le pida. Si el valor de 10 en binario es 1010, al desplazar los bit una vez a la derecha nos queda 0101, al desplazar una segunda ves nos queda 0010
# debemos ir llenando con 0 los espacios vacios entonces 0010 es 2 decimal.