import kalkulator2 as k

def test_oblicz_plus():
    assert k.oblicz(2, 3, "+") == 5

def test_oblicz_dzielenie():
    assert k.oblicz(8, 2, "/") == 4
    assert k.oblicz(5, 0, "/") == "Błąd: dzielenie przez zero!"

def test_oblicz_nieznana():
    assert k.oblicz(1, 1, "%") == "Nieznana operacja."
