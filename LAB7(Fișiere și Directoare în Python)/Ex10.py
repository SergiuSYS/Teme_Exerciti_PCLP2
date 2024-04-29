filein = open('LAB7(Fișiere și Directoare în Python)/input.txt','r')
fileout = open('LAB7(Fișiere și Directoare în Python)/output.txt','w')

sir = filein.read()
sir2 = [sir[i:i+8] for i in range(0, len(sir), 8)]
print(sir2)