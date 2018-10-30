# Exercise 2
# Feet conversion

def take_input():
    try:
        p=float(input("Insert feet value: "))
        return p
    except:
        print("Value not valid")
        return take_input

def feet_to_yards(feet):
    return feet/3

def feet_to_pollici(feet):
    return feet*12

def feet_to_cm(feet):
    return feet_to_pollici(feet)*2.54

def feet_to_m(feet):
    return feet_to_cm(feet)/100

def converti(feet):
    print(str(feet) + "feet= " + str(feet_to_yards(feet)) + " yards")
    print(str(feet) + "feet= " + str(feet_to_pollici(feet)) + " pollici")
    print(str(feet) + "feet= " + str(feet_to_cm(feet)) + " cm")
    print(str(feet) + "feet= " + str(feet_to_m(feet)) + " m")

# Execute code
if __name__ == "__main__":
    converti(take_input())