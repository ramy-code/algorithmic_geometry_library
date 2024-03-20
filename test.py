from point import Point
from vector import Vector
from point_cloud import PointCloud
from polygon import Polygon
import turtle

a = Point(30,22)
b = Point.generate_random(100,100)
c = Point.generate_random(100,100)
d = Point.generate_random(100,100)
turtle.setup(500, 500)  
turtle.setworldcoordinates(0, 500, 500, 0)

cld = PointCloud([a,b,c,d])
poly = Polygon(cld)
turtle.speed(0)
cld.draw()
poly.draw()
turtle.hideturtle()
turtle.done()