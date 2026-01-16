# Behave BDD Feladat - Alapszerkezet

Ez a mappa tartalmazza a Behave BDD feladat alapszerkezetét, amit ki kell egészítened.

## Kezdés

1. Olvasd el a **FELADATLEIRAS.md** fájlt részletesen!
2. **Először** implementáld a `src/number_checker.py` fájlban a `check_number` függvényt
3. Töltsd ki a `features/even.feature` fájlt scenariókkal
4. Implementáld a step-eket a `features/steps/even_steps.py` fájlban (használd a `check_number` függvényt!)
5. Futtasd le a teszteket: `python -m behave`

## Projekt struktúra

```
feladat/
├── src/
│   └── number_checker.py    # Tesztelendő kód (IDE kell implementálnod)
├── features/
│   ├── even.feature          # Scenariók (IDE kell írnod)
│   └── steps/
│       └── even_steps.py     # Step definitions (IDE kell implementálnod)
└── FELADATLEIRAS.md          # Részletes feladatleírás
```

## Segítség

Ha elakadtál, nézd meg a példa megoldást a projekt gyökérkönyvtárában!
