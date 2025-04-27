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
        if self.tamaño_maximo == 0:
            return [[]]
        lista_resultados = []
        pila = [[]]
        print(pila)
        while pila:
           combinacion_a_verificar = pila.pop()
           if combinacion_a_verificar == []:
            total = 0
           else:
               total = sum(combinacion_a_verificar)
           if total == self.tamaño_maximo:
               lista_resultados.append(combinacion_a_verificar)
           elif total < self.tamaño_maximo:
               for placas in self.placas_disponibles:
                   pila.append(combinacion_a_verificar.append(placas))

               
        #for x in range(len(self.placas_disponibles)):
        #    if self.placas_disponibles[x] == self.tamaño_maximo:
        #        return [[self.placas_disponibles[x]]]
        return lista_resultados
            

    
    
        



def test_esapcio_0_devuelve_lista_vacia():
    armario = Armario(placas_disponibles=[50],tamaño_maximo=0)
    resultado = armario.armado()
    assert resultado == [[]]

def test_sin_solucion_devuelve_lista_vacia():
    armario = Armario(placas_disponibles=[50],tamaño_maximo=25)
    resultado = armario.armado()
    assert resultado == [[]]
    
def test_un_solo_elemento_devuelve_una_lista():
    armario = Armario(placas_disponibles=[50],tamaño_maximo=50)
    resultado = armario.armado()
    assert resultado == [[50]]

def test_2_elementos_en_una_lista():
    armario = Armario(placas_disponibles=[50,75],tamaño_maximo=100)
    resultado = armario.armado()
    assert resultado == [[50,50]]