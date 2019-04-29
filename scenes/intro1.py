import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

class intro1(KnotScene):
    def construct(self):
        math = TextMobject("Mathematical Knots")
        other = TextMobject("Tied Knots")

        neq = TexMobject(r"\neq")
        neq.scale(1.2)

        math.next_to(neq, UP * 1.2)
        other.next_to(neq, DOWN * 1.2)

        self.play(FadeIn(math))
        self.play(FadeIn(other))
        self.wait()

        self.play(DrawBorderThenFill(neq))

        self.wait()
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()