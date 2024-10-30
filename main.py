import os

sciezka_skryptu = os.path.abspath(__file__)
sciezka_bez_pliku = os.path.dirname(sciezka_skryptu)
print(sciezka_bez_pliku)
sciezka_z_plikiem_txt = sciezka_bez_pliku + '\\tekst.txt'
print(sciezka_z_plikiem_txt)
plik = open(sciezka_z_plikiem_txt, "r")
tekst = plik.read()
print(tekst)
plik.close()

#liczenie ilosci wystapienia litery w calym pliku
def policz(txt, znak):
    licznik = 0
    for z in txt:
        # print(z) #print pokazuje nam, że tekst pobrany z pliku jest stringiem i można po nim iterować pojedyncze litery
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


