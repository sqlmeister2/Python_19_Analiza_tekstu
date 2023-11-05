plik = open("tekst.txt", "r")
tekst = plik.read()
plik.close()

#liczenie ilosci wystapienia litery w calym pliku

def policz(txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik

print(tekst)
print(policz(tekst, "k"))
print(policz(tekst.lower(), "k"))
#print(policz(tekst, "K" or "k")) nie działa

#procentowy udział
for z in "abcdefghijklmnoprstowxyz": # iteruje po każdej literze, bo to jest traktowane jako lista
    ile = policz(tekst.lower(), z)
    procent = ile * 100 / len(tekst)
    print("{0} - {1} - {2}%".format(z.upper(), ile, round(procent, 2)))
