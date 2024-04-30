import matplotlib.pyplot as plt
import numpy as np
import csv

valori = []
fructe = []

with open('LAB8(Grafice in Python)/fructe.csv', 'r', encoding='utf-8-sig') as csvFile:
    csvReader = csv.reader(csvFile)
    next(csvReader)
    for line in csvReader:
        fructe.append(line[0])
        valori.append(int(line[1]))
    print(fructe)

max_index = valori.index(max(valori))
explode = [0] * len(valori)
explode[max_index] = 0.1
plt.pie(valori,labels = fructe,explode=explode)
plt.show()
    









