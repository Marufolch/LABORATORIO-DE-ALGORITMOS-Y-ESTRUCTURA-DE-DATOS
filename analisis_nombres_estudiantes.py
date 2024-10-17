lista_nombres = []

new_name = 0
agregar = True
print("A continuación, por favor ingrese los nombres de los estudiantes: ")
primera_letra = 0
no_primera_letra = 0
while agregar:
    new_name = input('ingrese un nombre: ')
    if new_name == "FIN":
        agregar = False
    elif new_name == "REPETIR":
        print(lista_nombres)
    elif new_name.isalpha() == False:
        print('ingres un nombre valido, el campo no puede estar vacio, contener numeros ni caracteres especiales. ')
    else:
        lista_nombres.append(new_name)
print("que desea hacer a continuacion:")
print("""presione el numero segun la opcion requerida:
      1- Monstrar los nombres ingresados
      2- Ordenar los nombres
      3- Analizar la longitud de los nombres
      4- Contar vocales y consonantes")
      5- Contar palabras en cada nombre
      6- Mostrar los nombres invertidos
      7- Mostrar nombre que empiece por una letra elegida por el usuario
      8- Buscar si un nombre esta en la lista
      9- Mostrar los nombres con mas de 5 caracteres.
      10- Convertir los nombres a mayúsculas o minúsculas.
      11- Finalizar""")
option = 0
flag = True
while flag:
    option = int(input("ingrese una opcion: "))
    match option:
     case 1:
        for i in lista_nombres:
            print(f'- {i}')
     case 2:
        lista_ordenada = sorted(lista_nombres)
        for i in lista_ordenada:
            print(f'- {i}')
     case 3:
        print(f'Ordenados alfabeticamente, el nombre mas largo es {max(lista_nombres)} y el nombre mas corto es {min(lista_nombres)}')
     case 4: 
        unir= ' '.join(lista_ordenada)
        consonante= "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vocal = "aeiouAEIOU"
        contar_vocal = 0
        contar_consonante= 0
        for i in unir:
            if i in vocal:
                contar_vocal += 1
        
        for i in unir:
            if i in consonante:
                contar_consonante += 1
        print(f'En el listado hay {contar_vocal} vocales, y hay un total de {contar_consonante} de consonantes')
     case 5:
        for i in lista_nombres:
            print(f'{i} contiene {len(i.split())} palabra(s)')
     case 6:
        print(f'Estos son los nombres al revez: ')
        for i in lista_ordenada:
            print(i[::-1])
     case 7:
        print("elige una letra para encontrar un nombre que empiece con ella:")
        elegir_letra = input("")
        for i in lista_nombres:
            if i.startswith(elegir_letra):
                primera_letra = 1
            else:
                no_primera_letra = 1
        if primera_letra== 1:
            print(f'Con la letra {elegir_letra} empieza el nombre {i.capitalize()}')
        elif  no_primera_letra == 1: 
            print("no hay ningun nombre que empiece con esa letra")
     case 8:
        buscar_nombre= input("ingrese un nombre para buscar: ")
        if buscar_nombre in lista_nombres:
            print(f'{buscar_nombre} ya esta en la lista.')
        else:
            print("ese nombre no esta en la lista.")
     case 9:
         print("Estos son los nombres que tienen mas de 5 caracteres")
         for i in lista_nombres:
             if len(i)> 5:
                 print(i)
     case 10:
         min_may= 0
         print('para ver los nombres en minuscula presione 1, para verlos en mayuscula, presione 2')
         min_may = int(input())
         if min_may == 1:
            for i in lista_nombres:
                print(i.lower())
         elif min_may == 2:
            for i in lista_nombres:
                print(i.upper())
         elif min_may != 1 and min_may != 0:
             break
             print('seleccionar una opcion del menu inicial: ')     
     case 11:
         break
print("se ha cerrado el menu.")
    
    