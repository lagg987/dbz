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

goku = Peleador("goku", 1000 ,700 ,2000)
majinboo = Peleador("majinboo",800 ,500 ,2000)

goku.Atacar(majinboo)