# lista = [4, 6, 8, 0]
#
# for i in lista:
#     print(i)
#     print(i * 2)
#
# print(i)

lista = [4, 6, 8, 0]
wyniki = []

for liczba in lista:
    wyniki.append(liczba * 2)

print(wyniki)

for i in range(10, 100, 10):
    print(i)

liczby = list(range(1, 11, 2))
print(liczby)

imiona = ['Tomek', 'Bartek', 'Ania']
for p in range(len(imiona)):
    print(p + 1, imiona[p])

for poz, imie in enumerate(imiona, 1):
    print(poz, imie)


for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
