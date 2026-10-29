"""Cerința 1 – Verificarea conjecturii lui Goldbach pentru un număr par n > 2."""


def este_prim(x):
    """Returnează True dacă x este număr prim (verificare prin împărțiri până la √x)."""
    if x < 2:
        return False
    if x < 4:          # 2 și 3 sunt prime
        return True
    if x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True


def citeste_numar_par():
    """Citește de la tastatură un număr natural par mai mare decât 2."""
    while True:
        text = input("Introduceți un număr natural par mai mare decât 2: ").strip()
        if not text.isdigit():
            print("  Valoare invalidă: introduceți un număr natural (doar cifre).")
            continue
        n = int(text)
        if n <= 2:
            print("  Numărul trebuie să fie mai mare decât 2.")
        elif n % 2 != 0:
            print(f"  {n} este impar. Introduceți un număr par.")
        else:
            return n


def descompuneri_goldbach(n):
    """Returnează lista perechilor (p, q) de numere prime cu p + q = n și p <= q."""
    perechi = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if este_prim(p) and este_prim(q):
            perechi.append((p, q))
    return perechi


def afiseaza_descompuneri(n, perechi):
    """Afișează descompunerile găsite într-un format lizibil."""
    if not perechi:
        print(f"\nNu s-a găsit nicio descompunere pentru {n} (contraexemplu la conjectură!).")
        return
    print(f"\n{n} poate fi scris ca sumă de două numere prime în {len(perechi)} moduri:")
    for p, q in perechi:
        print(f"  {n} = {p} + {q}")
    print(f"Pe scurt: {n} = " + " = ".join(f"{p}+{q}" for p, q in perechi))


def main():
    n = citeste_numar_par()
    afiseaza_descompuneri(n, descompuneri_goldbach(n))


if __name__ == "__main__":
    main()
