'''
Se dă un număr natural cu maxim 9 cifre în variabila n. Se cere să se determine ultima cifră a puterii 3^n
'''
n = int(input("Introduceți un număr natural (cu cel mult 9 cifre): "))
 
ultima_cifra_n = n % 10
putere3 = ultima_cifra_n % 4
rezultat = 3 ** putere3

print("Ultima cifră a puterii 3^", n, "este:", rezultat)