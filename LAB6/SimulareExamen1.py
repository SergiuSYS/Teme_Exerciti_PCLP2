numar = (input("introduceti un numar de minim 4 cifre: "))
numarNou = []
for n in numar:
    cifra_int = int(n)
    if cifra_int %2 != 0:
        numarNou.append(n)
print(*numarNou)
        
