filein = open('LAB7(Fișiere și Directoare în Python)/input.txt','r')
fileout =  open('LAB7(Fișiere și Directoare în Python)/output.txt','w')

fileout.write(('propozitia are ' + str(len(filein.read().split(' '))) + ' cuvinte'))