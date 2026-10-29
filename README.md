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

_În lucru pe branch-ul `feature/big-numbers`._
