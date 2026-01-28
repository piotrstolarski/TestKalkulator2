import kalkulator3 as k

def test_kwadrat():
    assert k.kwadrat(5) == 25

def test_suma_listy():
    assert k.suma_listy([1, 2, 3]) == 6

def test_srednia():
    assert k.srednia([2, 4, 6]) == 4
    assert k.srednia([]) == 0
