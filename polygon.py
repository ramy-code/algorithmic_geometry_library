from math import atan2
from point_cloud import PointCloud
import turtle
class Polygon:

    def __init__(self,contour):
        if isinstance(contour,PointCloud):
            self.contour = contour
        else :
            raise TypeError("Contour of Polygon needs to be a cloud of Points.")

    
    def __str__(self):
        return str(self.contour)

    def polar_sort(self,center=(0,0)):
        self.contour.points = sorted(self.contour.points, key=lambda vertex: (atan2(vertex.y - center[1], vertex.x - center[0])))

    def draw(self):
        self.polar_sort()
        turtle.penup()
        first_point = self.contour.points[0]
        turtle.goto(first_point.x,first_point.y)
        turtle.pendown()
        for point in self.contour.points:
            turtle.goto(point.x,point.y)
        turtle.goto(first_point.x,first_point.y)