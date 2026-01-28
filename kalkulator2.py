def oblicz(a, b, operacja):
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b if b != 0 else "Błąd: dzielenie przez zero!"
    else:
        return "Nieznana operacja."

if __name__ == "__main__":
    print("Prosty kalkulator")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    op = input("Wybierz operację (+ - * /): ")

    print("Wynik:", oblicz(a, b, op))
