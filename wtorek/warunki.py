# znaPython = False
#
# if znaPython:
#    print("Gratulacje")
# else:
#    print("Musisz się nauczyć")
#
# print("...Kolejne instrukcje programu...")

# znaPython = input("Czy znasz język?")
#
# if znaPython == "tak" or znaPython == "Tak" or znaPython == "t":
#     print("Gratulacje")
# elif znaPython == "nie":
#     print("Musisz się nauczyć")
# else:
#     print("Nie ma takiego wyboru")
#
# print("...Kolejne instrukcje programu...")

# podatek = 3000
# if 500 < podatek < 1000:
#     oplata = 0.0
# elif podatek < 3000:
#     oplata = 0.2
# elif podatek < 5000:
#     oplata = 0.35
# elif podatek != 9999:
#     oplata = -0.2
# else:
#     oplata = 0.45
#
# print(oplata)

# zamowienie = 250
#
# if zamowienie > 100:
#     rabat = 0.10
# else:
#     rabat = 0.0
#
# print(f"Twoje zamówienie na kwotę {zamowienie} otrzymuje rabat w wysokości: {rabat}")

# zamowienie = 250
#
# rabat = 0.10 if zamowienie > 100 else 0.0
# print(f"Twoje zamówienie na kwotę {zamowienie} otrzymuje rabat w wysokości: {rabat}")

alert = 'console'
error = 'critical'
message = 'warning!!!'

if alert == 'console':
    print(message)
elif alert == 'email':
    if error == 'critical':
        print("Wysyłam maila....")
    elif error == 'medium':
        print("Wysyłam mniej ważnego maila....")
    else:
        print("Wysyłam maila ale później")
else:
    print("Błędny status alertu")
