# def drukuj_napis():
#     print("NAPIS")
#
# lista = [drukuj_napis (),drukuj_napis(),'Tomek']
# print(lista)

def drukuj_napis():
    print("NAPIS")


def drukarka(tekst, ile_razy):
    wydruk = (tekst + " ") * ile_razy
    return wydruk

def drukarka2(tekst, ile_razy):
    return (tekst + " ") * ile_razy

def drukarka3(tekst='Hello', ile_razy=3):
    return (tekst + " ") * ile_razy


lista = [drukarka("NAPIS", 5), drukarka2("NAPIS", 2), drukarka3("coś",2), "tomek"]
print(lista)

