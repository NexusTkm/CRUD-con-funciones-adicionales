import os
import time
estatus_producto = "Activo"
try:
    def ultimo_id():
        with open("Constructora.txt", 'r', encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if lineas:
                ultimo_id = int(lineas[-1].strip().split('-')[0]) + 1
            else:
                ultimo_id = 1
            return ultimo_id

    def registrar(): 
        while True:
            nuevo_id = ultimo_id()
            id_producto = str(nuevo_id).zfill(3)
            nombre_producto = input("Ingrese el nombre del producto: ")
            if nombre_producto.strip() == "":
                print("No se insertaron registros")
                print("Regresando al menú principal...")
                time.sleep(0.5)
                return menu()
            cantidad_producto = input("Ingrese la cantidad de producto: ")
            precio_producto = input("Ingrese el precio del producto: ")
            precio_con_pesos = f"${precio_producto}"
            print("El estatus es: ", estatus_producto)
        
            with open("Constructora.txt", "a", encoding="utf-8") as Nx:
                Nx.write(f"{id_producto} -  {nombre_producto} -   {cantidad_producto}       -  {precio_con_pesos}      -  {estatus_producto}\n")
            opcion = input("Presione [1] Para Continuar y [0] Para Regresar al menú principal: ")
            if opcion != '1':
                print("Regresando al menú principal...")
                time.sleep(0.5)
                return menu()

    def modificar():
        while True:
            Id_producto = input("Ingresa el ID del producto que deseas modificar: ")
            encontrado = False
            lineas_m = []
            with open("Constructora.txt", "r", encoding="utf-8") as Archvio:
                lineas = Archvio.readlines()
            for linea in lineas:
                if Id_producto in linea:
                    encontrado = True
                    print("ID  -  Nombre   -  Cantidad  -  Precio  -  Estatus")
                    print(linea.strip())
                    confirmacion = input("¿Deseas modificar este producto? (Si[1]/No[0]): ").strip()
                    if confirmacion == "1":
                        while True:
                            print("Selecciona qué campo deseas modificar:")
                            print("[1] Nombre")
                            print("[2] Cantidad")
                            print("[3] Precio")
                            opcion = input("Ingresa el número correspondiente a la opción: ").strip()
                            if opcion not in ['1', '2', '3']:
                                print("Opción no válida. Por favor, ingresa un número válido.")
                                continue
                            nuevo_valor = input("Ingrese el nuevo valor: ")
                            posicion = linea.split(' - ')
                            if opcion == '1':
                                posicion[1] = nuevo_valor
                            elif opcion == '2':
                                posicion[2] = nuevo_valor
                            elif opcion == '3':
                                posicion[3] = nuevo_valor
                            nueva_linea = ' - '.join(posicion)
                            lineas_m.append(nueva_linea + '\n')
                            print("Producto modificado con éxito.")
                            break
                    with open("Constructora.txt", "w", encoding="utf-8") as Archvio:
                        Archvio.writelines(lineas_m)
                else:
                        lineas_m.append(linea)
            else:
                lineas_m.append(linea)

            if not encontrado:
                print("No se encontró ningún producto con el ID especificado.")
                return menu()
            opcion = input("Presione [1] Para Continuar y [0] Para Regresar al menú principal: ")
            if opcion != '1':
                print("Regresando al menú principal...")
                time.sleep(0.5)
                return menu()

    def consultas():
        while True:
            Id_producto = input("Ingresa el ID del producto que deseas consultar: ")
            with open("Constructora.txt", "r") as Nx:
                for linea in Nx:
                    if linea[:3] == Id_producto:
                        elementos = linea.strip().split('-')
                        id_producto = elementos[0].strip()
                        nombre = elementos[1].strip()
                        cantidad = elementos[2].strip()
                        precio = elementos[3].strip()
                        estatus = elementos[4].strip()
                        print("ID:", id_producto)
                        print("Nombre:", nombre)
                        print("Cantidad:", cantidad)
                        print("Precio:", precio)
                        print("Estatus:", estatus)
                opcion = input("Presione [1] Para Continuar y [0] Para Regresar al menú principal: ")
                if opcion != '1':
                    print("Regresando al menú principal...")
                    time.sleep(0.5)
                    return menu()

    def baja():
        while True:
            with open("Constructora.txt", 'r', encoding="utf-8") as Nx:
                lineas = Nx.readlines()
            id_linea = int(input("Ingrese el ID que desea dar de baja: ")) - 1
            if id_linea < 0 or id_linea >= len(lineas):
                print("ID de línea inválido.")
                return
            print("ID  -  Nombre   -  Cantidad  -  Precio  -  Estatus")
            print(lineas[id_linea].strip())
            confirmacion = input("¿Desea dar de baja? (Si[1]/No[0]): ").strip()
            if confirmacion == "1":
                nueva_linea = lineas[id_linea].replace("Activo", "Inactivo")
                lineas[id_linea] = nueva_linea
                with open("Constructora.txt", 'w', encoding="utf-8") as Nx_escritura:
                    Nx_escritura.writelines(lineas)
                print("Baja Exitosa")
            else:
                print("Operación cancelada.")
            opcion = input("Presione [1] Para Continuar y [0] Para Regresar al menu principal: ")
            if opcion != '1':
                    print("Regresando al menú principal...")
                    time.sleep(0.5)
                    return menu()

    def alta():
        while True:
            with open("Constructora.txt", 'r', encoding="utf-8") as Nx:
                lineas = Nx.readlines()

            id_linea = int(input("Ingrese el ID que desea dar de alta: ")) - 1

            if id_linea < 0 or id_linea >= len(lineas):
                print("ID de línea inválido.")
                return
        
            print("ID  -  Nombre   -  Cantidad  -  Precio  -  Estatus")
            print(lineas[id_linea].strip())
            confirmacion = input("¿Desea dar de Alta? (Si[1]/No[0]): ").strip()

            if confirmacion == "1":
                nueva_linea = lineas[id_linea].replace("Inactivo", "Activo")
                lineas[id_linea] = nueva_linea

                with open("Constructora.txt", 'w', encoding="utf-8") as Nx_escritura:
                    Nx_escritura.writelines(lineas)

                print("Alta Exitosa")
            else:
                print("Operación cancelada.")
            opcion = input("Presione [1] Para Continuar y [0] Para Regresar al menu principal: ")
            if opcion != '1':
                    print("Regresando al menú principal...")
                    time.sleep(0.5)
                    return menu()

    def respaldar():
        while True:
            with open("Constructora.txt", "r", encoding="utf-8") as original:
                nombre_respaldo = input("Ingrese el nombre el nuevo archivo de respaldo: ")
                with open(nombre_respaldo, "w", encoding="utf-8") as respaldo:
                    for linea in original:
                        respaldo.write(linea)
            print("El Archivo está respaldado.")
            opcion = input("Presione [1] Para Continuar y [0] Para Regresar al menú principal: ")
            if opcion != '1':
                print("Regresando al menú principal...")
                time.sleep(0.5)
                return menu()

    def listar():
        while True:
            print("Elija cómo desea listar el contenido: ")
            print("[1] Activo")
            print("[2] Inactivo")
            print("[3] Todos ")
            opcion_estatus = input("Ingrese el número correspondiente a su elección: ")

            if opcion_estatus not in ['1', '2', '3']:
                return listar()

            with open("Constructora.txt", 'r', encoding="utf-8") as Nx:
                print("ID  -  Nombre   -  Cantidad  -  Precio  -  Estatus")
                for linea in Nx:
                    datos = linea.strip().split('  -  ')
                    if opcion_estatus == '3' or (opcion_estatus == '1' and datos[-1] == 'Activo') or (opcion_estatus == '2' and datos[-1] == 'Inactivo'):
                        print(linea.strip())
            opcion = input("Presione [1] Para Continuar y [0] Para Regresar al menú principal: ")
            if opcion != '1':
                print("Regresando al menú principal...")
                time.sleep(0.5)
                return menu()

    def salir():
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu():
        salir()
        print("╔═══════════════════════════════════════════╗")
        print("║             CONSTRUMATERIALES             ║")
        print("╚═══════════════════════════════════════════╝")
        print("¡Bienvenido al menú de la <CONSTRUMATERIALES>!")
        print(" Elige una de las siguientes opciones")
        print("[1] Registrar")
        print("[2] Modificar")
        print("[3] Consultar")
        print("[4] Dar de baja")
        print("[5] Dar de alta ")
        print("[6] Respaldar")
        print("[7] Listar")
        print("[8] Salir")
        opcion = input("Elige la acción que deseas realizar [1-8]: ")
        if opcion == "":
            print("¡Seleccione una Opcion!")
            time.sleep(0.5)
            return menu()
        elif opcion == "1":
            print("MENU DE REGISTRO")
            registrar()
        elif opcion == "2":
            print("MENU DE MODIFICACIONES")
            modificar()
        elif opcion == "3":
            print("MENU DE CONSULTAS")
            consultas()
        elif opcion == "4":
            print("MENU DE BAJAS")
            baja()
        elif opcion == "5":
            print("MENU DE ALTAS")
            alta()
        elif opcion == "6":
            print("MENU DE RESPALDOS")
            respaldar()
        elif opcion == "7":
            print("MENU DE LISTADO")
            listar()
        elif opcion == "8":
            print("Cerrando el Programa...")
            time.sleep(0.5)
            salir()
            print("¡Programa Cerrado con exito!")
        else:
            print("La acción que deseas realizar no es válida")
    if __name__ == "__main__":
        menu()
except FileNotFoundError as e:
    print("El archivo especificado no se encuentra")
except IOError as e:
    print("Error al leer el archivo")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("Error")