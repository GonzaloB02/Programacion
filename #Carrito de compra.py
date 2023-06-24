#Carrito de compra

Codigo = ""
Productos = {"Producto" : ["SHAMPOO", "MANZANA", "JABON", "LAVANDINA", "VINO"],
             "Cantidad" : [3, 8, 17, 5, 2],
             "Precio" : [25, 25, 10, 15, 30],
             "Codigo" : [1111, 1112, 1113, 1114, 1115],
             "Tipo" : ["Higiene", "Alimento", "Higiene", "Limpieza", "Bebida"]}
Carrito = {"Producto": [],
           "Cantidad" : [],
           "Codigo" : [],
           "Tipo" : [],
           "SubTotal" : []}
Agregar = ""
Total = 0


def BuscarProducto():
    Encontrado = False
    while True:
        try:
            Buscador = input("Ingrese el nombre producto que desea buscar: ").upper()
            #print(Buscador)
            for i in range (len(Productos["Producto"])):
                if str(Buscador) == Productos["Producto"][i].strip():
                    print(f"""
                        Nombre:{Productos['Producto'][i]}
                        Precio:{Productos['Precio'][i]}
                        Codigo:{Productos['Codigo'][i]}
                        Cantidad:{Productos['Cantidad'][i]}
                        Tipo:{Productos['Tipo'][i]}""")
                    Encontrado = True
                    break
                #Si habillito esto solo me deja encontrar el "SHAMPOO" pero con los demas los saltea
                #elif int(Buscador) == Productos["Codigo"][i]:
                    #print(f"""
                        #Nombre:{Productos['Producto'][i]}
                        #Precio:{Productos['Precio'][i]}
                        #Codigo:{Productos['Codigo'][i]}
                        #Cantidad:{Productos['Cantidad'][i]}
                        #Tipo:{Productos['Tipo'][i]}""")
                    #Encontrado = True
                    #break

            if Encontrado == False:
                print("Producto no encontrado")   
            Encontrado = False
            while True:
                Decision = input("Desea volver al menu principal?(Y/N): ").upper()
                if Decision == "Y":
                    return()
                if Decision == "N":
                    break
                else: 
                    print("Codigo erroneo, intente otra vez: ")
        except ValueError:
            continue


def ProductosCarrito():
    global Carrito
    global Total
    Validacion = False
    Opcion = ""
    while True:
        try:
            Agregar = input("Ingrese el nombre del producto que desee agregar al carrito: ").upper()
            for i in range (len(Productos["Producto"])):
                if Productos["Producto"][i].upper() == Agregar:
                    print(f"""
                        Nombre:{Productos['Producto'][i]}
                        Codigo:{Productos['Codigo'][i]}
                        Precio:{Productos['Precio'][i]}
                        Cantidad:{Productos['Cantidad'][i]}""")
                    Validacion = True
                    Cant = input("Ingrese la cantidad que desea agregar al carrito: ")
                    if not str.isdigit(Cant):
                        print(f"{Cant} no es un numero valido, intente otra vez")
                        break
                    while True:
                        Opcion = input("Esta seguro de agregar este producto? Y/N: ").upper()
                        if str.isdigit(Cant) and int(Cant) != 0:
                            if int(Cant) <= Productos["Cantidad"][i]:
                                Validacion = True
                            else:
                                print("Cantidad no valida o fuera del rango, intente otra vez")
                                break
                        if Opcion == "Y":
                            Cant = int(Cant)
                            SubTotal = Cant * Productos["Precio"][i]
                            Total += SubTotal
                            Carrito["Producto"].append(Agregar)
                            Carrito["Cantidad"].append(Cant) 
                            Productos["Cantidad"][i] -= Cant
                            Carrito["Codigo"].append(Productos["Codigo"][i]) 
                            Carrito["SubTotal"].append(SubTotal)
                            Carrito["Tipo"].append(Productos["Tipo"][i])
                            SubTotal = 0
                            break
                        elif Opcion == "N":
                            break
                        else:
                            print("La opcion que ha ingresado ha sido incorrecta, intente otra vez")
                    #print(Carrito)
            if Validacion == False:
                print("Producto no encontrado")
            Validacion = False
            while True:
                Decision = input("Desea volver al menu principal?(Y/N):").upper()
                if Decision == "Y":
                    return()
                if Decision == "N":
                    break
                else:
                    print("Codigo erroneo")
        except ValueError:
            continue

#Validacion basica completada
#Proceso basico a completar (Necesito terminar completamente las anteriores 2 funciones)
def IngresarCarrito():
    Eleccion = ""
    Modificar = ""
    global Carrito
    Cantidad = 0
    global Total
    while True:
        try:
            Eleccion = input("""
                1. Mostrar carrito
                2. Modificar carrito
                """)
            if Eleccion == "1":
                print("Producto   Cantidad   SubTotal")
                for i in range(len(Carrito["Producto"])):
                    if Carrito["Cantidad"][i] > 0:
                        a = Carrito["Producto"][i].ljust(12)
                        b = str(Carrito["Cantidad"][i]).ljust(10)
                        c = str(Carrito["SubTotal"][i]).ljust(10)
                        print(f"{a}{b}{c}")
                print(f"Total: {Total}")
                

            if Eleccion == "2":
                Modificar = input("Que producto desea modificar: ").upper()
                for i in range(len(Carrito["Producto"])):
                    if Modificar == Carrito["Producto"][i]:
                        print(Carrito)
                        CantidadCarrito = Carrito["Cantidad"][:]
                        CantidadProducto = Productos["Cantidad"][:]
                        while True:
                            try:
                                Cantidad = input("Ingrese la cantidad que desea aumentar/restar: (agregue un más o menos delante del número)")
                                if Cantidad[0] in ("+", "-") and len(Cantidad) > 1:
                                    Cantidad = int(Cantidad)
                                    if Cantidad > 0:
                                        if Cantidad <= CantidadProducto[i]:
                                            CantidadCarrito[i] += Cantidad
                                            CantidadProducto[i] -= Cantidad
                                            break
                                        else:
                                            print("La cantidad que desea agregar no se encuentra en stock, ingrese otra cantidad")
                                            break
                                    elif Cantidad < 0:
                                        if abs(Cantidad) <= CantidadCarrito[i]:
                                            CantidadCarrito[i] += Cantidad
                                            CantidadProducto[i] -= abs(Cantidad)
                                            Total -= ((Carrito["SubTotal"][i]) / (Carrito["Cantidad"][i]))
                                            Carrito["SubTotal"][i] = Productos["Precio"][i] * CantidadCarrito[i]
                                            if Carrito["Cantidad"][i] == 0:
                                                Carrito["Producto"].pop(i)
                                                Carrito["Cantidad"].pop(i)
                                                Carrito["Codigo"].pop(i)
                                                Carrito["Tipo"].pop(i)
                                                Carrito["SubTotal"].pop(i)
                                            break
                                        else:
                                            print("Cantidad fuera del límite, intente con otra cantidad")
                                            break
                                else:
                                    print(f"{Cantidad} no es un número válido, intente otra vez")
                            except ValueError:
                                continue

                        Carrito["Cantidad"] = CantidadCarrito[:]
                        Productos["Cantidad"] = CantidadProducto[:]

                    print(Carrito)

            Decision = input("Desea volver al menu principal?(Y/N):").upper()
            if Decision == "Y":
                break
            else:
                continue
        except ValueError:
            continue


while True:

    try:
        for i, (j, k, l) in enumerate(zip(Productos["Producto"], Productos["Precio"], Productos["Codigo"])):
                if Productos["Cantidad"][i] > 0:
                    print(f"""
                        Nombre:{j}
                        Precio:{k}
                        Codigo:{l}""")

        print('''
        1.Buscar producto detalladamente
        2.Agregar producto al carrito
        3.Ingresar al carrito
        4.Salir
        ''')

        Codigo = input("Ingrese la accion deseada: ")

        if Codigo == "1":
            BuscarProducto()

        if Codigo == "2":
            ProductosCarrito()

        if Codigo == "3":
            IngresarCarrito()

        if Codigo == "4":
            break
        
        else:
            print("Codigo erroneo")

    except ValueError:
        print("Opcion invalida")