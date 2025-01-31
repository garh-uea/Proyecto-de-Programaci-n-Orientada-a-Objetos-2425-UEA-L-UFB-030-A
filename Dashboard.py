import os
import subprocess

def mostrar_menu():
    while True:
        print("\nMenú Principal")
        print("1. Semana 2: Técnicas de programación")
        print("2. Semana 3: POO frente a la programación tradicional")
        print("3. Semana 4: Caracteristicas de la POO - Ejemplos del Mundo Real")
        print("4. Semana 5: Tipos de datos, Identificadores")
        print("5. Semana 6: Objetos, clases, Herencia, Polimorfismo")
        print("6. Semana 7: Constructores y Destructores")
        print("7. Salir")

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
        print("1. Mostrar código del programa")
        print("2. Ejecutar programa")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_codigo_semana_2()
        elif opcion == "2":
            ejecutar_programa_semana_2()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_semana_3():
    while True:
        print("\nSemana 3: POO frente a la programación tradicional")
        print("1. Mostrar código de Programa de Control de Temperaturas en POO")
        print("2. Mostrar código de Programa de Control de Temperaturas en Programación Tradicional")
        print("3. Ejecutar Programa de Control de Temperaturas en POO")
        print("4. Ejecutar Programa de Control de Temperaturas en Programación Tradicional")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_codigo_semana_3(opcion)
        elif opcion == "2":
            mostrar_codigo_semana_3(opcion)
        elif opcion == "3":
            ejecutar_programa_semana_3(opcion)
        elif opcion == "4":
            ejecutar_programa_semana_3(opcion)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_semana_4():
    while True:
        print("\nSemana 4: Caracteristicas de la POO - Ejemplos del Mundo Real")
        print("1. Mostrar código de Programa de Cuenta Bancaria POO")
        print("2. Mostrar código de Programa de Tienda Ropa POO")
        print("3. Ejecutar Programa de Cuenta Bancaria POO")
        print("4. Ejecutar Programa de Tienda Ropa POO")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_codigo_semana_4(opcion)
        elif opcion == "2":
            mostrar_codigo_semana_4(opcion)
        elif opcion == "3":
            ejecutar_programa_semana_4(opcion)
        elif opcion == "4":
            ejecutar_programa_semana_4(opcion)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_semana_5():
    while True:
        print("\nSemana 5: Tipos de datos, Identificadores")
        print("1. Mostrar código del programa: Sistema de Registro")
        print("2. Ejecutar programa: Sistema de Registro")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_codigo_semana_5()
        elif opcion == "2":
            ejecutar_programa_semana_5()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_semana_6():
    while True:
        print("\nSemana 6: Objetos, clases, Herencia, Polimorfismo")
        print("1. Mostrar código del programa: Tienda_Ropa_POO")
        print("2. Ejecutar programa: Tienda_Ropa_POO")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_codigo_semana_6()
        elif opcion == "2":
            ejecutar_programa_semana_6()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")



def mostrar_codigo_semana_2():
    ruta_archivo = os.path.join("Semana 2/Técnicas de Programación", "Técnicas de Programación.py")
    try:
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
            print("\n# Código: Técnicas de programación")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
    except IOError:
        print("Error: No se pudo leer el archivo")


def mostrar_codigo_semana_3(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - POO.py")
        try:
            with open(ruta_archivo, "r") as archivo:
                contenido = archivo.read()
                print("\n# Código: Temperaturas - POO")
                print(contenido)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - Programación Tradicional.py")
        try:
            with open(ruta_archivo, "r") as archivo:
                contenido = archivo.read()
                print("\n# Código: Temperaturas - Programación Tradicional")
                print(contenido)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")


def mostrar_codigo_semana_4(opcion):
    if opcion == "1":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Cuenta_Bancaria_POO.py")
        try:
            with open(ruta_archivo, "r") as archivo:
                contenido = archivo.read()
                print("\n# Código: Cuenta_Bancaria_POO")
                print(contenido)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")

    elif opcion == "2":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Tienda_Ropa_POO.py")
        try:
            with open(ruta_archivo, "r") as archivo:
                contenido = archivo.read()
                print("\n# Código: Técnicas de programación")
                print(contenido)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        except IOError:
            print("Error: No se pudo leer el archivo")


def mostrar_codigo_semana_5():
    ruta_archivo = os.path.join("Semana 5/Tipos de datos, Identificadores", "Sistema_Registro.py")
    try:
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
            print("\n# Código: Sistema_Registro")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
    except IOError:
        print("Error: No se pudo leer el archivo")


def mostrar_codigo_semana_6():
    ruta_archivo = os.path.join("Semana 6/Objetos, clases, Herencia, Polimorfismo", "Tienda_Ropa_POO.py")
    try:
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
            print("\n# Código: Tienda_Ropa_POO")
            print(contenido)
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
    if opcion == "3":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - POO.py")
        try:
            subprocess.run(["python", ruta_archivo], check=True)
        except subprocess.CalledProcessError:
            print("Error: Hubo un problema al ejecutar el programa")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
    elif opcion == "4":
        ruta_archivo = os.path.join("Semana 3/POO frente a la programación tradicional", "Temperaturas - Programación Tradicional.py")
        try:
            subprocess.run(["python", ruta_archivo], check=True)
        except subprocess.CalledProcessError:
            print("Error: Hubo un problema al ejecutar el programa")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")


def ejecutar_programa_semana_4(opcion):
    if opcion == "3":
        ruta_archivo = os.path.join("Semana 4/Caracteristicas de la POO - Ejemplos del Mundo Real", "Cuenta_Bancaria_POO.py")
        try:
            subprocess.run(["python", ruta_archivo], check=True)
        except subprocess.CalledProcessError:
            print("Error: Hubo un problema al ejecutar el programa")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
    elif opcion == "4":
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


if __name__ == "__main__":
    mostrar_menu()
