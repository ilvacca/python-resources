# Exercise 5
#
# Given 6
# 1?2?3?4?5?6
# 1?2?3?4?5
# 1?2?3?4
# 1?2?3
# 1?2
# 1

##n=-1
##while n<0:
##    n=int(input('Digita numero positivo: '))
##    if n<0:
##        print('ridigita')
##
##for i in range(n,0,-1):
##    stringa=str(1)
##    for t in range(2,i+1):
##        stringa+='?'+str(t)
##    print(stringa)


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
