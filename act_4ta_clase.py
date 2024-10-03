# Práctica Operadores de Comparación 1
# Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool
num1 = 36
num2 = 21
mi_bool= num1 >= num2
print(mi_bool)

# Crea dos variables (num1 y  num2):
# Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 25 **0.5
num2 = 5
mi_bool = num1 == num2
print(mi_bool)

# Práctica Operadores de Comparación 3
num1= 64*3
num2= 24*8
mi_bool = num1 != num2
print(mi_bool)

# Práctica Operadores Lógicos 1
num1=36
num2=72/2
num3=48
# Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
mi_bool= num1 > num2 and num1<num3
print(mi_bool)

# Práctica Operadores Lógicos 2
num1=36
num2=72/2
num3=48
mi_bool= num1>num2 or num1<num3
print(mi_bool)

# Práctica Operadores Lógicos 3
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool= "éxito" and "tecnología" not in frase
print(mi_bool)

# Práctica Control de Flujo 1
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
if num1>num2:
    print(f'{num1} es mayor que {num2}')
elif num2>num1:
    print(f'{num2} es mayor que {num1}')
elif num1 == num2:
    print('{num1} y {num2} son iguales')

# Práctica Control de Flujo 2
# Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

# Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:

# "Puedes conducir"

# "No puedes conducir aún. Debes tener 18 años y contar con una licencia"

# "No puedes conducir. Necesitas contar con una licencia"

# Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.

edad = 16
tiene_licencia = False
if edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
if edad >= 18 and tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")
if edad >= 18:
    print("Puedes conducir")
    
# Práctica Control de Flujo 3
# Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.
# Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
# "Cumples con los requisitos para postularte"
# "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
# "Para postularte, necesitas tener conocimientos de inglés"
# "Para postularte, necesitas saber programar en Python"
# Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.
habla_ingles = True
sabe_python = False
if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False and sabe_python==True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles ==True and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")


