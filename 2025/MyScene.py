from manimlib import *

class SquareToCircle(InteractiveScene):
    def construct(self):
        square = Square(side_length=2)
        circle = Circle(radius=5)
        self.add(square, circle)
        self.play(Transform(square, circle), run_time=8)
        self.wait(2)
        
# class mob(Mobject):
#     def construct(self):
         