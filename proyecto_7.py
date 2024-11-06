class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, balance):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance
    def __str__(self):
        return (F"Esta cuenta pertenece a {self.nombre} {self.apellido} con numero de cuenta {self.num_cuenta}, y su saldo es de ${self.balance}.")
    def depositar(self):
        try:
            print("Cuanto desea depositar?")
            deposito= float(input())
            self.balance = self.balance + deposito
        except:
            print("ingrese un monto valido.")
    def retirar(self):
        try:
            print("cuanto dinero quiere retirar?")
            retirar_dinero = float(input())
            if self.balance > retirar_dinero:
                self.balance = self.balance- retirar_dinero
            else:
                print('No tienes saldo suficiente, ingresa una cantidad menor.')
        except:
            print("Ingrese un importe valido.")
    def __str__(self):
        return (f"Esta cuenta pertenece a {self.nombre} {self.apellido} "
                f"con número de cuenta {self.num_cuenta}, y su saldo es de ${self.balance}.")
def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    num_cuenta = input("Ingrese su número de cuenta: ")
    balance = 25000 # por defecto le vamos a poner que el cajero ya sabe cual es el saldo y no se lo pregunta al cliente
    return Cliente(nombre, apellido, num_cuenta, balance )

def msj_opciones():
    print("""
¿Que operacion desea realizar?
    1- Extracciones
    2- Depositos
    3- Ver saldo
    4)- Salir""")
    
cliente1 = crear_cliente()
print(cliente1)
flag = True
print("Usted a ingresado al menu del cajero")
while flag:
    msj_opciones()
    opciones = int(input())
    match opciones:
        case 1:
            cliente1.retirar()
        case 2:
            cliente1.depositar()
        case 3:
            print(f' Su saldo es de ${cliente1.balance}')
        case 4:
            flag = False
            print("Cerrando sesion...")
    if opciones > 4:
        print("Por favor ingrese una opcion valida.")    
        