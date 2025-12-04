class Mago(Personaje):
    def __init__(self, nombre, vida, poder_magico):
        super().__init__(nombre, vida)
        self.poder_magico = poder_magico

    def atacar(self, enemigo):
        print(f"{self.nombre} lanza un hechizo")
        enemigo.recibir_daño(self.poder_magico)


def turno_de_ataque(atacante, defensor):
    # Polimorfismo: no importa si es Guerrero o Mago,
    # ambos tienen el método atacar(...)
    atacante.atacar(defensor)


# Uso polimórfico
guerrero = Guerrero("Guts", 100, 18)
mago = Mago("Vanessa", 80, 25)
ogro = Personaje("Ogro", 120)

turno_de_ataque(guerrero, ogro)
turno_de_ataque(mago, ogro)
