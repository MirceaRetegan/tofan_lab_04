# Laborator 4 – Conjectura lui Goldbach și numere mari

Proiect Python cu două aplicații independente, fiecare în fișierul ei.
Necesită doar Python 3.8+ (fără biblioteci externe).

## Cerința 1 – Conjectura lui Goldbach

_În lucru pe branch-ul `feature/goldbach`._

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
