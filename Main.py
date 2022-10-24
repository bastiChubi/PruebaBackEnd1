from Scooter import Scooter
from Transporte import Transporte
from Tv import Tv
from Consola import Consola
from Tecnologia import Tecnologia
from Bicicleta import Bicicleta

listaTvs = []
listaConsolas = []
listaScooter = []
listaBicicleta = []


def RegistrarTv():
    voltaje = int(input("Ingrese cantidad de voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    tamano = float(input("Ingrese tamaño: "))
    t = Tv(voltaje,precio,eficiencia,marca,tamano)
    listaTvs.append(t)
    print("----------------------------------------------------")
    print("Registro exitoso")
    print(t)
    t.calcularDescuento()
    
def RegistrarConsola():
    voltaje = int(input("Ingrese cantidad de voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    nombreC = input("Ingrese nombre: ")
    version = input("Ingrese version: ")
    c = Consola(voltaje,precio,eficiencia,marca,nombreC,version)
    listaConsolas.append(c)
    print("----------------------------------------------------")
    print("Registro exitoso")
    print(c)
    c.calcularDescuento()

def RegistrarScooter():
    voltaje = int(input("Ingrese cantidad de voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    aro = float(input("Ingrese aro: "))
    velocidad = int(input("Ingrese velocidad: "))
    peso = float(input("Ingrese peso: "))
    s = Scooter(voltaje,precio,eficiencia,marca,aro,velocidad,peso)
    listaScooter.append(s)
    print("----------------------------------------------------")
    print("Registro exitoso")
    print(s)

def RegistrarBicicleta():
    aro = float(input("Ingrese aro: "))
    peso = float(input("Ingrese peso: "))
    precio = float(input("Ingrese precio: "))
    marca = input("Ingrese marca: ")
    b = Bicicleta(aro,peso,precio,marca)
    listaBicicleta.append(b)
    print("----------------------------------------------------")
    print("Registro exitoso")
    print(b)

def CotizarTvs():
    pass 

def CotizarConsolas():
    pass 

def CotizarScooters():
    pass 

def CotizarBicicletas():
    pass 


while True:
    print("-----------------------------------------")
    print("Que opcion desea")
    print("1.- Registrar")
    print("2.- Cotizar")
    opcion = input("Ingrese opcion a utilizar: ")
    if opcion == "1":
        print("-----------------------------------")
        print("Que quiere registrar")
        print("1.- Registrar TV")
        print("2.- Registrar Consola")
        print("3.- Registrar Scooter")
        print("4.- Registrar bicicleta")
        opcionn = input("Ingrese opcion a utilizar: ")
        if opcionn == "1":
            RegistrarTv()
        elif opcionn == "2":
            RegistrarConsola()
        elif opcionn == "3":
            RegistrarScooter()
        elif opcionn == "4":
            RegistrarBicicleta()
        else:
            print("Opcion erronea")
    elif opcion == "2":
        print("----------------------------------")
        print("Que quiere cotizar")
        print("1.- Cotizar TVS")
        print("2.- Cotizar Consolas")
        print("3.- Cotizar Scooters")
        print("4.- Cotizar bicicletas")
        opcionnn = input("Ingrese opcion a cotizar: ")
        if opcionn == "1":
            CotizarTvs()
        elif opcionn == "2":
            CotizarConsolas
        elif opcionn == "3":
            CotizarScooters()
        elif opcionn == "4":
            CotizarBicicletas()
        else:
            print("Opcion erronea")
        
   