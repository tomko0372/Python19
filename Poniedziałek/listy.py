# indeks=int(input('Podaj miejsce wstawienia:'))
# cyfra = input('Podaj ocenę z klasówki:')
import random

oceny = [5, 3, 5, 3, 4, 4, 2, 1, 4, 3, 3, 4]
print(len(oceny))
print(oceny[:5])
print("ilość 3 w ocenach", oceny.count(3))
print(oceny)
# oceny.insert(indeks, int(cyfra))
oceny.append(6)
oceny.remove(1)
oceny.pop()
oceny.sort()
oceny.reverse()
oceny[-1] = 7
print(oceny)
dziennik = tuple(oceny)
print(dziennik)
oceny = list(dziennik)
print(oceny)

oceny2 = oceny.copy()
oceny[-1] = 33
print("oceny2", oceny2)
print(oceny)
loteria = random.choice(oceny)
print("Wylosowana ocena:", loteria)

kostka6 = random.randint(1, 6)
print("Wynik rzutu kością",kostka6)
print(random.random())

losowe_wartosci = []
losowe_wartosci.append(int(random.random() * 1000))
losowe_wartosci.append(int(random.random() * 1000))
losowe_wartosci.append(int(random.random() * 1000))
losowe_wartosci.append(int(random.random() * 1000))
losowe_wartosci.append(int(random.random() * 1000))
losowe_wartosci.append(int(random.random() * 1000))
losowe_wartosci.append(int(random.random() * 1000))
print(losowe_wartosci)

