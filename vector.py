from point import Point

class Vector:

    def __init__(self,p1,p2):

        if isinstance(p1,Point) and isinstance(p2,Point):
            self.x = p2.x - p1.x
            self.y = p2.y - p1.y

        else :
            raise TypeError("Vector needs to be defined by two Points.")
        
    def __gt__(self,other):
        return self.slope() > other.slope()
    
    def __lt__(self,other):
        return self.slope() < other.slope()
    
    def slope(self):
        if self.x == 0:
            return float('inf') if self.y > 0 else float('-inf')
        return self.y / self.x

    def scalar_product(self,v):

        if isinstance(v,Vector):
            return Vector(self.x * v.x + self.y * v.y)
        
        elif isinstance(v,(int,float)):
            return Vector(v*self.x,v*self.y)
        
        else :
            raise TypeError("Scalar Product only possible between 2 vectors or vector and numeric value.")
        
    def determinant(self,v):
        
        if isinstance(v,Vector):
            return Vector(self.x * v.y - self.y * v.x)
        else :
            raise TypeError("Determinant only possible between 2 vectors.")
        
    def power(m):
        if isinstance(m,Point):
            pass
        else:
            pass
    
