class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        print(f"{self.nombre} recibe {cantidad} de daño. Vida: {self.vida}")


class Guerrero(Personaje):  # Hereda de Personaje
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca con espada")
        enemigo.recibir_daño(self.fuerza)


# Uso
guts = Guerrero("Guts", 100, 20)
enemigo = Personaje("Enemigo genérico", 50)

guts.atacar(enemigo)
