from point import Point
from vector import Vector

a = Point(3,2)
b = Point.generate_random(10,10)

print(a,b)
print(a.euclidean_distance(b))
print(a>b)

v = Vector(a,b)
print(v.slope())
