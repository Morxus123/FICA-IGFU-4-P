# Wgranie FICA–IGF-U v4.1 na GitHub bez terminala

Repozytorium docelowe:
`Morxus123/FICA-IGFU-4-P`

## Najprostsza metoda

1. Otwórz repozytorium na GitHubie.
2. Wejdź do `main`.
3. Kliknij **Add file → Upload files**.
4. Z paczki wybierz wszystkie pliki i katalogi znajdujące się bezpośrednio w tym katalogu.
5. Jeżeli GitHub zapyta o zastąpienie `main.py`, potwierdź.
6. Na dole wybierz **Commit changes** do `main`.
7. Po commicie poczekaj na GitHub Actions.
8. Render powinien wykryć nowy commit i wykonać deployment.

## Kontrola po wdrożeniu

Otwórz:

`https://fica-igfu-4-1.onrender.com/api/final`

Musi być:

`"version":"4.1.0"`

Następnie:

`/api/science/engines`

powinien zwrócić listę wykonywalnych silników dziedzinowych.

## Uwaga

Nie wgrywaj pliku ZIP jako jednego pliku do repozytorium. Wgraj jego zawartość, zachowując strukturę katalogów, szczególnie:

```text
.github/workflows/ci.yml
tests/
main.py
Dockerfile
render.yaml
requirements.txt
```
