from program.klasa import Human

czlowiek1 = Human("Adam", 25, 'm')
czlowiek1.imie = 'Adam'
czlowiek1.wiek = 25
czlowiek1.plec = 'm'

czlowiek1.witaj()
czlowiek1.spacer()
czlowiek1.policz(5,5)

czlowiek2 = Human()
czlowiek2.imie = 'Ewa'
czlowiek2.wiek = 18
czlowiek2.plec = 'k'

czlowiek2.witaj()
czlowiek2.spacer()
czlowiek2.policz(15,65)

czlowiek3 = Human()
czlowiek3.imie = 'Ala'
czlowiek3.wiek = 2
czlowiek3.plec = 'k'

czlowiek3.witaj()
czlowiek3.spacer()
czlowiek3.policz(5,5)