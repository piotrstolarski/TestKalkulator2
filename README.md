# Kalkulator – projekt do nauki Git ![tests](https://img.shields.io/badge/tests-pytest-blue)

Ten projekt zawiera proste przykładowe pliki `kalkulator*.py` oraz testy w `tests/`,
przydatne podczas nauki pracy z Git i GitHub.

## Struktura projektu

```
kalkulator1.py
kalkulator2.py
kalkulator3.py
README.md
.gitignore
LICENSE
tests/
  ├─ test_kalkulator1.py
  ├─ test_kalkulator2.py
  └─ test_kalkulator3.py
```

## Jak uruchomić skrypty

Uruchom dowolny z kalkulatorów w terminalu:

```bash
python kalkulator1.py
python kalkulator2.py
python kalkulator3.py
```

> W `kalkulator2.py` program odczytuje dane z klawiatury.

## Jak uruchomić testy (pytest)

1. (Opcjonalnie) utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```
2. Zainstaluj pytest:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install pytest
   ```
3. Uruchom testy:
   ```bash
   pytest -q
   ```

## Przydatne komendy Git

```bash
git status
git add .
git commit -m "Opis zmian"
git push -u origin main
```

## Licencja

Projekt na licencji MIT – patrz plik `LICENSE`.
