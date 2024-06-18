"""
HRA BULLS AND COWS
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Vrbík
email: filip.vrbik@vzp.cz
discord: filip.vrbik
"""

from datetime import datetime # funkce na práci s časem
from random import sample # funkce pro gen. pseudonáhodných čísel


# Generování náhodných a unikátních čísel, na prvním místě nesmí být 0
def generuj_nahodna_cisla(interval = 10, poc_cisel = 4) -> list:  
    while True:
        nahodna_cisla = sample(range(interval),poc_cisel)
        if nahodna_cisla[0] != 0:
            return nahodna_cisla
        else:
            continue

# Kontrola, zda nejsou zadané hodnoty duplicitní
# tato funkce je vložena do fce kontrola_a_zadani_cisel
# vrací hodnotu True x False
def kontrola_duplicit(zadana_cisla_dupl)-> bool:
    kontrolni_set = set()
    kontrolni_list = list()
    for cislo in zadana_cisla_dupl:
        kontrolni_set.add(cislo)
        kontrolni_list.append(cislo)
    return len(kontrolni_list) == len(kontrolni_set)

# Zadání vstupních 4 čísel a kontrola jejich správnosti
def kontrola_a_zadani_cisel():
    global pocet_pokusu
    while True:
        zadana_cisla = input("Enter a four digit number: ")
        if len(zadana_cisla) == 4 and zadana_cisla.isdigit() and zadana_cisla[0] != "0" and kontrola_duplicit(zadana_cisla):
            pocet_pokusu += 1
            return (zadana_cisla)
        elif len(zadana_cisla) != 4:
            print ("The number must consist of four digits!")
        elif not zadana_cisla.isdigit():
            print ("The number must consist of digits!")
        elif zadana_cisla[0] == "0":
            print ("The number most not start with zero!")
        elif not kontrola_duplicit(zadana_cisla):
            print ("The number most consist of four unique digits!")  
        pocet_pokusu += 1

# Tato funkce pocita, kolik je bulls a cows
# Porovnává hodnoty z generuj_nahodna_cisla a kontrola_a_zadani_cisel
def pocitej_bulls_cows(nahodna_cisla_zadani:int, zadana_cisla_uzivatel:str): 

    poradi_cisel = (0,1,2,3)
    pocet_bulls = 0
    pocet_cows = 0
    for poradi in poradi_cisel:
        if str(nahodna_cisla_zadani[poradi]) == zadana_cisla_uzivatel[poradi]:
            pocet_bulls += 1
        elif zadana_cisla_uzivatel[poradi] in str(nahodna_cisla_zadani):
            pocet_cows += 1
    return pocet_bulls, pocet_cows

#Tato funkce pouze vypíše počet bulls
def vypis_pocet_bulls(pocet_bulls:int):

    if pocet_bulls == 0:
        print("0 bulls,", end=" ")
    elif pocet_bulls == 1:
        print("1 bull,", end=" ")
    elif pocet_bulls == 4:
        print("Correct, you've guessed the right number", end=" ")
    else:
        print(pocet_bulls, " bulls,", end=" ")

#Tato funkce pouze vypíše počet cows
def vypis_pocet_cows(pocet_bulls:int, pocet_cows:int):
    if pocet_bulls == 4:
        return
    elif pocet_cows == 0:
        print("0 cows")
    elif pocet_cows == 1:
        print("1 cow")
    else:
        print(pocet_cows, " cows")


print("Hi there!")
print(40*"-")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(40*"-")

# začátek měření času
cas_zacatek = datetime.now()

# První kolo vypsání a zadávání čísel
pocet_pokusu = 0
nahodna_cisla_zadani = generuj_nahodna_cisla(10,4)
print(nahodna_cisla_zadani)
zadana_cisla_uzivatel = kontrola_a_zadani_cisel()
pocet_bulls, pocet_cows = pocitej_bulls_cows(nahodna_cisla_zadani, zadana_cisla_uzivatel)
vypis_pocet_bulls(pocet_bulls)
vypis_pocet_cows(pocet_bulls, pocet_cows)


# Zde smyčka neustálého zadávání, dokud uživatel netrefí všechna 4 čísla
while pocet_bulls < 4:
    zadana_cisla_uzivatel = kontrola_a_zadani_cisel()
    pocet_bulls, pocet_cows = pocitej_bulls_cows(nahodna_cisla_zadani, zadana_cisla_uzivatel)
    vypis_pocet_bulls(pocet_bulls)
    vypis_pocet_cows(pocet_bulls, pocet_cows)

print (f"in {pocet_pokusu} guesses!")

# konec měření času
cas_konec = datetime.now()

# Výpočet uplynulého času
cas_saldo = cas_konec - cas_zacatek
print(f"Total time: {round(cas_saldo.total_seconds())} seconds.")
