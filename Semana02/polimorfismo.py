#Técnica de Polimorfismo
#Distintas clases implementan el mismo método con comportamientos diferentes, pero se usan de forma uniforme.
class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def recibir_daño(self, daño):
        self.vida -= daño
        print(f"{self.nombre} recibe {daño} de daño y le queda {self.vida} de vida.")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca con su espada.")
        enemigo.recibir_daño(self.fuerza)

class Mago(Personaje):
    def __init__(self, nombre, vida, poder_magico):
        super().__init__(nombre, vida)
        self.poder_magico = poder_magico

    def atacar(self, enemigo):
        print(f"{self.nombre} lanza un hechizo.")
        enemigo.recibir_daño(self.poder_magico)

def turno_de_ataque(atacante, defensor):
    # Polimorfismo: no importa si es Guerrero o Mago,
    # ambos tienen el método atacar(...)
    atacante.atacar(defensor)

# Uso polimórfico
guerrero = Guerrero("Guts", 100, 18)
mago = Mago("Kerly", 80, 25)
ogro = Personaje("Ogro", 120)

turno_de_ataque(guerrero, ogro)
turno_de_ataque(mago, ogro)
