'''
Să se scrie un program în care se citește de la tastatură un număr şi se afișează
toți divizorii acestuia.
'''

a = int(input("Enter a number: "))
k = 0
for i in range(1, a+1): # punem (1,a+1) pentru ca nu vrem sa inecapa i de la 0
    if a % i == 0:      # si a +1 pentr a il include si pe a 
        k = k+1
if k == 2:
    print("este prim")
else:
    print("nu este prim")