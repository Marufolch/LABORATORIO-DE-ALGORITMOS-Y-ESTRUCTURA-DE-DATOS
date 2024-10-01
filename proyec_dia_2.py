print("""A continuacion debera ingresar unos datos para que el sistema pueda calcular
la comision por venta que corresponde este mes""")
nombre = input("Ingrese su nombre y apellido: ")
venta_total = float(input("Ingrese las ventas totales del mes: "))
comision = venta_total/100*13
print(f'Este mes le corresponde ${comision} de comision x sus ventas')