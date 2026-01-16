"""
Szám ellenőrző modul - páros/páratlan ellenőrzés

TODO: Implementáld a check_number függvényt!
"""


def check_number(number):
    """
    Ellenőrzi, hogy a szám páros vagy páratlan.
    
    Args:
        number (int): Az ellenőrizendő szám
        
    Returns:
        str: "even" ha páros, "odd" ha páratlan
    """
    if number == 0:
        return "zero"
    elif number % 2 == 0:
        return "even"
    elif number < 0:
        if number % 2 == 0:
            return "negative even"
        else:
            return "negative odd"
    else:
        return "odd"


