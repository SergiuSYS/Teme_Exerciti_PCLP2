#Se citesc de la tastatură coeficienții ecuației de gradul 2. Să se afișeze cât este x.
#Formă generală: ax2+bx+c=0.

import sympy as sp

a = int(input("introduceti a: "))
b = int(input("introduceti b: "))
c = int(input("introduceti b: "))
x = sp.symbols('x')

ecuatie = a*x**2+b*x+c

solutie = sp.solve(ecuatie,x)
print("x este: ", solutie)
