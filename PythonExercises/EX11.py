# Exercise 11

class Person:
    def __init__(self, name, surname, ss_number):
        self.name= name
        self.surname= surname
        self.ss_number= ss_number
    def __str__(self):
        return "{0} {1} has the social number {2}".format(self.name, self.surname, self.ss_number)
class Student(Person):
    def __init__(self, name, surname, ss_number, mat_num, degree):
        Person.__init__(self, name, surname, ss_number)
        self.mat_num= mat_num
        self.degree= degree
    def __str__(self):
        return "{0} {1} has the social number {2} and matriculation number {3} and is studying {4}".format(self.name, self.surname, self.ss_number, self.mat_num, self.degree)

if __name__ == "__main__":
    P= Person("khaoula", "Alaoui", "4555")
    S= Student("omar", "saidi", "455", "585", "CS")
    print(P)
    print(S)
