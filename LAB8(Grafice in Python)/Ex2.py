import matplotlib.pyplot as plt
import numpy as np

filein = open('LAB8(Grafice in Python)/input.txt','r')
fileout = open('LAB8(Grafice in Python)/output.txt','w')
'''
dx = filein.readline().strip().split(' ')
dy = filein.readline().strip().split(' ')

plt.plot(dx,dy)
plt.show()

'''
#citirea unui sir de numere(charactere) transformate in int
#dx = [int(x) for x in filein.readline().strip().split(' ')] 
#dy = [int(y) for y in filein.readline().strip().split(' ')]

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
#colors = np.random.randint(100, size=(100))
#sizes = 10 * np.random.randint(100, size=(100))
plt.bar(x, y,color="DarkMagenta" ,width = 0.3)
#plt.plot(dx,dy) 
#plt.plot(y)
plt.show()

#plot gafic cu linie 
#pie grafic tip placinta
#scatter grafic in care se pun doar puncte
#bar grafic cu dreptunghiuri
