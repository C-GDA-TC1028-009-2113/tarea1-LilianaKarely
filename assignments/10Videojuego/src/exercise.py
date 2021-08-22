def main():
    #escribe tu código abajo de esta línea
    nuevos=int(input("Dame la cantidad de juegos nuevos: "))
    usados=int(input("Dame la cantidad de juegos usados: "))
    pagarN=nuevos*1000
    pagarU=usados*350
    print("El total de la compra es:",(pagarN+pagarU))




if __name__ == '__main__':
    main()
