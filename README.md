# Laborator 4 – Conjectura lui Goldbach și numere mari

Proiect Python cu două aplicații independente, fiecare în fișierul ei.
Necesită doar Python 3.8+ (fără biblioteci externe).

## Cerința 1 – Conjectura lui Goldbach

Fișier: `goldbach.py`

Citește un număr natural par `n > 2` (valorile invalide sunt respinse cu un mesaj)
și afișează toate perechile de numere prime `(p, q)` cu `p + q = n` și `p ≤ q`.
Testul de primalitate este implementat manual (împărțiri până la √x).

```bash
python goldbach.py
```

Exemplu: pentru `n = 10` se afișează `10 = 3 + 7` și `10 = 5 + 5`.

## Organizare

- Fiecare cerință este dezvoltată pe un branch separat.
- Branch-urile sunt integrate în `main` prin Pull Request.
- Fiecare problemă se află într-un fișier distinct.

## Cerința 2 – Adunarea și înmulțirea numerelor mari

Fișier: `numere_mari.py`

Citește două numere naturale (maxim 200 de cifre fiecare) din `numere.txt`,
câte unul pe linie, și afișează suma și produsul. Numerele sunt reprezentate
ca liste de cifre – nu sunt convertite la `int` și nu se folosesc biblioteci
pentru numere mari.

- adunare cifră cu cifră, de la dreapta la stânga, cu transport;
- înmulțire în coloană, prin produse parțiale și transport;
- se verifică existența fișierului și validitatea datelor;
- se tratează valorile 0 și 1, transportul final și zerourile din față.

```bash
python numere_mari.py
```

Exemplu: pentru `999` și `2` → suma `1001`, produsul `1998`.
