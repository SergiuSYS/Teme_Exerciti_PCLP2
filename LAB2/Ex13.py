'''
Să se realizeze un program care citește două numere reale de la tastatură și apoi afișează un meniu cu următoarele opțiuni:
a. Suma numerelor introduse
b. Diferența numerelor introduse
c. Produsul numerelor introduse
d. Raportul numerelor introduse
e. Media aritmetică a numerelor
'''

a = int(input("introduceti a: "))
b = int(input("introduceti b: "))

while(1):
    print("1. Suma numerelor introduse")
    print("2. Diferența numerelor introduse")
    print("3. Produsul numerelor introduse")
    print("4. Raportul numerelor introduse")
    print("5. Media aritmetică a numerelor")

    n = int(input("introduceti optiunea: "))

    match(n):
        case 1:
            print("suma numerelor este: ", a+b)
        case 2:
            print("Diferența numerelor este: ", a-b)
        case 3:
            print("produsul numerelor este: ", a*b)
        case 4: 
            if(b ==0):
                print("raportul nu este posibil")
            else:
                print("raportul numerelor este: ", a/b)
        case 5:
            print("media aritmetica a numerelor este: ", (a+b)/2)



