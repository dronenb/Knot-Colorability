import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class EndScene(Scene):
    def construct(self):
        title = TextMobject("Topics to Investigate")
        title.scale(1.5)
        title.to_edge(UP)

        inv1 = TextMobject("Alexander Polynomial")
        inv2 = TextMobject("Surfaces and Genus")
        inv3 = TextMobject("Braids")
        inv4 = TextMobject("Linking Number")
        more = TextMobject("...and so much more")

        self.play(FadeIn(title))

        self.play(FadeIn(inv1))
        self.play(ApplyMethod(inv1.shift, LEFT * 3 + UP * 1.0))

        self.play(FadeIn(inv2))
        self.play(ApplyMethod(inv2.shift, RIGHT * 3 + UP * 1.0))

        self.play(FadeIn(inv3))
        self.play(ApplyMethod(inv3.shift, LEFT * 3 + DOWN * 1.0))

        self.play(FadeIn(inv4))
        self.play(ApplyMethod(inv4.shift, RIGHT * 3 + DOWN * 1.0))

        self.play(FadeIn(more))
        self.play(ApplyMethod(more.shift, DOWN * 2.5))

        self.wait()
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()

