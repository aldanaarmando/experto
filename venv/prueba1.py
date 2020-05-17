from random import choice
from experta import *

class Light(Fact):
    pass


class semaforo(KnowledgeEngine):
    @Rule(Light(color='verde'))
    def green_light(self):
        print("Adelante")

    @Rule(Light(color='rojo'))
    def red_light(self):
        print("Alto")

    @Rule(AS.light << Light(color=L('amarillo') | L('amarillo_parpadeando')))
    def cautious(self, light):
        print("Tenga cuidado el semaforo esta en", light["color"])

engine = semaforo()
engine.reset()
color2=input()
engine.declare(Light(color=color2))
engine.run()