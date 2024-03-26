'''
Se dau două numere naturale cu cel mult 9 cifre fiecare. Se cere să se afișeze acel număr care are penultima cifră mai mare.
'''
numar_initial = 462999977
numar2_initial = 144612864
k = 0

while numar_initial > 0:
    k += 1
    numar = numar_initial
    numar2 = numar2_initial
    cifra1 = numar % 10  
    numar = numar // 10 
    cifra2 = numar2 % 10  
    numar2 = numar2 // 10 
    if k == 2:
        if cifra1 > cifra2:
            print(numar_initial)
        else:
            print(numar2_initial)
        break  
#se putea face mai frumos dar ayaye :)