import pytest
import string
import re
class Calculadora:

    #TODO a futuro continuar el resto del ejercicio a partir del punto 6, una vez finalizado el ejercicio de dados

    INPUT_INVALIDO = "No se puede poner un separador despues de otro separados"
    SIN_COMA_AL_FINAL = "no puede haber coma al final del input"

    def __init__(self, numeros):
        self.numeros = numeros
        self.delimitador = ","  

    def procesar_entrada(self):
        if self.numeros.startswith("//"):
            match = re.match(r"//(.+)\n(.*)", self.numeros)
            if match:
                self.delimitador = match.group(1)  
                self.numeros = match.group(2)  

        regex_delimitador = re.escape(self.delimitador)  # Escapa caracteres especiales
        self.numeros_lista = re.split(f"{regex_delimitador}|\n", self.numeros)

    def validar_entrada(self):
        for i, caracter in enumerate(self.numeros):
            if caracter in [",", "\n"] and self.delimitador not in [",", "\n"]:
                raise ValueError(f"'{self.delimitador}' expected but '{caracter}' found at position {i}.")

    def sumar(self):
        if self.numeros == "":
            return 0

        self.procesar_entrada()  # Extraer delimitador y lista de números
        self.validar_entrada()  # Validar si hay errores de formato

        # Convertir lista de strings a enteros y sumarlos
        numeros_enteros = list(map(int, filter(None, self.numeros_lista)))
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

def test_procesando_numeros_con_salto_de_linea():
    calculadora = Calculadora(
        numeros="1,2\n3"
    )
    assert calculadora.sumar() == 6

def test_input_invalido():
   calculadora = Calculadora(
       numeros = "2,\n3"
   )
   assert calculadora.numeros != calculadora.INPUT_INVALIDO

#def test_sin_coma_al_final():
#    calculadora = Calculadora(
#        numeros = "1,2,"
#    )
#    with pytest.raises(ValueError, match=Calculadora.SIN_COMA_AL_FINAL):
#        calculadora.sumar()

def test_suma_con_delimitador_personalizado():
    calc = Calculadora("//;\n1;3")
    assert calc.sumar() == 4

def test_suma_con_otro_delimitador():
    calc = Calculadora("//|\n1|2|3")
    assert calc.sumar() == 6

def test_suma_con_delimitador_mas_largo():
    calc = Calculadora("//sep\n2sep5")
    assert calc.sumar() == 7

def test_error_si_hay_delimitador_incorrecto():
    calc = Calculadora("//|\n1|2,3")
    with pytest.raises(ValueError, match="'\\|' expected but ',' found at position 3."):
        calc.sumar()