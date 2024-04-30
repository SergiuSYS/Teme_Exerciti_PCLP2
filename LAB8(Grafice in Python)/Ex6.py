import matplotlib.pyplot as plt

filein = open('LAB8(Grafice in Python)/input.txt', 'r') 
ae = ['a', 'b', 'c', 'd', 'e']
fj = ['f', 'g', 'h', 'i', 'j']
ko = ['k', 'l', 'm', 'n', 'o']
pt = ['p', 'q', 'r', 's', 't']
uz = ['u', 'v', 'x', 'y', 'z']

count_directory = {'ae': 0, 'fj': 0, 'ko': 0, 'pt': 0, 'uz': 0}
nume = filein.read().strip()

for i in nume:
    for key in count_directory:
        if i in globals()[key]:
            count_directory[key] += 1
            break

label = list(count_directory.keys())
counts = [count_directory[key] for key in label]

plt.bar(label,counts)
plt.show()