from dice import Dice

class Player:
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion
    
    
    
    def roll_dice(self, dice):
        roll1 = dice.roll()
        roll2 = dice.roll()
        total = roll1 + roll2
        print(f"{self.nombre} lanzo {roll1} y {roll2} y obtuvo {total}")
        return total