import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

etichete = ["Mere", "Cirese", "Banane", "Capsuni"]
culori=["green", "red", "yellow", "pink"]

distanta = [0.2, 0, 0, 0]

plt.pie(y, labels = etichete, colors=culori,explode = distanta)
plt.legend(title = "Fructe:")
plt.show()

