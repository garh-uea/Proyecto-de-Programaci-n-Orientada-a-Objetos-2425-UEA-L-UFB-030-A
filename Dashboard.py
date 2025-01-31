import os
import subprocess
import platform

def mostrar_menu():
    while True:
        print("\n****************************** Menú Principal *******************************")
        print("* 1. Semana 2: Técnicas de programación                                      *")
        print("* 2. Semana 3: POO frente a la programación tradicional                      *")
        print("* 3. Semana 4: Caracteristicas de la POO - Ejemplos del Mundo Real           *")
        print("* 4. Semana 5: Tipos de datos, Identificadores                               *")
        print("* 5. Semana 6: Objetos, clases, Herencia, Polimorfismo                       *")
        print("* 6. Semana 7: Constructores y Destructores                                  *")
        print("* 7. Salir                                                                   *")
        print("*****************************************************************************")


        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_semana_2()
        elif opcion == "2":
            menu_semana_3()
        elif opcion == "3":
            menu_semana_4()
        elif opcion == "4":
            menu_semana_5()
        elif opcion == "5":
            menu_semana_6()
        elif opcion == "6":
            menu_semana_7()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_semana_2():
    while True:
        print("\nSemana 2: Técnicas de programación")
        print("1. Mostrar Documentación del Tema")
        print("2. Mostrar código del programa")
        print("3. Ejecutar programa")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_semana_2(opcion)
        if opcion == "2":
            mostrar_semana_2(opcion)
        elif opcion == "3":
            ejecutar_programa_semana_2()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_semana_3():
    while True:
        print("\nSemana 3: POO frente a la programación tradicional")
        print("1. Mostrar Documentación del Tema")
        print("2. Mostrar código de Programa de Control de Temperaturas en POO")
        print("3. Mostrar código de Programa de Control de Temperaturas en Programación Tradicional")
        print("4. Ejecutar Programa de Control de Temperaturas en POO")
        print("5. Ejecutar Programa de Control de Temperaturas en Programación Tradicional")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_semana_3(opcion)
        elif opcion == "2":
            mostrar_semana_3(opcion)
        elif opcion == "3":
            mostrar_semana_3(opcion)
        elif opcion == "4":
            ejecutar_programa_semana_3(opcion)
        elif opcion == "5":
            ejecutar_programa_semana_3(opcion)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_semana_4():
    while True:
        print("\nSemana 4: Caracteristicas de la POO - Ejemplos del Mundo Real")
        print("1. Mostrar Documentación del Tema")
        print("2. Mostrar código de Programa de Cuenta Bancaria POO")
        print("3. Mostrar código de Programa de Tienda Ropa POO")
        print("4. Ejecutar Programa de Cuenta Bancaria POO")
        print("5. Ejecutar Programa de Tienda Ropa POO")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_semana_4(opcion)
        elif opcion == "2":
            mostrar_semana_4(opcion)
        elif opcion == "3":
            mostrar_semana_4(opcion)
        elif opcion == "4":
            ejecutar_programa_semana_4(opcion)
        elif opcion == "5":
            ejecutar_programa_semana_4(opcion)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_semana_5():
    while True:
        print("\nSemana 5: Tipos de datos, Identificadores")
        print("1. Mostrar Documentación del Tema")
        print("2. Mostrar código del programa: Sistema de Registro")
        print("3. Ejecutar programa: Sistema de Registro")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_semana_5(opcion)
        if opcion == "2":
            mostrar_semana_5(opcion)
        elif opcion == "3":
            ejecutar_programa_semana_5()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_semana_6():
    while True:
        print("\nSemana 6: Objetos, clases, Herencia, Polimorfismo")
        print("1. Mostrar Documentación del Tema")
        print("2. Mostrar código del programa: Tienda_Ropa_POO")
        print("3. Ejecutar programa: Tienda_Ropa_POO")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_semana_6(opcion)
        if opcion == "2":
            mostrar_semana_6(opcion)
        elif opcion == "3":
            ejecutar_programa_semana_6()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_semana_7():
    while True:
        print("\nSemana 7: Constructores y Destructores")
        print("1. Mostrar Documentación del Tema")
        print("2. Mostrar código del programa: Constructores_Destructores")
        print("3. Ejecutar programa: Constructores_Destructores")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_semana_7(opcion)
        if opcion == "2":
            mostrar_semana_7(opcion)
        elif opcion == "3":
            ejecutar_programa_semana_7()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def mostrar_semana_2(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 2/Técnicas de Programación", "Técnicas de Programación.pdf")
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", ruta_archivo])
            elif platform.system() == "Windows":
                os.startfile(ruta_archivo)
            else:  # Linux y otros
                subprocess.run(["xdg-open", ruta_archivo])
            print(f"\nSe ha abierto el archivo PDF: {ruta_archivo}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo PDF en la ruta {ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el PDF: {e}")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 2/Técnicas de Programación", "Técnicas de Programación.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print(
                    "\n************************************************ Código: Técnicas de programación ************************************************")
                print(contenido)
                print(
                    "\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")


def mostrar_semana_3(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "POO frente a la programación tradicional.pdf")
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", ruta_archivo])
            elif platform.system() == "Windows":
                os.startfile(ruta_archivo)
            else:  # Linux y otros
                subprocess.run(["xdg-open", ruta_archivo])
            print(f"\nSe ha abierto el archivo PDF: {ruta_archivo}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo PDF en la ruta {ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el PDF: {e}")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - POO.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n************************************************ Código: Temperaturas - POO ************************************************")
                print(contenido)
                print("\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")

    elif opcion == "3":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - Programación Tradicional.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n************************************************ Código: Temperaturas - Programación Tradicional ************************************************")
                print(contenido)
                print("\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")


def mostrar_semana_4(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Caracteristicas de la POO.pdf")
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", ruta_archivo])
            elif platform.system() == "Windows":
                os.startfile(ruta_archivo)
            else:  # Linux y otros
                subprocess.run(["xdg-open", ruta_archivo])
            print(f"\nSe ha abierto el archivo PDF: {ruta_archivo}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo PDF en la ruta {ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el PDF: {e}")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Cuenta_Bancaria_POO.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n************************************************ Código: Cuenta_Bancaria_POO ************************************************")
                print(contenido)
                print("\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")

    elif opcion == "3":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Tienda_Ropa_POO.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n************************************************ Código: Tienda Ropa POO ************************************************")
                print(contenido)
                print("\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")


def mostrar_semana_5(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 5/Tipos de datos, Identificadores", "Tipos de datos, Identificadores.pdf")
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", ruta_archivo])
            elif platform.system() == "Windows":
                os.startfile(ruta_archivo)
            else:  # Linux y otros
                subprocess.run(["xdg-open", ruta_archivo])
            print(f"\nSe ha abierto el archivo PDF: {ruta_archivo}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo PDF en la ruta {ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el PDF: {e}")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 5/Tipos de datos, Identificadores", "Sistema_Registro.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n************************************************ Código: Sistema_Registro ************************************************")
                print(contenido)
                print("\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")


def mostrar_semana_6(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 6/Objetos, clases, Herencia, Polimorfismo", "Objetos, clases, Herencia, Polimorfismo.pdf")
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", ruta_archivo])
            elif platform.system() == "Windows":
                os.startfile(ruta_archivo)
            else:  # Linux y otros
                subprocess.run(["xdg-open", ruta_archivo])
            print(f"\nSe ha abierto el archivo PDF: {ruta_archivo}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo PDF en la ruta {ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el PDF: {e}")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 6/Objetos, clases, Herencia, Polimorfismo", "Tienda_Ropa_POO.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n************************************************ Código: Tienda_Ropa_POO ************************************************")
                print(contenido)
                print("\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")


def mostrar_semana_7(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 7/Constructores y Destructores", "Constructores y Destructores.pdf")
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", ruta_archivo])
            elif platform.system() == "Windows":
                os.startfile(ruta_archivo)
            else:  # Linux y otros
                subprocess.run(["xdg-open", ruta_archivo])
            print(f"\nSe ha abierto el archivo PDF: {ruta_archivo}")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo PDF en la ruta {ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el PDF: {e}")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 7/Constructores y Destructores", "Constructores_Destructores.py")
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n************************************************ Código: Constructores_Destructores ************************************************")
                print(contenido)
                print("\n********************************************************* Fin del Código *********************************************************")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")



def ejecutar_programa_semana_2():
    ruta_archivo = os.path.join("Semana 2/Técnicas de Programación", "Técnicas de Programación.py")
    try:
        subprocess.run(["python", ruta_archivo], check=True)
    except subprocess.CalledProcessError:
        print("Error: Hubo un problema al ejecutar el programa")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")


def ejecutar_programa_semana_3(opcion):
    if opcion == "4":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - POO.py")
        try:
            subprocess.run(["python", ruta_archivo], check=True)
        except subprocess.CalledProcessError:
            print("Error: Hubo un problema al ejecutar el programa")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
    elif opcion == "5":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - Programación Tradicional.py")
        try:
            subprocess.run(["python", ruta_archivo], check=True)
        except subprocess.CalledProcessError:
            print("Error: Hubo un problema al ejecutar el programa")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")


def ejecutar_programa_semana_4(opcion):
    if opcion == "4":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Cuenta_Bancaria_POO.py")
        try:
            subprocess.run(["python", ruta_archivo], check=True)
        except subprocess.CalledProcessError:
            print("Error: Hubo un problema al ejecutar el programa")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
    elif opcion == "5":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Tienda_Ropa_POO.py")
        try:
            subprocess.run(["python", ruta_archivo], check=True)
        except subprocess.CalledProcessError:
            print("Error: Hubo un problema al ejecutar el programa")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")


def ejecutar_programa_semana_5():
    ruta_archivo = os.path.join("Semana 5/Tipos de datos, Identificadores", "Sistema_Registro.py")
    try:
        subprocess.run(["python", ruta_archivo], check=True)
    except subprocess.CalledProcessError:
        print("Error: Hubo un problema al ejecutar el programa")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")


def ejecutar_programa_semana_6():
    ruta_archivo = os.path.join("Semana 6/Objetos, clases, Herencia, Polimorfismo", "Tienda_Ropa_POO.py")
    try:
        subprocess.run(["python", ruta_archivo], check=True)
    except subprocess.CalledProcessError:
        print("Error: Hubo un problema al ejecutar el programa")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")


def ejecutar_programa_semana_7():
    ruta_archivo = os.path.join("Semana 7/Constructores y Destructores", "Constructores_Destructores.py")
    try:
        subprocess.run(["python", ruta_archivo], check=True)
    except subprocess.CalledProcessError:
        print("Error: Hubo un problema al ejecutar el programa")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")

if __name__ == "__main__":
    mostrar_menu()
