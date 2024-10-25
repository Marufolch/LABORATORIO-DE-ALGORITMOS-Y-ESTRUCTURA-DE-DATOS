# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.
def devolver_distintos(num1,num2,num3):
    total = num1+num2+num3
    if total > 15:
        print(f'el numero mayor es:  {max(num1,num2,num3)}')
    elif total < 10:
        print(f'el numero menor es: {min(num1,num2,num3)}')
    elif total <=15 and total >=10:
        print(f'el vamor intermedio es: {(num1+num2+num3)/3}')
devolver_distintos(3,6,8)

def palabra(palabra_al_azar):
    letras_ordenadas = "".join(sorted(set(palabra_al_azar)))
    print(letras_ordenadas)
    
palabra("dinosaurio")

def contar_ceros(*args):
    ceros = args.count(0)
    return print(ceros >1)

contar_ceros(2,3,7,65,0,54,3,0)


def contar_primos(num):
    cantidad_primos = 0
    for numero in range(3,num + 1):  
        es_primo = True
        for i in range(2, numero): 
            if numero % i == 0:
                es_primo = False
                break  
        if es_primo:
            print(numero)  
            cantidad_primos += 1  
    print(f'del 3 hasta el {num} hay {cantidad_primos} de numeros primos')
            
        
contar_primos(10)


# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.