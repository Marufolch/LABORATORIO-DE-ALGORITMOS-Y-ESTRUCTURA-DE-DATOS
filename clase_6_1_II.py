abrir_archivo = open('texto_prueba.txt')
leer_archivo = abrir_archivo.read()
print(leer_archivo)
abrir_archivo.close
print('****************')

abrir_archivo = open('texto_prueba.txt')
una_linea = abrir_archivo.readline()
print(una_linea)
abrir_archivo.close

print('****************')
abrir_archivo = open('texto_prueba.txt')
dos_lineas= abrir_archivo.readline()
dos_lineas= abrir_archivo.readline()
print(dos_lineas)
abrir_archivo.close
print('****************')

# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
archivo2 = open('mi_archivo.txt','w')

archivo2_modificado= archivo2.write("Nuev texto")
archivo2.close()

open_archivo= open('mi_archivo.txt')
print(open_archivo.read())
archivo2.close()

# Práctica Crear y Escribir Archivos 2
# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
with open('mi_archivo.txt', 'a') as archivo2:
    archivo2.write('\n Nuevo inicion de sesion')
    
with open('mi_archivo.txt', 'r') as archivo2:
    print(archivo2.read())
    

# Práctica Crear y Escribir Archivos 3
# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" .
# Inserta un tabulador entre cada elemento de la lista para separarlos.
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# Imprime el contenido completo de "registro.txt" al finalizar.
# Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
with open('registro.txt', 'w') as archivo3:
    archivo3.writelines(["Federico", "\t.20/12/2021", "\t.08:17:32 hs", "\t.Sin errores de carga"])
    
with open('registro.txt', 'r') as archivo3:
    print(archivo3.read())