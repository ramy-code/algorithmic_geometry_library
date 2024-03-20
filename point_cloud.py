import turtle 
from point import Point
class PointCloud:

    def __init__(self, points = []):
        self.points = points
        if not isinstance(points,list):
            raise TypeError("Point Cloud needs to be initialized with a list of points or empty list")
        elif len(points) > 0 :
            is_point = [ True if isinstance(p,Point) else False for p in points]
            if not all(is_point) : 
                raise TypeError("Point Cloud needs to be a list of points.")

    def __str__(self):
        return f'{[str(point) for point in self.points]}'
    
    @classmethod
    def generate_point_cloud(cls, nb_points, bound_x, bound_y):
        points = [Point.generate_random(bound_x,bound_y) for i in range(nb_points)]
        return points

    def copy(self):
        return [point for point in self.points]

    def add(self,point):
        if isinstance(point,Point):
            self.points.append(point)
        else :
            raise TypeError("Point Cloud is a list of Points")


    def remove(self,point_to_remove):
        if isinstance(point_to_remove,Point):
            for point in self.points:
                if point.x == point_to_remove.x and point.y == point_to_remove.y:
                    self.points.remove(point)
                    return True
            return False
        else :
            raise TypeError('Cannot remove non point from point cloud')

    def sort(self):
        self.points = sorted(self.points,key=lambda point : (point.x,point.y))

    def draw(self):
        for point in self.points :
            point.draw()

