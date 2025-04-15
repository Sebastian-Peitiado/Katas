#1 el armado del armario no puede exceder los 250cm
#2 el armado del armario no puede ser menor que 250 cm
# las placas que se utilicen no pueden ser distintas a las medidas que ya estan pre determinadas
#3 tiene que calcular el precio por utilizar esas medidas
#4 tiene que mostrar todas las convinaciones mas baratas posibles 
#5 tiene que mostrar las convinaciones mas convenientes
#6 el programa debe tener las convinaciones de placas ya predeterminadas
#7 debe tener el valor de esas placas  "" ""
#8 y debe mostrar de manera decendente de la mas barata a la mas cara, lo mismo para las convinaciones de placas
#9 tiene que especificar que medidas utilizo para armarlo

class Armario():
    def __init__(self,placas_disponibles: list,tamaño_maximo: int):
        self.placas_disponibles = placas_disponibles
        self.tamaño_maximo = tamaño_maximo

    def armado(self):
        armario_terminado = {}
        for key in range(0,self.placas_disponibles[5],1):
            pass
        



def test_creacion_de_armario():
    armario = Armario(placas_disponibles=[50,75,100,120],tamaño_maximo=250)
    assert armario != None

def test_02():
    armario = Armario(placas_disponibles=[50,75,100,120],tamaño_maximo=250)
    opciones_de_armado = armario.armado()
    assert opciones_de_armado == [{75,75,100},204]
    
