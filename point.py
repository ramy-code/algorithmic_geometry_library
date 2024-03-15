import random
import math
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"({self.x} , {self.y})")

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    
    def __gt__(self,other):
        if (self.x > other.x and self.y >= other.y) or (self.x >= other.x and self.y > other.y):
            return True
        else :
            return False
        
    def __lt__(self,other):
        if (self.x < other.x and self.y <= other.y) or (self.x <= other.x and self.y < other.y):
            return True
        else :
            return False 
        
    @classmethod
    def generate_random(cls,max_x,max_y):
        return Point(round(random.uniform(0,max_x),3),round(random.uniform(0,max_y),3))

    def euclidean_distance(self,other):
        if isinstance(other,Point):
            return round( math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2) , 3)
        else:
            raise TypeError("Can only compute distance between two Points.")
    