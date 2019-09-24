# Exercise 10

class Time:
    def __init__(self, ora, minuto, secondo):
        self.ora=self.set_ora(ora)
        self.minuto=self.set_minuto(minuto)
        self.secondo=self.set_secondo(secondo)

    def set_ora(self, ora):
        if ora>=0 and ora<24:
            return ora
        else:
            print("Insert a value between 0 & 24")
            return 0

    def set_minuto(self, minuto):
        if minuto>=0 and minuto <60:
            return minuto
        else:
            print("Insert a value between 0 & 60")
            return 0

    def set_secondo(self, secondo):
        if secondo>=0 and secondo <60:
            return secondo
        else:
            print("Insert a value between 0 & 60")
            return 0

    def __str__(self):
        return ("%02d:%02d:%02d" %(self.ora, self.minuto, self.secondo))
    
class Appuntamento:
    def __init__(self, inizio, fine, descrizione):
        self.inizio=inizio
        self.fine=fine
        self.descrizione=descrizione

    def set_inizio(self, inizio):
        self.inizio= inizio

    def set_fine(self, fine):
        self.fine= fine

    def set_descrizione(self, descrizione):
        self.descrizione=descrizione

    def __str__(self):
        return ("Time inizio: " + str(self.inizio) +"\nTime fine: " + str(self.fine)+"\nDescrizione: "+ self.descrizione)

if __name__== "__main__":
    t1=Time(22,2,9)
    t2=Time(23,30,0)
    appuntamento=Appuntamento(t1, t2, "Meeting deep learning")
    print(appuntamento)
