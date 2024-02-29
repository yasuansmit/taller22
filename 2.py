precio_computadorE = 250
precio_computadorP = 270
precio_tabletas =120
precio_videoBem = 55
precio_televisor = 500


cantidad_computadorE = 0
cantidad_computadorP = 0
cantidad_tabletas = 0
cantidad_videoBem = 0
cantidad_televisor = 0




def facturar():
    total_computadores_escritorios =  cantidad_computadorE * precio_computadorE
    total_computadores_portatil =  cantidad_computadorP * precio_computadorP
    total_tabletas =  cantidad_tabletas * precio_tabletas
    total_videoBem =  cantidad_videoBem * precio_videoBem
    total_televisores =  cantidad_televisor * precio_televisor
    total = total_computadores_escritorios + total_computadores_portatil + total_tabletas + total_videoBem + total_televisores

    print("Factura")
    print("Cantidad de escritorios que se compro fueron: ====",cantidad_computadorE,  "El total de escritorios: ",total_computadores_escritorios)
    print("Cantidad de portatil que se compro fueron: ====",cantidad_computadorP, "El total de portatil: ",total_computadores_portatil)
    print("Cantidad de tabletas que se compro fueron:==== ",cantidad_tabletas, "El total de tabletas: ",total_tabletas)
    print("Cantidad de videoBem que se compro fueron: ====",cantidad_videoBem, "El total de videoBem: ",total_videoBem)
    print("Cantidad de televisores que se compro fueron:==== ",cantidad_televisor, "El total de televisores: ",total_televisores)
def mostrar_menu():
    
    print("Bienvenido a la tienda")
    print("==MENU==")
    print("Tenemos muchos productos como:")
    print("(1) Computadora de escritorio")
    print("(2) Computadora portatil")
    print("(3) Tabletas")
    print("(4) VideoBem")
    print("(5) Televisores")
    print("(6) Facturar")
    return input("Seleccione una opcion:")
while True:
        opcion = mostrar_menu()

        if opcion == "1":
            cantidad_computadorE += 1
        elif opcion == "2":
            cantidad_computadorP += 1
        elif opcion == "3":
            cantidad_tabletas += 1
        elif opcion == "4":
            cantidad_videoBem += 1
        elif opcion == "5":
            cantidad_televisor += 1
        elif opcion == "6":
            facturar()
            break
        else:
            print("Opcion no valida")

