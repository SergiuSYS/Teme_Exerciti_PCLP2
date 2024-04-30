import matplotlib.pyplot as plt

n = int(input('introduceti marimea sirurilor: '))
dx = [int(input('introdu un numar pentru dx: ')) for _ in range(n)]
dy = [int(input('introdu un numar pentru dy: ')) for _ in range(n)]
culoare = input('introduceti o culoare: ')
linie = input('introduceti tipul de linie: ')
plt.plot(dx,dy, color = f'{culoare}',ls = f'{linie}')
plt.show()