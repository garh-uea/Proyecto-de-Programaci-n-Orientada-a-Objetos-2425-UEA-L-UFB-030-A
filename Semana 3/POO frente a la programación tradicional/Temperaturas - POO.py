# Clase Padre para representar datos generales del clima
class Clima:
    def __init__(self, ciudad, estacion, temperaturas):
        # Inicializa la clase con la ciudad, estación del año y las temperaturas semanales.
        self.__ciudad = ciudad  # Ciudad encapsulada (Nombre de la ciudad)
        self.__estacion = estacion  # Estación del año encapsulada (Invierno o Verano)
        self.__temperaturas = temperaturas  # Temperaturas semanales encapsuladas (Lista con las 5 temperaturas de la semana)

    def mostrar_datos(self):
        # Método para mostrar los datos generales de la ciudad y las temperaturas ingresadas.
        print("\n******************** Datos del Clima ********************")
        print(f"Ciudad: {self.__ciudad}")
        print(f"Estación: {self.__estacion}")
        print("Temperaturas de la semana: " + ", ".join(f"{temp}°" for temp in
                                                        self.__temperaturas))  # Muestra las temperaturas de la semana formateadas con el símbolo "°" y separadas por comas.
        print("*********************************************************\n")

    def get_temperaturas(self):
        # Método para acceder a las temperaturas desde clases derivadas.
        return self.__temperaturas

    def get_ciudad(self):
        # Método para acceder a la ciudad desde clases derivadas.
        return self.__ciudad


# Clase derivada para calcular y analizar datos del clima
class AnalisisClima(Clima):
    def __init__(self, ciudad, estacion, temperaturas):
        super().__init__(ciudad, estacion, temperaturas)  # Hereda los atributos de la clase padre

    def calcular_promedio(self):
        # Método para calcular el promedio semanal de temperaturas.
        temperaturas = self.get_temperaturas()
        promedio = sum(temperaturas) / len(temperaturas)
        ciudad = self.get_ciudad()
        print(f"El promedio semanal de temperaturas en {ciudad} es: {promedio:.2f}°C")
        return promedio

    def analizar_clima(self):
        # Método adicional para analizar los datos del clima, determinando días más cálidos y fríos.
        temperaturas = self.get_temperaturas()
        max_temp = max(temperaturas)
        min_temp = min(temperaturas)
        print(f"El día más cálido tuvo {max_temp}°C y el más frío tuvo {min_temp}°C.")


# Crear instancia de la clase derivada
clima_semanal = AnalisisClima("Tena", "Verano", temperaturas=[28, 30, 31, 29, 32])

# Mostrar datos, calcular promedio y realizar análisis
clima_semanal.mostrar_datos()
clima_semanal.calcular_promedio()
clima_semanal.analizar_clima()