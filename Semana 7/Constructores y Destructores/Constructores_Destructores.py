# Clase para gestionar la creación, apertura, escritura, cierre y eliminación de un archivo de base de datos.
class BaseDatos:

    def __init__(self, nombre_archivo):     # Constructor de la clase. Inicializa el nombre del archivo y lo abre en modo de escritura.
        self.nombre_archivo = nombre_archivo
        print(f"************ Inicializando el archivo {self.nombre_archivo} ************")
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' creado y abierto en modo escritura.\n")


    def escribir_datos(self, datos):    # Escribe datos en el archivo. Los datos deben ser una cadena de texto.
        self.archivo.write(datos + '\n')
        print(f"Datos escritos en el archivo: {datos}")


    def cerrar_archivo(self):  # Método privado para cerrar el archivo.
        self.archivo.close()
        print(f"\n************ Archivo '{self.nombre_archivo}' cerrado correctamente. ************")


    def __del__(self):  # Destructor de la clase. Se asegura de cerrar y eliminar el archivo si no ha sido cerrado aún.
        print(f"************ Destructor llamado para el archivo: {self.nombre_archivo} ************")
        self.cerrar_archivo()


# Crea una instancia de la clase para manejar un archivo llamado 'mi_base_de_datos.txt'
gestor_archivo = BaseDatos("mi_base_de_datos.txt")

# Escribe algunos datos en el archivo
gestor_archivo.escribir_datos("Nombres: Gustavo Rodríguez")
gestor_archivo.escribir_datos("Residencia: Tena")

# Elimina el archivo
gestor_archivo.cerrar_archivo()
