"""
Ejercicio Nro8 - Cajero Automático: realizar un programa que simule un cajero automático con un saldo inicial de 1000$ y tendrá un menú con estas opciones:

1.- Ingresar dinero en la cuenta.
2.- Retirar dinero de la cuenta.
3.- Mostrar saldo disponible.
4.- Salir.

"""

print("CAJERO AUTOMATICO")
print("Opciones:")
print("1 para DEPOSITAR dinero en la cuenta")
print("2 para RETIRAR dinero en la cuenta")
print("3 para MOSTRAR DINERO DISPONIBLE en la cuenta")
print("4 para SALIR")

saldo = 1000

while True:
    opcion = int(input("¿Que desea realizar? "))
    if opcion == 1:
        depo = float(input("Ingrese el monto a depositar: "))
        saldo += depo
    elif opcion == 2:
        reti = float(input("Ingrese el monto a retirar: "))
        if reti > saldo:
            print("Dinero insuficiente")
        else:
            saldo -= reti
    elif opcion == 3:
        print(f"La cuenta tiene monto disponible de: {saldo}")
    elif opcion == 4:
        print("Hasta pronto!")
        break
    else:
        print("ERROR! No existe esa opcion :(")
