import pytest, string


class BuscadorDeCiudades():

    CIUDADES = [
        "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver",
        "Amsterdam", "Vienna", "Sydney", "New York City", "London", "Bangkok",
        "Hong Kong", "Dubai", "Rome", "Istanbul"
    ]

    def buscar(self, texto_buscar)-> str:
        if texto_buscar == "*":
            return self.CIUDADES
        elif len(texto_buscar) < 2:
            return None
        else:
            resultado = []
            for ciudad in self.CIUDADES:
                ciudad_minuscula = ciudad.lower()
                texto_minuscula = texto_buscar.lower()
                if ciudad_minuscula.find(texto_minuscula) != -1:
                    resultado.append(ciudad)
            return resultado


def test_01():
    buscador = BuscadorDeCiudades()
    response = buscador.buscar(texto_buscar = "p")
    assert  response == None


def test_02():
    buscador = BuscadorDeCiudades()
    response = buscador.buscar(texto_buscar = "Ist")
    assert  response == ["Istanbul"]

def test_03():
    buscador = BuscadorDeCiudades()
    response = buscador.buscar(texto_buscar = "Va")
    assert  response == ["Valencia","Vancouver"]

def test_04():
    buscador = BuscadorDeCiudades()
    response = buscador.buscar(texto_buscar = "Van")
    assert  response == ["Vancouver"]

def test_05():
    buscador = BuscadorDeCiudades()
    response = buscador.buscar(texto_buscar = "van")
    assert  response == ["Vancouver"]

def test_06():
    buscador = BuscadorDeCiudades()
    response = buscador.buscar(texto_buscar = "ape")
    assert  response == ["Budapest"]

def test_07():
    buscador = BuscadorDeCiudades()
    response = buscador.buscar(texto_buscar = "*")
    assert  response == BuscadorDeCiudades.CIUDADES