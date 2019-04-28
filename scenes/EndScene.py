import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class EndScene(Scene):
    def construct(self):
        title = TextMobject("Invariants to Look Into")
        title.scale(1.5)
        title.to_edge(UP)

        inv1 = TextMobject("invarient1")
        inv2 = TextMobject("invarient2")
        inv3 = TextMobject("invarient3")
        inv4 = TextMobject("invarient4")

        self.play(FadeIn(title))

        self.play(FadeIn(inv1))
        self.play(ApplyMethod(inv1.shift, LEFT * 3 + UP * 1.0))

        self.play(FadeIn(inv2))
        self.play(ApplyMethod(inv2.shift, RIGHT * 3 + UP * 1.0))

        self.play(FadeIn(inv3))
        self.play(ApplyMethod(inv3.shift, LEFT * 3 + DOWN * 1.0))

        self.play(FadeIn(inv4))
        self.play(ApplyMethod(inv4.shift, RIGHT * 3 + DOWN * 1.0))

        self.wait()
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()

