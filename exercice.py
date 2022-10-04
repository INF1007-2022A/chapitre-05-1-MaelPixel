#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number<0:
        absnb=number/-1
    else:
        absnb=number
    return absnb


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste=[]
    for c in prefixes:
        liste.append((c)+suffixe)

    return [liste]


def prime_integer_summation() -> int:
    number=0
    for nb in range(101):
            number+=nb
    return number


def factorial(number: int) -> int:
    nb=1
    while number>1:
        nb*=(number*(number-1))
        number-=2
    return nb


def use_continue() -> None:
    k=[]
    for c in range(1,11):
        if c==5:
            pass
        else:
            k.append(c)
    print(k)



def verify_ages(groups: List[List[int]]) -> List[bool]:
   liste=[]
   taille=0
    for c in groups:
        taille=len(c)
        if taille> 10 or taille <= 3:
           liste = liste
        for x in c:
            if x==25:
                liste.append(c)
                break
            if x<18:
                break
            if x>70 or x==50:
                continue
                if x>70 or x==50:
                    break
                else:
                    liste.append(c)


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
