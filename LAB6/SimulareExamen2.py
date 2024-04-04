a = int(input("Introdu câte nume dorești să introduci: "))

vocale = ['a', 'e', 'i', 'o', 'u']
numeCuVocale = []

for i in range(a):
    nume_familie = input("Introduceți numele de familie: ").split()
    numeCuVocale.extend([nume for nume in nume_familie if nume[-1] in vocale])

print("Numele care conțin vocale la sfârșit sunt:", numeCuVocale)
