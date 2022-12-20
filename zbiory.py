zbior = {1, 2, 3, 6, 7, 8}
oceny = [1, 3, 1, 3, 4, 4, 2, 1, 4, 3, 7, 3, 4, 9]
nowe_oceny = set(oceny)
print(nowe_oceny.intersection())
print(nowe_oceny.difference(zbior))
print(zbior.difference(nowe_oceny))
