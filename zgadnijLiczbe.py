import random

losowaLiczba = random.randint(1, 100)

def main():
    print("Zgadnij liczbe od 1 do 100")
    while True:
        podanaLiczba = int(input("Wpisz liczbe: "))
        if podanaLiczba > losowaLiczba:
            print('Podana liczba jest za duża')
            continue
        elif podanaLiczba < losowaLiczba:
            print("Podana liczba jest za mała")
            continue
        else:
            print("Brawo udało ci się zgadnąć!")
            break
main()

