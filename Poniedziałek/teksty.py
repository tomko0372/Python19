imie = "Tomek"
wiek = "50"
print(type(imie))
print(type(wiek))
print("wynik możenia:", wiek * 2)  # tutaj jest błąd!
print("wynik łączenia:", imie + " " + wiek)
print(imie.upper())
print(imie.lower())
print(imie.title())
print(imie.count("M"))
print(imie.join('MGL'))
print(imie.rstrip())
print(imie[0:3])  # wycinanie tekstu - od:do
print(imie[-3:-1])  # wycinanie tekstu od końca - od:do
s = "Witaj świecie"
print(len(s))
print(s.removeprefix("Wi"))