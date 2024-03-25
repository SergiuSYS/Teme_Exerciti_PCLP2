'''
Se dau două numere naturale cu cel mult 5 cifre fiecare. Se cere să se înmulțească primul cu ultima cifră a celui de-al doilea număr, 
iar al doilea cu ultima cifră a primului număr, după care să se afișeze suma lor.
'''

numar1 = int(input("Introduceți primul număr: "))
numar2 = int(input("Introduceți al doilea număr: "))

 
ultima_cifra_numar1 = numar1 % 10
ultima_cifra_numar2 = numar2 % 10

suma = (numar1 * ultima_cifra_numar2) + (numar2 * ultima_cifra_numar1)
print(suma)