def bisiesto(x):
    if x % 4 == 0 and x % 100 !=0 or x % 400 == 0:
        print("bisiesto")
    else:
        print("no es bisiesto")
        
bisiesto(2023)
