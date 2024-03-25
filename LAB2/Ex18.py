for i in range(5):
    x = int(input("introduceti x: "))
    if x<0:
        print("rezultatul este: ", x**2-2)
    elif x==0:
        print("rezultatul este: ", 3)
    else:
        print("rezultatul este: ", x+2)
