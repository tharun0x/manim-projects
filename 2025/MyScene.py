from manimlib import *

class SquareToCircle(InteractiveScene):
    def construct(self):
        square = Square(side_length=2)
        circle = Circle(radius=3)
        self.add(square, circle)
        self.play(Transform(square, circle))
        self.add(Axes())
        self.wait(1)
        
