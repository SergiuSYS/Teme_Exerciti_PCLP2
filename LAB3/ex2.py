n = int(input("introduceti un numar: "))
k = 1
for i in range(1, n + 1):
    if(n % i != 0):
        k+=1
if(k == 2):
    print("numarul este prim")
else:
    print("numarul nu este prim")