# Clase Padre para representar una Cuenta Bancaria
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Nombre del titular de la cuenta
        self.saldo = saldo  # Saldo inicial de la cuenta

    def datos_cliente(self):
        print("\n******************** Detalles de la Cuenta ********************")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo:.2f}")  # Imprime el saldo actual de la cuenta, formateado con dos decimales
        print("****************************************************************\n")

    def depositar(self, monto):  # Deposita un monto en la cuenta.
        self.saldo += monto
        print(
            f"${monto:.2f} depositados. Nuevo saldo: ${self.saldo:.2f}")  # Imprime el monto depositado y el nuevo saldo de la cuenta, ambos formateados con dos decimales

    def retirar(self, monto):  # Retira un monto de la cuenta si hay fondos suficientes.
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"${monto:.2f} retirados. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes para realizar el retiro")


# Clase para representar una cuenta de ahorros
class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)  # Hereda los atributos de la Clase Padre


# Función para transferir fondos entre dos cuentas
def transferencia(cuenta_origen, cuenta_destino,
                  monto):  # Transfiere fondos de una cuenta a otra si hay saldo suficiente en la cuenta origen.
    print("\n**************************** Procesando Transferencia ****************************")
    print(f"Cuenta de Origen: {cuenta_origen.titular}")
    print(f"Cuenta de Destino: {cuenta_destino.titular}")

    if cuenta_origen.saldo >= monto:
        cuenta_origen.retirar(monto)  # Realiza el retiro del monto desde la cuenta de origen
        cuenta_destino.depositar(monto)  # Deposita el monto en la cuenta de destino
        print(f"Transferencia exitosa: ${monto:.2f} transferidos de {cuenta_origen.titular} a {cuenta_destino.titular}")
    else:
        print("Transferencia fallida: Fondos insuficientes")

    print("**********************************************************************************\n")


# Creación de una cuenta de ahorros
cuenta_1 = CuentaAhorros("Gustavo Rodríguez", 1000)  # Inicializa con titular y saldo
cuenta_1.datos_cliente()  # Muestra los atributos de la cuenta
cuenta_1.depositar(500)  # Deposita $500
cuenta_1.retirar(300)  # Retira $300
cuenta_1.datos_cliente()  # Muestra el saldo actualizado

# Creación de otra cuenta de ahorros
cuenta_2 = CuentaAhorros("María Zambrano", 500)  # Inicializa con titular y saldo
cuenta_2.datos_cliente()  # Muestra los atributos de la cuenta
cuenta_2.depositar(200)  # Deposita $200
cuenta_2.retirar(800)  # Intenta retirar $800 (Fondos insuficientes)
cuenta_2.datos_cliente()  # Verifica el saldo actualizado

# Ejemplo de transferencia entre cuentas
transferencia(cuenta_1, cuenta_2, 400)  # Transfiere $400 de cuenta_1 a cuenta_2
cuenta_1.datos_cliente()  # Verifica el nuevo saldo de cuenta_1
cuenta_2.datos_cliente()  # Verifica el nuevo saldo de cuenta_2
