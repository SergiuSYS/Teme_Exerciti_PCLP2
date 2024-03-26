'''
Dându-se două numere naturale cu maxim patru cifre fiecare în variabilele a şi b, 
se cere să se afișeze câte numere impare sunt mai mici sau egale cu b şi mai mari sau egale cu a.
'''
a = int(input("Introduceți primul număr (cu cel mult 4 cifre): "))
b = int(input("Introduceți al doilea număr (cu cel mult 4 cifre): "))
 
numere_impare = 0

for numar in range(a, b + 1):
    if numar % 2 != 0:
        numere_impare += 1

print("Numere impare între", a, "și", b, "sunt:", numere_impare)