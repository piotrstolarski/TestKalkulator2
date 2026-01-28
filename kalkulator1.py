def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def mnoz(a, b):
    return a * b

def dziel(a, b):
    if b == 0:
        return "Błąd: dzielenie przez zero!"
    return a / b

if __name__ == "__main__":
    print(dodaj(2, 3))
    print(odejmij(10, 4))
    print(mnoz(3, 7))
    print(dziel(8, 2))
