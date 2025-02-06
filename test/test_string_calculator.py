import pytest
import string

class Calculadora:

    def __init__(self, numeros):
        self.numeros = numeros 
    
    def sumar(self):
        
        if self.numeros == "":
            return 0
        
        
        numeros_enteros = list(map(int, filter(None, self.numeros.split(","))))

        return sum(numeros_enteros)  

        

def test_prueba_cadena_vacia():
    calculadora = Calculadora(numeros="")
    assert calculadora.sumar() == 0  
    

def test_prueba_un_solo_numero():
    calculadora = Calculadora(numeros="1")
    assert calculadora.sumar() == 1  
    

def test_prueba_cadena_con_coma():
    calculadora = Calculadora(numeros="1,2")
    assert calculadora.sumar() == 3  

def test_multiples_cadenas_con_coma():
    calculadora = Calculadora(numeros="1,2,3")
    assert calculadora.sumar() == 6  

