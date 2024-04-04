while True:
    n = int(input("Introduceți un număr: "))
    
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
