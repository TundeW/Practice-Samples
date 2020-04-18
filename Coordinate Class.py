#Coordinates and Vectors.
#This is a class that represents the x,y plane coordinate system(A vector).
#It has a distance method to find the scalr distance between two instances of the coordinate(DISTANCE BETWEEN TWO VECTORS)
#It has a sub method that subtracts the x values and y values of two vector instances. and returns a new instance with the resulting x and y values as the coordinates.(VECTOR SUBTRACTION)


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance (self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq )**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__ (self, other):
        return Coordinate(self.x-other.x, self.y-other.y)
