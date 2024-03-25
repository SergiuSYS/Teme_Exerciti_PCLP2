'''
Dându-se un număr natural cu exact patru cifre în variabila n, se cere să se afișeze câte cifre impare conține?
'''
n = str(input("intro du numarul n: "))

for i in n:
    cifra_int = int(i)
    if cifra_int %2 != 0:
        print(cifra_int)

