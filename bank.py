from program.bankomat import Bankomat

start_bal = float(input('Podaj wysokość salda:'))
savings = Bankomat(start_bal)

pay = float(input('Podaj kwotę wpłaty:'))
print("Wpłacam środki...")
savings.despoit(pay)

cash = float(input("Podaj kwotę wypłaty:"))
print('Kwota zostanie odjęta od salda')
savings.pin(cash)

saldo = savings.get_balance()
print("Aktualne saldo rachunku wynosi", saldo)
def pin(self, amount):
        pin = int(input('Podaj pin:'))
        if pin == 1597:
            self.__withdraw(amount)
        else:
            print('Zły PIN!!!')
