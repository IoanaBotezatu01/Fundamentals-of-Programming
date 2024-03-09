def create_tranzactie(id, ziua, suma, tipul):
    return {"ziua": ziua, "suma": suma, "tipul": tipul}


def get_ziua(tranzactie):
    return tranzactie["ziua"]


def get_suma(tranzactie):
    return tranzactie["suma"]


def get_tipul(tranzactie):
    return tranzactie["tipul"]

def set_ziua(tranzactie, ziua):
    tranzactie["ziua"] = ziua


def set_suma(tranzactie, suma):
    tranzactie["suma"] = suma


def set_tipul(tranzactie, tipul):
    tranzactie["tipul"] = tipul


def afisare():
    print('''
    1.Introduceti datele tranzactiei
    2.Afisare date tranzactie
    3.Introduceti datele tranzactiei fara ziua pe care nu o doriti
    4.Afisare date tranzactie cu ziua stearsa
    5.Exit
    6.Introduceti datele tranzactiei fara tipul pe care nu il doriti
    7.Afisare date tranzactie cu tipul sters
    8.Introduceti datele tranzactiei fara perioada pe care nu o doriti
    9.Afisare date tranzactie cu perioada stearsa
    10.Modifica ultima tranzactia (Se afiseaza tot cu a doua optiune pentru ca modifica afisarea totala)
    ''')


def citire(tranzactii):
    ziua = input("Introdu ziua: ")
    suma = input("Introdu suma: ")
    tipul = int(input("Introdu tipul: "))
    adauga_tranzactii(tranzactii, id, ziua, suma, tipul)


def adauga_tranzactii(tranzactii, id, ziua, suma, tipul):
    tranzactii.append(create_tranzactie(id, ziua, suma, tipul))


def citire_StergereZIUA(tranzactii):
    id = input("Introdu id:")
    ziua = input("Introdu ziua: ")
    suma = input("Introdu suma: ")
    tipul = int(input("Introdu tipul: "))
    n = (input("Numarul zilei pe care vrei sa o elimini: "))
    if (ziua != n):
        adauga_tranzactii(id, tranzactii, ziua, suma, tipul)


def citire_StergereTIP(tranzactii):
    id = input("Introdu id:")
    ziua = input("Introdu ziua: ")
    suma = input("Introdu suma: ")
    tipul = (input("Introdu tipul: "))
    n = (input("Numarul tipului pe care vrei sa o elimini: "))
    if (tipul != n):
        adauga_tranzactii(id, tranzactii, ziua, suma, tipul)


def citire_StergerePERIOADA(tranzactii):
    id = input("Introdu id:")
    ziua = input("Introdu ziua: ")
    suma = input("Introdu suma: ")
    tipul = (input("Introdu tipul: "))
    n = (input("Ziua de inceput a perioadei:"))
    m = (input("Ziua de sfarsit a perioadei:"))
    if (ziua < n or ziua > m):
        adauga_tranzactii(tranzactii, id, ziua, suma, tipul)


def teste():
    assert create_tranzactie(1, 1, 1,2)
    assert create_tranzactie(1, 3, 2,2)
    assert create_tranzactie(2, 3, 2,2)
    assert create_tranzactie(2, 1, 1,2)


def menu():
    tranzactii = []
    val = True
    while val:
        afisare()
        optiune = input("Optiunea ta este:")
        if optiune == "1":
            citire(tranzactii)
        elif optiune == "2":
            for x in tranzactii:
                print(x)
        elif optiune == "3":
            citire_StergereZIUA(tranzactii)
        elif optiune == "4":
            for x in tranzactii:
                print(x)
        elif optiune == "5":
            val = False
        elif optiune == "6":
            citire_StergereTIP(tranzactii)
        elif optiune == "7":
            for x in tranzactii:
                print(x)
        elif optiune == "8":
            citire_StergerePERIOADA(tranzactii)
        elif optiune == "9":
            for x in tranzactii:
                print(x)
        elif optiune == "10":
            modifica_tranzactie(tranzactii)
        else:
            print("Comanda este gresita")


teste()
menu()