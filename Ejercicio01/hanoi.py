from Pila import Pila


print("\n{:3}{:<5}  ".format("  ", "-"*50))
print("{:15}{:<0}  ".format("  ", "TORRES DE HANOI"))
print("{:3}{:<5}  ".format("  ", "-"*50))
print("\n{:3}{:<5}  ".format("  ", "La cantidad de discos debe ser mayor o igual a 3" ))

cantidad = int(input("\n{:3}{:<0}  ".format("  ", "Ingrese el numero de discos: ") ))


TorreInicial = Pila()
TorreMedio = Pila()
TorreFinal = Pila()


def Llenar_torreInicial():
    for i in range(cantidad):
        #disco = int(input())
        disco = int(input("\n{:3}{:<0}  ".format("  ","Numero del disco {}:".format(i + 1))))

        TorreInicial.items.append(disco)


def Llenar_torreFinalconInicial():
    disco_retirar = TorreInicial.pop()
    TorreFinal.items.append(disco_retirar)


def Llenar_torreFinal_Medio():
    disco_retirar = TorreMedio.pop()
    TorreFinal.items.append(disco_retirar)


def Llenar_TorreMedioconInicial():
    disco_retirar = TorreInicial.pop()
    TorreMedio.items.append(disco_retirar)


def Llenar_TorreMedioconFinal():
    disco_retirar = TorreFinal.pop()
    TorreMedio.items.append(disco_retirar)


def Llenar_TorreInicialconFinal():
    disco_retirar = TorreFinal.pop()
    TorreInicial.items.append(disco_retirar)


def Llenar_TorreInicialconMedio():
    disco_retirar = TorreMedio.pop()
    TorreInicial.items.append(disco_retirar)


if cantidad == 3:
    Llenar_torreInicial()
    print("")
    print("\n{:3}{:<25} {:<25}{:<25} ".format("  ", "TORRE INICIAL", "TORRE DEL MEDIO", "TORRE FINAL"))
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    #print("Las torre contienen los siguientes discos: ", TorreInicial.items, TorreMedio.items, TorreFinal.items)
    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    #print("Las torre contienen los siguientes discos: ", TorreInicial.items, TorreMedio.items, TorreFinal.items)
    Llenar_TorreMedioconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    #print("Las torre contienen los siguientes discos: ", TorreInicial.items, TorreMedio.items, TorreFinal.items)
    Llenar_TorreMedioconFinal()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    #print("Las torre contienen los siguientes discos: ", TorreInicial.items, TorreMedio.items, TorreFinal.items)
    Llenar_torreFinalconInicial()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    #print("Las torre contienen los siguientes discos: ", TorreInicial.items, TorreMedio.items, TorreFinal.items)
    Llenar_TorreInicialconMedio()
    print("{:3}{:<25} {:<25}{:<25} ".format("  ", str(TorreInicial.items), str(TorreMedio.items), str(TorreFinal.items)))

    #print("Las torre contienen los siguientes discos: ", TorreInicial.items, TorreMedio.items, TorreFinal.items)
