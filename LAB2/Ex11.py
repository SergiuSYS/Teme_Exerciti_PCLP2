#Se dau de la tastatură numele și nota la informatică pentru doi elevi. 
#Se cere să se afișeze numele elevilor în ordinea descrescătoare a notei la informatică. 
#Dacă amândoi elevii au aceeași medie se va afișa primul, cel care are numele alfabetic mai mic

nume1 = str(input("introduceti numele: "))
nota1 = int(input("introduceti nota: "))

nume2 = str(input("introduceti numele: "))
nota2 = int(input("introduceti nota: "))

elevi = [(nume1, nota1),(nume2, nota2)]

sortare = sorted(elevi,key =lambda x:(-x[1],x[0]))

for elev in sortare:
    print(elev[0], "-", elev[1])