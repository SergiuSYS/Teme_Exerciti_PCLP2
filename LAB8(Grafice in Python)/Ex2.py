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
dx = [int(x) for x in filein.readline().strip().split(' ')] 
dy = [int(y) for y in filein.readline().strip().split(' ')]

plt.plot(dx,dy) 
#plt.plot(y)
plt.show()