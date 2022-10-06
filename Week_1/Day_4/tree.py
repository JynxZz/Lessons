import random
# TODO : create class OrangeTree
class OrangeTree():
    # TODO : init --> age height fruits dead
    def __init__(self, age=0, height=0, fruits=0, dead=False):
        self.age = age
        self.height = height 
        self.fruits = fruits
        self.dead = dead
        
    def one_year_passes(self):
        # TODO: age the tree by one year
        self.age += 1
        self.check_alive()
        if not self.dead :
            self.height_grow()
            self.grow_fruits()
        
    
    def pick_a_fruit(self):
        if self.fruits > 1 :
            self.fruits -= 1
            
    # TODO: check if the tree has survived    
    def check_alive(self):
        if self.age > 100:
            self.dead = True
        elif self.age > 50:
            dice = random.randint(0, 100)
            if dice < 50:
                self.dead = True 
        return self.dead 
    
    # TODO: if so, make the tree height grow
    def height_grow(self):
        if self.age <= 10:
            self.height += 1
        return self.height
    
    # TODO: if so, make the tree grow fruits
    def grow_fruits(self):
        self.fruits = 0
        if self.age <= 5:
            self.fruits = 0
        elif self.age < 10:
            self.fruits += 100
        elif self.age < 15:
            self.fruits += 200
        else: 
            self.fruits = 0
        return self.fruits
