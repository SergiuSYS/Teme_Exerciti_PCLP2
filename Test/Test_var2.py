import cv2
import csv
import matplotlib.pyplot as plt

imagine = cv2.imread('images.png')
linii = imagine.shape[0]
coloane  = imagine.shape[1]

numeFisier = input('introduceti numele fisierului in care se vor salva datele: ')
def filtru():
    for i in range(linii):
        for j in range(coloane):
            if imagine[i,j][1] > 50:
                imagine[i,j][2] = imagine[i,j][2] + 50
                    
def Salvare():
    with open (f'{numeFisier}.txt','w') as Fisier:
        for j in range(coloane):
            Fisier.write(f'{imagine[linii-1, j][0]} {imagine[linii-1, j][1]} {imagine[linii-1, j][2]}\n')

def grafic():
    B = []
    G = []
    R = []
    valb = valg = valr = 0
    with open(f'{numeFisier}.txt', 'r') as Fisier:
        for line in Fisier:
            b, g, r = map(int, line.strip().split())
            B.append(b)
            if b > 120:
                valb += 1
            G.append(g)
            if g > 120:
                valg += 1
            R.append(r)
            if r > 120:
                valr += 1
    lista_valori = [valb, valg, valr]
    sorted_indices = sorted(range(len(lista_valori)), key=lambda k: lista_valori[k], reverse=True)

    for i, idx in enumerate(sorted_indices, start=1):
        if idx == 0:
            plt.subplot(1, 3, i)
            plt.plot(B, color='blue')
            plt.title('Blue Channel')
            plt.xlabel('Pixel Index')
            plt.ylabel('Pixel Value')
        elif idx == 1:
            plt.subplot(1, 3, i)
            plt.plot(G, color='green')
            plt.title('Green Channel')
            plt.xlabel('Pixel Index')
            plt.ylabel('Pixel Value')
        else:
            plt.subplot(1, 3, i)
            plt.plot(R, color='red')
            plt.title('Red Channel')
            plt.xlabel('Pixel Index')
            plt.ylabel('Pixel Value')

    plt.tight_layout()
    plt.show()
 
filtru()
Salvare()
grafic()

cv2.imshow('imagine', imagine)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
