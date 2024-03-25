#se citesc de la tastatura coeficentii ecuatiei de gradul 1 sa se afiseze cat este x 
# ax+b =0

# folosesti pip install sympy pentru a instala biblioteca
import sympy as sp

a = int(input("introduceti a: "))
b = int(input("introduceti b: "))
x = sp.symbols('x')

ecuatie = a*x+b

solutie = sp.solve(ecuatie,x)
print("x este: ", solutie)

