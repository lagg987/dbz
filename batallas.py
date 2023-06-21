class Peleador:
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        print(f"El peleador {self.nombre} esta listo para la batalla!")

    def Atacar(self, enemigo):
        difdeatk = self.ataque - enemigo.defensa
        if difdeatk >= 0:
            enemigo.vida = enemigo.vida - difdeatk
            print(f"{enemigo.nombre} ah pedido {difdeatk} puntos vitales!")
        else:
            print(f"{enemigo.nombre} ah resistido el ataque sin daños!")

class Batalla:
    def __init__(self, luchador1, luchador2):
        self.luchador1 = luchador1
        self.luchador2 = luchador2
        turno = 1
        while self.luchador1.vida > 0 and self.luchador2.vida > 0:
            if turno == 1:
                self.luchador1.Atacar(self.luchador2)
                turno = 2
            else:
                self.luchador2.Atacar(self.luchador1)
                turno = 1
        if self.luchador1.vida <= 0:
            print(f"El luchador {self.luchador2.nombre} es el ganador!")
        else:
            print(f"El luchador {self.luchador1.nombre} es el ganador!")

goku = Peleador("goku", 1000 ,700 ,2000)
majinboo = Peleador("majinboo",800 ,500 ,2000)

pelea = Batalla(goku, majinboo)