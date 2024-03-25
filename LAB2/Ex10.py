#Se citesc de la tastatură 4 variabile de tip întreg. Să se afișeze variabilele în ordine descrescătoare.

a = int(input("introduceti a: "))
b = int(input("introduceti b: "))
c = int(input("introduceti c: "))
d = int(input("introduceti c: "))

print(sorted([a,b,c,d], reverse=True))