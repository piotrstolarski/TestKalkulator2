def kwadrat(x):
    return x * x

def suma_listy(liczby):
    return sum(liczby)

def srednia(liczby):
    if not liczby:
        return 0
    return sum(liczby) / len(liczby)

if __name__ == "__main__":
    print(kwadrat(5))          # 25
    print(suma_listy([1, 2]))  # 3
    print(srednia([2, 4, 6]))  # 4
