'''
Se dau două numere naturale cu cel mult 4 cifre fiecare. 
Se cere să se verifice dacă primul se împarte exact la ultima cifră a celui de-al doilea (se va afișa DA sau NU).
'''
numar1 = int(input("Introduceți primul număr: "))
numar2 = int(input("Introduceți al doilea număr: "))

ultimaCifra = numar2 % 10

if ultimaCifra != 0 and numar1 % ultimaCifra == 0:
    print("DA")
else:
    print("NU")