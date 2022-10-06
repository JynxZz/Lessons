from math import ceil 

class Potion:
    def __init__(self, color, volume):
        self.color = color 
        self.volume = volume
    
    def mix(self, other):
        
        #TODO : New Volume & Ratio 
        new_volume = self.volume + other.volume 
        
        ratio_potion = self.volume / new_volume
        ratio_other = other.volume / new_volume
        
        #TODO : New Colors 
        new_color_1 = ceil(ratio_potion * self.color[0] + ratio_other * other.color[0])
        new_color_2 = ceil(ratio_potion * self.color[1] + ratio_other * other.color[1])
        new_color_3 = ceil(ratio_potion * self.color[2] + ratio_other * other.color[2])
        
        #TODO : Return New Potion 
        return Potion((new_color_1, new_color_2, new_color_3), new_volume)