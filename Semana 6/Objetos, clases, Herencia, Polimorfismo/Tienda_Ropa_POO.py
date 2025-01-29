# Clase Principal para las prendas en venta
class Prenda:
    # Constructor que inicializa los atributos nombre, precio y cantidad de la prenda
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre  # Atributo privado que almacena el nombre de la prenda
        self.__precio = precio  # Atributo privado que almacena el precio de la prenda
        self.__cantidad = cantidad  # Atributo privado que almacena la cantidad de prendas

    # Método para obtener la información completa de la prenda (nombre, precio y cantidad)
    def obtener_info(self):
        return f'Prenda: {self.__nombre}, Precio unitario: {self.__precio}, Cantidad: {self.__cantidad}'

    # Método para obtener únicamente el nombre de la prenda
    def obtener_nombre(self):
        return self.__nombre

    # Método para obtener únicamente el precio unitario de la prenda
    def obtener_precio(self):
        return self.__precio

    # Método para obtener la cantidad de prendas
    def obtener_cantidad(self):
        return self.__cantidad

    # Método para obtener el precio total en función de la cantidad
    def calcular_precio_total(self):
        return self.__precio * self.__cantidad


# Clase Hija que hereda los atributos de la Clase Padre "Prenda"
class PrendaConDescuento(Prenda):
    # Constructor que inicializa los atributos nombre, precio, descuento y cantidad
    def __init__(self, nombre, precio, descuento, cantidad=1):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase Padre "Prenda"
        self.__descuento = descuento  # Atributo privado que almacena el porcentaje de descuento

    # Sobrescritura del método obtener_info para incluir información del precio con descuento
    def obtener_info(self):
        # Cálculo del precio con descuento por unidad
        precio_con_descuento = self.obtener_precio() * (1 - self.__descuento)
        # Precio total considerando la cantidad
        precio_total_con_descuento = precio_con_descuento * self.obtener_cantidad()
        # Retorna una cadena con el nombre, el precio original, el precio con descuento y el total
        return (f'Prenda: {self.obtener_nombre()}, Precio unitario original: {self.obtener_precio()}, '
                f'Precio unitario con descuento: {precio_con_descuento:.2f}, Cantidad: {self.obtener_cantidad()}, '
                f'Total: {precio_total_con_descuento:.2f}')

    # Método para calcular el precio total con descuento en función de la cantidad
    def calcular_precio_total(self):
        return self.obtener_precio() * (1 - self.__descuento) * self.obtener_cantidad()

# Función para mostrar todas las prendas en una lista
def mostrar_prendas(prendas):
    print("***************** Total de Prendas *****************")  # Encabezado
    # Itera sobre cada prenda en la lista y muestra su información
    for prenda in prendas:
        print(prenda.obtener_info())

# Función para calcular el precio total de las prendas en una lista
def calcular_precio_total(prendas):
    # Suma los precios totales de todas las prendas usando comprensión de listas
    total = sum(prenda.calcular_precio_total() for prenda in prendas)
    # Imprime el precio total de las prendas
    print(f'\nPrecio total de la Compra: {total:.2f}')


# Creación de instancias de la clase Prenda con cantidad
prenda1 = Prenda("Camisa", 16, 3)
prenda2 = Prenda("Pantalón", 38, 2)
prenda_descuento = PrendaConDescuento("Zapatos", 55, 0.30, 2)

# Crear una lista que almacena todas las prendas
prendas = [prenda1, prenda2, prenda_descuento]

# Muestra las prendas y sus detalles
mostrar_prendas(prendas)

# Calcula y muestra el precio total de las prendas compradas.
calcular_precio_total(prendas)