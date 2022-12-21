#plik = open('klienci.txt', 'r')
#plik = open('klienci.txt', 'w')
plik = open('klienci.txt', 'a')


lista = ['Paweł W', 'Tomek', 'Radek']
name = 'Paweł W'
wiek = 35

plik.write(name + '\n')
plik.write(str(wiek) + '\n')
plik.write(str(lista) + '\n')

nowa_lista = []
zawartosc1 = plik.readline().rstrip('\n')
zawartosc2 = plik.readline().rstrip('\n')
zawartosc3 = plik.readline().rstrip('\n')

nowa_lista.append(zawartosc1)
nowa_lista.append(int(zawartosc2))
plik = open('klienci.txt', 'r')
# plik = open('klienci.txt', 'w')
# plik = open('klienci.txt', 'a')


# lista = ['Paweł W', 'Tomek', 'Radek']
# name = 'Paweł W'
# wiek = 35

# plik.write(name + '\n')
# plik.write(str(wiek) + '\n')
# plik.write(str(lista) + '\n')

nowa_lista = []

nowa_lista.append(plik.readline().rstrip('\n'))
nowa_lista.append(plik.readline().rstrip('\n'))
nowa_lista.append(plik.readline().rstrip('\n'))

plik.close()
print(nowa_lista)
