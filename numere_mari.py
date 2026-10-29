"""
Cerința 2 – Adunarea și înmulțirea a două numere naturale de cel mult 200 de cifre.

Numerele sunt păstrate ca liste de cifre (cifra unităților pe poziția 0).
Numărul întreg NU este convertit niciodată la int; se lucrează cifră cu cifră.
"""

import os

NUME_FISIER = "numere.txt"
MAX_CIFRE = 200


# ---------- Conversii șir <-> listă de cifre ----------

def sir_in_cifre(sir):
    """'1234' -> [4, 3, 2, 1] (ordine inversă: unitățile primele)."""
    return [ord(c) - ord("0") for c in reversed(sir)]


def elimina_zerouri(cifre):
    """Elimină zerourile nesemnificative (de la final, adică din fața numărului)."""
    cifre = list(cifre)
    while len(cifre) > 1 and cifre[-1] == 0:
        cifre.pop()
    return cifre


def cifre_in_sir(cifre):
    """[4, 3, 2, 1] -> '1234'."""
    return "".join(chr(d + ord("0")) for d in reversed(elimina_zerouri(cifre)))


# ---------- Citire și validare ----------

def valideaza_numar(text, nr_linie):
    """Verifică dacă textul este un număr natural valid; returnează șirul normalizat."""
    if text == "":
        raise ValueError(f"linia {nr_linie} este goală")
    if not all("0" <= c <= "9" for c in text):
        raise ValueError(f"linia {nr_linie} conține caractere care nu sunt cifre: '{text}'")
    normalizat = text.lstrip("0") or "0"
    if len(normalizat) > MAX_CIFRE:
        raise ValueError(f"numărul de pe linia {nr_linie} are {len(normalizat)} cifre (maxim {MAX_CIFRE})")
    return normalizat


def citeste_numere(nume_fisier=NUME_FISIER):
    """Citește cele două numere din fișier (câte unul pe linie)."""
    if not os.path.isfile(nume_fisier):
        raise FileNotFoundError(f"fișierul '{nume_fisier}' nu există")
    with open(nume_fisier, "r", encoding="utf-8") as f:
        linii = [linie.strip() for linie in f if linie.strip() != ""]
    if len(linii) != 2:
        raise ValueError(f"fișierul trebuie să conțină exact 2 numere, câte unul pe linie (găsite: {len(linii)})")
    return valideaza_numar(linii[0], 1), valideaza_numar(linii[1], 2)


# ---------- Operații ----------

def aduna(a, b):
    """Adunare cifră cu cifră, de la dreapta la stânga, cu transport."""
    rezultat, transport = [], 0
    for i in range(max(len(a), len(b))):
        s = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) + transport
        rezultat.append(s % 10)
        transport = s // 10
    if transport:                      # transportul final
        rezultat.append(transport)
    return elimina_zerouri(rezultat)


def inmulteste_cu_cifra(a, cifra):
    """Produs parțial: număr (listă de cifre) × o singură cifră, cu transport."""
    rezultat, transport = [], 0
    for d in a:
        p = d * cifra + transport
        rezultat.append(p % 10)
        transport = p // 10
    if transport:
        rezultat.append(transport)
    return elimina_zerouri(rezultat)


def inmulteste(a, b):
    """
    Înmulțire în coloană: pentru fiecare cifră a lui b se calculează un produs
    parțial, deplasat cu i poziții (i zerouri la dreapta), apoi se adună.
    Returnează (produs, lista_produselor_partiale).
    """
    produs, partiale = [0], []
    for i, cifra in enumerate(b):
        partial = [0] * i + inmulteste_cu_cifra(a, cifra)
        partiale.append(elimina_zerouri(partial))
        produs = aduna(produs, partial)
    return elimina_zerouri(produs), partiale


# ---------- Afișare ----------

def cifre_text(numar):
    """'1 cifră' / '5 cifre' – acord corect în limba română."""
    n = len(numar)
    return "1 cifră" if n == 1 else f"{n} cifre"


def afiseaza_adunare(sa, sb, suma):
    """Afișează adunarea aliniată la dreapta, ca la calculul în coloană."""
    latime = max(len(sa), len(sb), len(suma)) + 2
    print(sa.rjust(latime))
    print("+" + sb.rjust(latime - 1))
    print("-" * latime)
    print(suma.rjust(latime))


def afiseaza_inmultire(sa, sb, a, b, produs):
    """
    Afișează înmulțirea în coloană: fiecare produs parțial (a × cifra lui b)
    este deplasat cu câte o poziție spre stânga, apoi se face suma lor.
    """
    latime = max(len(sa), len(sb), len(produs)) + 2
    print(sa.rjust(latime))
    print("x" + sb.rjust(latime - 1))
    print("-" * latime)
    for i, cifra in enumerate(b):
        partial = cifre_in_sir(inmulteste_cu_cifra(a, cifra))
        semn = "+" if i == len(b) - 1 and len(b) > 1 else " "
        print(semn + (partial + " " * i).rjust(latime - 1))
    if len(b) > 1:
        print("-" * latime)
        print(produs.rjust(latime))


def main():
    try:
        sa, sb = citeste_numere()
    except (FileNotFoundError, ValueError) as eroare:
        print(f"Eroare: {eroare}.")
        return

    a, b = sir_in_cifre(sa), sir_in_cifre(sb)
    suma = cifre_in_sir(aduna(a, b))
    produs = cifre_in_sir(inmulteste(a, b)[0])

    print(f"Primul număr ({cifre_text(sa)}):    {sa}")
    print(f"Al doilea număr ({cifre_text(sb)}): {sb}")

    # Calculul în coloană se afișează doar dacă încape pe ecran
    if len(sb) <= 10 and len(sa) + len(sb) <= 60:
        print("\n=== Adunare ===")
        afiseaza_adunare(sa, sb, suma)
        print("\n=== Înmulțire ===")
        afiseaza_inmultire(sa, sb, a, b, produs)

    print("\n=== Rezultate ===")
    print(f"Suma     ({cifre_text(suma)}): {suma}")
    print(f"Produsul ({cifre_text(produs)}): {produs}")


if __name__ == "__main__":
    main()
