import matplotlib.pyplot as plt
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

class Circle:
    def __init__(self, center : point, radius : float):
        self.center: point = center
        self.radius: float = radius

    def area(self):
        return math.pi*self.radius**2

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()





