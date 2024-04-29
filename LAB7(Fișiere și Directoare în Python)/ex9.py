filein = open('LAB7(Fișiere și Directoare în Python)/input.txt','r')
fileout = open('LAB7(Fișiere și Directoare în Python)/output.txt','w')

sir = [i for i in filein.read().split('1') if i !='']
for i in sir:
    fileout.writelines((''.join(i) + '\n'))