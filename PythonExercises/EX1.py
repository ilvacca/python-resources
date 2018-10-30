from math import sqrt

def insert_cathetus2():
    while True:
        try:
            c1 = float(input("Cathetus 1:"))
            c2 = float(input("Cathetus 2:"))
            return (c1, c2)
        except:
            print("Error")
            

def insert_cathetus():
    try:
        c1=float(input("Insert the first one: "))
        c2=float(input("Insert the second one: "))
        return c1,c2
    except ValueError:
        print("not valid")
        return insert_cathetus()

c1,c2=insert_cathetus2()
h=sqrt(c1**2+c2**2)
print("L'ipotenusa è: %0.2f" %h)
