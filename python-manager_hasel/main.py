zbior_hasel = open("zbior_hasel.txt", 'a+')

def zakonczPrace():
    zbior_hasel.close()

def szukajHasla():
    print("Podaj nazwe platformy, do ktorej hasla szukasz.")
    word = input()
    with open("zbior_hasel.txt") as zbior_hasel:
        lines = zbior_hasel.readlines()
        for line in lines:
            if line.find(word) != -1:
                print("Wykryto slowo kluczowe" + " " + word + ".")
                print("Zawartosc wiersza: " + line)

def wypiszHasla():
    print("Oto lista twoich haseł:" + "\r")
    with open('zbior_hasel.txt') as f:
        for line in f:
            print(line.rstrip('\n'))



def dodajHaslo():
    print ("Napisz, na jakiej platformie posiadasz konto?")
    platforma = input()
    print("Napisz haslo do wymienionej wyzej platformy")
    haslo = input()
    zbior_hasel.writelines(platforma + ' ' + haslo +'\n')


while True:
    print("Napisz, jaka akcje zamierzasz podjac:")
    print("szukajHasla")
    print("wypiszHasla")
    print("dodajHaslo")
    print("zakonczPrace")
    wybor = input()
    if wybor == "szukajHasla":
        szukajHasla()
    elif wybor == "wypiszHasla":
        wypiszHasla()
    elif wybor == "dodajHaslo":
        dodajHaslo()
    elif wybor == "zakonczPrace":
        zakonczPrace()
        break
    else:
        print("Wybrano nieprawidlowe dzialanie. Sproboj ponownie.")
