filein = open('LAB7(Fișiere și Directoare în Python)/input.txt','r')
fileout = open('LAB7(Fișiere și Directoare în Python)/output.txt','w')

vocale = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 

#prin iterare
var = filein.read().split(' ')
a =[]
for i in var:
    if i[0] in vocale:
        a.append(i)
fileout.write(' '.join(a))

fileout.write('\n')#doar pentru a fi printate pe lini separate

#prin comprehesiunea sirurilor 
with open('LAB7(Fișiere și Directoare în Python)/input.txt', 'r') as filein:  
    fileout.write(' '.join([word for word in filein.read().split() if word and word[0] in vocale]))  
filein.close()
