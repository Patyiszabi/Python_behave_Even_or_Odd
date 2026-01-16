# Behave BDD Feladat - Páros szám ellenőrzése

## Feladat célja

A feladat célja, hogy megismerkedj a Python Behave BDD frameworkkel egy egyszerű, de tanulságos példán keresztül. Egy olyan tesztet fogsz írni, amely ellenőrzi, hogy egy szám páros vagy páratlan.

## Előfeltételek

- Python telepítve van a gépeden
- Behave telepítve van (vagy telepítsd: `pip install behave`)

## Projekt struktúra

A projekt a következő struktúrát követi:

```
feladat/
├── src/
│   └── number_checker.py    # IDE kell implementálnod a check_number függvényt
├── features/
│   ├── even.feature          # IDE kell írnod a scenariókat
│   └── steps/
│       └── even_steps.py     # IDE kell implementálnod a step-eket
└── FELADATLEIRAS.md          # Ez a fájl
```

> **Fontos**: A tesztelendő kód (a páros/páratlan ellenőrző logika) a `src/number_checker.py` fájlban van, NEM a step definitions-ben! Ez a helyes gyakorlat: a logika külön van a tesztektől.

## Feladat lépései

### 0. lépés: Tesztelendő kód implementálása

**Először** implementáld a `src/number_checker.py` fájlban a `check_number` függvényt:

- A függvény egy számot kap paraméterként (int)
- Visszaadja `"even"`-t, ha a szám páros
- Visszaadja `"odd"`-ot, ha a szám páratlan
- Használd a modulo operátort (`%`) az ellenőrzéshez

> 💡 **Tipp**: `number % 2 == 0` → páros, egyébként páratlan

### 1. lépés: Feature fájl elkészítése

A `features/even.feature` fájlban írd meg a következő scenariókat:

1. **Páros szám ellenőrzése**
   - Given: a szám 4
   - When: ellenőrzöm a számot
   - Then: az eredmény "even" (páros)

2. **Páratlan szám ellenőrzése**
   - Given: a szám 5
   - When: ellenőrzöm a számot
   - Then: az eredmény "odd" (páratlan)

3. **Nulla ellenőrzése**
   - Given: a szám 0
   - When: ellenőrzöm a számot
   - Then: az eredmény "even" (páros)

> 💡 **Tipp**: Nézd meg a példa projektet (`../features/even.feature`) a helyes szintaxisért!

### 2. lépés: Step definitions implementálása

A `features/steps/even_steps.py` fájlban implementáld a következő step-eket:

1. **Given step**: `the number is {number}`
   - Mentsd el a számot a `context.number`-be (konvertáld int-re!)

2. **When step**: `I check the number`
   - **Használd a `check_number` függvényt** a `src/number_checker.py` fájlból!
   - Hívd meg: `check_number(context.number)`
   - Mentsd el az eredményt a `context.result`-ba

3. **Then step**: `the result should be "{expected}"`
   - Hasonlítsd össze a `context.result`-ot az `expected` értékkel
   - Használj `assert`-et az ellenőrzéshez

> 💡 **Tipp**: Ne felejtsd el importálni a `check_number` függvényt: `from src.number_checker import check_number`
> 💡 **Tipp**: Nézd meg a példa projektet (`../features/steps/even_steps.py`) a megoldáshoz!

### 3. lépés: Tesztelés

Futtasd le a teszteket:

```bash
python -m behave
```

Vagy ha a behave parancs elérhető:

```bash
behave
```

## Várt eredmény

Ha mindent jól csináltál, a következő kimenetet kell látnod:

```
1 feature passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
9 steps passed, 0 failed, 0 skipped
```

## Kiegészítő feladatok (opcionális)

Ha kész vagy az alap feladattal, próbáld ki:

1. **Negatív számok**: Adj hozzá scenariókat negatív számokra (-4, -5)
2. **Nagy számok**: Teszteld nagy számokkal (1000, 1001)
3. **Hibakeresés**: Szándékosan rontsd el az expected értéket és nézd meg, milyen hibaüzenetet kapsz

## Segítség

Ha elakadtál:

- Nézd meg a példa projektet a projekt gyökérkönyvtárában
- A Behave dokumentáció: https://behave.readthedocs.io/
- Kérj segítséget a tanártól!

## Értékelés

A feladat akkor teljesített, ha:
- ✅ A `check_number` függvény helyesen van implementálva a `src/number_checker.py`-ban
- ✅ Mind a 3 scenario lefut hibamentesen
- ✅ A step definitions helyesen vannak implementálva és használják a `check_number` függvényt
- ✅ A kód tiszta és jól olvasható

Sok sikert! 🚀
