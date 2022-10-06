# TODO : Student Class --> name fives tens twenties
class Student(): 
    def __init__(self, name="", fives=0, tens=0, twenties=0):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        
    # TODO : wealth methode --> return total wealth
    def wealth(self):
        return self.fives*5 + self.tens*10 + self.twenties*20
    
    # TODO : compare methode --> 1 arg Student return the richer
    def compare(self, other):
        return self.name if self.wealth() > other.wealth() else other.name
        
    # TODO : advanced_compare --> 1 arg list of Student return sorted list the most to least
    def advanced_compare(self, student):
        stud_dict = {self.name:self.wealth()}
        for i in student:
            stud_dict[i.name] = i.wealth()
        return sorted(stud_dict)