# Tecnica Abstraccion
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    # Métodos "públicos" que abstraen el funcionamiento interno
    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: {self.saldo} USD")


# Uso
cuenta = CuentaBancaria("Ana", 100)
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.mostrar_saldo()