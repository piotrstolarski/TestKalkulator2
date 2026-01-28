import kalkulator1 as k

def test_dodaj():
    assert k.dodaj(2, 3) == 5

def test_odejmij():
    assert k.odejmij(10, 4) == 6

def test_mnoz():
    assert k.mnoz(3, 7) == 21

def test_dziel():
    assert k.dziel(8, 2) == 4
    assert k.dziel(5, 0) == "Błąd: dzielenie przez zero!"
