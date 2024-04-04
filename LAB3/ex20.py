# Definirea listelor prenume și varsta
prenume = ['Mihai', 'George', 'Ana', 'Dan', 'Ion', 'Geta', 'Vio']
varsta = [14, 23, 15, 14, 12, 41, 39]
 
print("a) Afișarea numelor și vârstelor:")
for i in range(len(prenume)):
    print(f"{prenume[i]} are varsta de {varsta[i]} ani.")
 
print("\nb) Adăugarea datelor noi și tipărirea listelor:")
prenume.extend(['Andreea', 'Ioan'])
varsta.extend([34, 23])
print("Lista prenume:", prenume)
print("Lista varsta:", varsta)
 
print("\nc) Ștergerea datelor despre Ana:")
index_ana = prenume.index('Ana')
del prenume[index_ana]
del varsta[index_ana]
print("Lista prenume dupa stergerea lui Ana:", prenume)
print("Lista varsta dupa stergerea lui Ana:", varsta)
 
print("\nd) Ordonarea crescătoare a listelor și afișarea lor:")
prenume.sort()
varsta.sort()
print("Lista prenume ordonata crescator:", prenume)
print("Lista varsta ordonata crescator:", varsta)

 
print("\ne) Ștergerea listei varsta:")
del varsta
 
print("\nf) Afișarea primelor trei elemente din lista prenume:")
print("Primele trei elemente din lista prenume:", prenume[:3])

 
print("\ng) Afișarea ultimelor două elemente din lista prenume:")
print("Ultimele doua elemente din lista prenume:", prenume[-2:])
 
print("\nh) Afișarea listei prenume de la dreapta la stânga:")
print("Lista prenume de la dreapta la stânga:", prenume[::-1])
 
print("\ni) Extinderea listei prenume și afișarea noii liste:")
prenume_extinse = ['Alex', 'Maria']
prenume.extend(prenume_extinse)
print("Lista prenume extinsa:", prenume)


print("\nj) Tipărirea elementelor cu indicii 2 și 4, apoi de la 0 la 5:")
print("Elementul de la indexul 2:", prenume[2])
print("Elementul de la indexul 4:", prenume[4])
print("Elementele de la indexul 0 la 5:", prenume[:6])
