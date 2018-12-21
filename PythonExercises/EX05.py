# Exercise 5

# Write a code that given a number, let's say 6,  returns:
# 1?2?3?4?5?6
# 1?2?3?4?5
# 1?2?3?4
# 1?2?3
# 1?2
# 1

def getNumber():
    while True:
        try:
            n = int(input("Input number: "))
            return(n)
        except:
            print("Error")

n = getNumber()

for i in range(n, 0, -1):
    lista = [str(a) for a in list(range(1,n+1))]
    listaString = "?".join(lista[:i])
    print(listaString)
