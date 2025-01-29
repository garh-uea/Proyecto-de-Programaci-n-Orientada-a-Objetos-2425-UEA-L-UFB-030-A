# Función para mostrar el menú de selección de ciudad
def mostrar_menu():
    print("\nSeleccione una ciudad para ingresar las temperaturas:")
    print("1. Guayaquil")
    print("2. Quito")
    print("3. Cuenca")
    print("4. Tena")
    opcion = int(input("Ingrese el número de la ciudad: "))
    return opcion

# Función para ingresar los datos de clima de una ciudad seleccionada
def ingresar_datos_clima(ciudad):
    print(f"\nIngresando datos para {ciudad}")
    temperaturas = []  # Lista para almacenar las temperaturas diarias
    print("Ingrese las temperaturas para los días de la semana:")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        temperatura = float(input(f"Temperatura del {dia}: "))  # Pedir temperatura diaria
        temperaturas.append(temperatura)  # Agregar temperatura a la lista
    return temperaturas  # Devolver las temperaturas ingresadas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    total_temperaturas = sum(temperaturas)  # Sumar todas las temperaturas
    return total_temperaturas / len(temperaturas)  # Calcular el promedio

# Función principal del programa
def main():
    # Lista de nombres de ciudades
    ciudades = ["Guayaquil", "Quito", "Cuenca", "Tena"]

    # Mostrar menú y seleccionar ciudad
    opcion = mostrar_menu()
    if opcion < 1 or opcion > 4:
        print("Opción no válida")
        return

    ciudad_seleccionada = ciudades[opcion - 1]  # Obtener el nombre de la ciudad seleccionada
    temperaturas = ingresar_datos_clima(ciudad_seleccionada)  # Ingresar datos para la ciudad seleccionada

    # Calcular y mostrar promedio semanal
    promedio_semanal = calcular_promedio_semanal(temperaturas)  # Calcular promedio
    print(f"\nPromedio semanal de temperaturas en {ciudad_seleccionada}: {promedio_semanal:.2f}°C")

# Función para mostrar el menú de selección de ciudad
def mostrar_menu():
    print("\nSeleccione una ciudad para ingresar las temperaturas:")
    print("1. Guayaquil")
    print("2. Quito")
    print("3. Cuenca")
    print("4. Tena")
    opcion = int(input("Ingrese el número de la ciudad: "))
    return opcion

# Función para ingresar los datos de clima de una ciudad seleccionada
def ingresar_datos_clima(ciudad):
    print(f"\nIngresando datos para {ciudad}")
    temperaturas = []  # Lista para almacenar las temperaturas diarias
    print("Ingrese las temperaturas para los días de la semana:")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        temperatura = float(input(f"Temperatura del {dia}: "))  # Pedir temperatura diaria
        temperaturas.append(temperatura)  # Agregar temperatura a la lista
    return temperaturas  # Devolver las temperaturas ingresadas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    total_temperaturas = sum(temperaturas)  # Sumar todas las temperaturas
    return total_temperaturas / len(temperaturas)  # Calcular el promedio

# Función principal del programa
def main():
    # Lista de nombres de ciudades
    ciudades = ["Guayaquil", "Quito", "Cuenca", "Tena"]

    # Mostrar menú y seleccionar ciudad
    opcion = mostrar_menu()
    if opcion < 1 or opcion > 4:
        print("Opción no válida")
        return

    ciudad_seleccionada = ciudades[opcion - 1]  # Obtener el nombre de la ciudad seleccionada
    temperaturas = ingresar_datos_clima(ciudad_seleccionada)  # Ingresar datos para la ciudad seleccionada

    # Calcular y mostrar promedio semanal
    promedio_semanal = calcular_promedio_semanal(temperaturas)  # Calcular promedio
    print(f"\nPromedio semanal de temperaturas en {ciudad_seleccionada}: {promedio_semanal:.2f}°C")

# Inicializa el programa
main()