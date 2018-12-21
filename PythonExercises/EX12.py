#ESERCIZIO 12
'''Write a function that gives a set of students and grades associated with them returns a dictionary 
of students and grades associated with them, divided by letter of surname. 
The keys are the groups (a-f), (g-o), (p-z), the values, the student lists and the grades.
Define the function of inserting and deleting a given student in the newly created dictionary.
Define the function that inserts a list of grades for a student in the dictionary.'''

class Subject:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

class Studente:

    def __init__(self, Nome, Cogn):
        self.Nome = Nome
        self.Cogn = Cogn
        self.materie = []

    def __str__(self):
        return "Dati personali di:"+ self.Nome + self.Cogn + self.materie

    def add_subj(self, name, mark):
        subj = Subject(name, mark)
        self.materie.append(subj.__dict__)

class Classe:
    def __init__(self):
        self.classeAF = []
        self.classeGO = []
        self.classePZ = []

    def add_stud(self,student):
        if student.Cogn[0] in "ABCDEF":
            self.classeAF.append(student.__dict__)
        elif student.Cogn[0] in "GHIKLMNO":
            self.classeGO.append(student.__dict__)
        elif student.Cogn[0] in "PQRSTUVWYXZ":
            self.classePZ.append(student.__dict__)
        else:
            print("error")

s1 = Studente("Pippo", "Baudo")
s1.add_subj("Matematica",7)
s1.add_subj("Fisica",8)
classe = []
classe.append(s1.__dict__)
s2 = Studente("Andrea", "Rossi")
s2.add_subj("Matematica",5)
s1.add_subj("Fisica",6)
classe.append(s2.__dict__)
c1 = Classe()
c1.add_stud(s1)
c1.add_stud(s2)
c1.__dict__
