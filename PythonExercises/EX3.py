def get_coefficients():
    a=float(input("Insert a: "))
    b=float(input("Insert b: "))
    c=float(input("Insert c: "))
    d=float(input("Insert d: "))
    e=float(input("Insert e: "))
    f=float(input("Insert f: "))
    return a,b,c,d,e,f
    
def determinante(a,b,c,d):
    delta=a*d-c*b
    return delta

def find_y(a,c,e,f,det):
    y= (a*f - c*e)/det
    return y

def find_x (b,d,e,f,det):
    x= (e*d-f*b)/det
    return x

    
if __name__=="__main__":
    a,b,c,d,e,f = get_coefficients()
    det = determinante(a,b,c,d)
    print("la x vale: ",find_x(b,d,e,f,det))
    print("la y vale: ",find_y(a,c,e,f,det))
