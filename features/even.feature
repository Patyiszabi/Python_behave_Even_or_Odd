Feature: Páros szám ellenőrzése

  # TODO: Írd ide a scenariókat!
  # 1. Páros szám ellenőrzése (pl. 4)
  # 2. Páratlan szám ellenőrzése (pl. 5)
  # 3. Nulla ellenőrzése (0)
  # 4. Negatív páros szám ellenőrzése (-4)
  # 5. Negatív páratlan szám ellenőrzése (-5)

  Scenario: Páros szám ellenőrzése
    Given the number is 4 
    When I check the number
    Then the result should be "even"

  Scenario: Páratlan szám ellenőrzése
    Given the number is 5
    When I check the number
    Then the result should be "odd"

  Scenario: Nulla ellenőrzése
    Given the number is 0
    When I check the number
    Then the result should be "zero"

    Scenario: Negatív páros szám ellenőrzése
      Given the number is -2
      When I check the number
      Then the result should be "negative even"
