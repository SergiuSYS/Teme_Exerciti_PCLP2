filein = open('LAB7(Fișiere și Directoare în Python)/input.txt','r')
fileout =  open('LAB7(Fișiere și Directoare în Python)/output.txt','w')
a = []
filein.seek(0)
for i in filein.read():
    if i.isdigit():
        a.append(i)
fileout.write(' '.join(a))
filein.close()

