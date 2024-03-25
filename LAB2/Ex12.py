#Se citește de la tastatură un număr întreg cuprins între 28 si 31. Să se afișeze lunile din an ce au maxim n zile n<=31.

zile_luni = {
    "ianuarie": 31,
    "februarie": 28,
    "martie": 31,
    "aprilie": 30,
    "mai": 31,
    "iunie": 30,
    "iulie": 31,
    "august": 31,
    "septembrie": 30,
    "octombrie": 31,
    "noiembrie": 30,
    "decembrie": 31
}

n = int(input("Introduceti un numar intreg intre 28 si 31: "))

 
print("Lunile din an ce au maxim", n, "zile sunt:")
for luna, zile in zile_luni.items():
    if zile <= n:
        print(luna.capitalize())