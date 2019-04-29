import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

class IntroKnot(KnotScene):
    def construct(self):
        line = Line((-3, 0, 0), (3, 0, 0))
        self.play(ShowCreation(line))
        self.wait()

        un = Knot()

        self.play(Transform(line, un))
        self.wait(0.2)

        tref = Knot("3_1")
        f8 = Knot("4_1")

        self.play(Transform(line, tref))
        self.wait(0.2)

        self.play(Transform(line, f8))

        self.wait()
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()