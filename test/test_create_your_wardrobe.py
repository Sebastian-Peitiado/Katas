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
    def __init__(self,placas_disponibles: list,tamaño_maximo: int, precios: dict):
        self.placas_disponibles = placas_disponibles
        self.tamaño_maximo = tamaño_maximo
        self.precios = precios



    def armado(self):
        resultado = []
        plaquetas_introducidas = []
        if self.placas_disponibles == self.tamaño_maximo:
            plaquetas_introducidas.append(self.placas_disponibles)
        
    
    
        



def test_creacion_de_armario():
    armario = Armario(placas_disponibles=[50,75,100,120],tamaño_maximo=250)
    assert armario != None

def test_armado_de_armario():
    armario = Armario(placas_disponibles=[50,75,100,120],tamaño_maximo=250,precios={50: 59, 75: 62, 100: 90, 120: 111})
    armario.armado()
    assert armario.armado() == [[75,75,100], 214]
    

    
