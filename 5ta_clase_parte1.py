# Práctica Métodos y Ayuda 1
# Remueve los caracteres a la izquierda de nuestro texto principal:

# ,

# :

# %

# _

# #

# Utiliza el método lstrip(). Imprime el resultado en pantalla:
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))
# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
# el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
print(frutas)
frutas.insert(3,"naranja")
print(frutas)
print('**************************************')
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
print(marcas_smartphones.isdisjoint(marcas_tv))
print("devuelve False dado que poseen un elemento en comun, la marca 'LG'")
# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento
print('*************************************************************')
# Práctica Crear Funciones 1
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

# Solo debes definir la función, no debes invocarla luego.
def saludar():
    print("hola mundo")
    
print('************************************************')
# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
# Solo debes definir la función y crear la variable, no debes invocar la función luego.
def bienvenida(nombre):
    nombre_persona = nombre
    print(f'bienvenido {nombre_persona}!')
    
print('**********************************************')
# Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.
# Solo debes definir la función y crear la variable, no debes invocar la función luego.
def cuadrado(un_numero):
    cuadra = un_numero ** 2
    
print('********************************************')
# Práctica Return 1
# Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:
def potencia(num1, num2):
    return  pow(num1, num2)

# Práctica Return 2
# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.
# Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.
def usd_a_eur():
    dolares = float(input("ingrese una cantidad de dolares: "))
    return  dolares*0.90


# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento,
# invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.
def invertir_palabra(palabra):
    return palabra[::-1]
