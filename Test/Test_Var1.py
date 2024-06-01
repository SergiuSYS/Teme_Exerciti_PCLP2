import cv2
import matplotlib.pyplot as plt

imagine = cv2.imread('imagine3.png')

linii = imagine.shape[0]
coloane  = imagine.shape[1]

def filtru():
    for linie in range(linii):
        for coloana in range(coloane-30, coloane):
            pixel = imagine[linie, coloana]
            imagine[linie, coloana] = [pixel[1], pixel[0], pixel[2]]


def Salvare():
    global imagine, linii, coloane
    if linii != coloane:
        imagine = cv2.resize(imagine, (linii, linii))
        linii = coloane = linii

    with open ('ListaPixeliImagine.txt','w') as Fisier:
        for i in range(linii):
            for j in range(coloane):
                if i == j:
                    Fisier.write(f'{imagine[i, j][0]} {imagine[i, j][1]} {imagine[i, j][2]}\n')

def grafic():
    B = []
    G = []
    R = []
    with open('ListaPixeliImagine.txt', 'r') as Fisier:
        for line in Fisier:
            b, g, r = map(int, line.strip().split())
            B.append(b)
            G.append(g)
            R.append(r)

    plt.plot(B, color='blue', label='B')
    plt.plot(G, color='green', label='G')
    plt.plot(R, color='red', label='R')
    plt.xlabel('Abscisa')
    plt.ylabel('Ordonata')
    plt.title('Grafic cu vlorile pixelilor')
    plt.legend()
    plt.show()

filtru()
Salvare()
grafic()

cv2.imshow('imagine', imagine)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
