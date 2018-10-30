# Exercise 4
# Create a calculator

def calculator (x, caracters, y):
    if caracters == "+":
        return x+y
    elif caracters =="-":
        return x-y
    elif caracters =="*":
        return x*y
    elif caracters =="/":
        return x/y
    elif caracters =="%":
        return x%y
    else:
        return ("caracters error")

while  __name__ =="__main__":
    x = int(input("insert the first number "))
    y = int(input("insert the second number"))
    caracters= str(input("the caracters is: "))
    print(calculator(x, caracters, y))
